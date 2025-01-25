"""Main module for the RAGPDF package."""

import json
import asyncio
from typing import Union, Iterator, Dict, Any, List, Optional
from litellm import aembedding, acompletion

from .pdf_processor import PDFProcessor
from .embedding_manager import EmbeddingManager
from .models import RAGContext, DocumentChunk, EmbeddingConfig, LLMConfig


class RAGPDF:
    """Main class for the RAGPDF package."""

    def __init__(self, embedding_config: Union[Dict[str, Any], EmbeddingConfig], 
                 llm_config: Optional[Union[Dict[str, Any], LLMConfig]] = None, 
                 index_path: Optional[str] = None):
        """
        Initialize the RAGPDF system.

        Args:
            embedding_config (Union[Dict[str, Any], EmbeddingConfig]): Configuration for the embedding model:
                - model: Model name
                - api_key: API key (optional, default: "")
                - api_base: Base URL for the API (optional, default: None)
            llm_config (Optional[Union[Dict[str, Any], LLMConfig]]): Configuration for the language model:
                - model: Model name
                - api_key: API key (optional, default: "")
                - api_base: Base URL for the API (optional, default: None)
                - temperature: Temperature for response generation (optional)
                - max_tokens: Maximum tokens in response (optional)
            index_path (Optional[str]): Path to save/load the FAISS index file. If None,
                                      the index will be kept in memory only.
        """
        # Convert dict configs to model instances if needed
        if isinstance(embedding_config, dict):
            embedding_config = EmbeddingConfig(**embedding_config)
        if isinstance(llm_config, dict) and llm_config is not None:
            llm_config = LLMConfig(**llm_config)

        self.pdf_processor = PDFProcessor()
        self.embedding_manager = EmbeddingManager(embedding_config.model_dump(exclude_none=True), index_path)
        self.embedding_config = embedding_config
        self.llm_config = llm_config
        self.file_chunks = {}  # Store mapping of chunks to their source files
        self.current_context = None  # Store current RAGContext

    async def setup(self):
        """Setup any async components. Used mainly for testing."""
        pass

    async def add(self, pdf_path: str) -> None:
        """
        Add a PDF to the system.

        Args:
            pdf_path (str): Path to the PDF file.

        Raises:
            FileNotFoundError: If the PDF file doesn't exist.
            PyPDF2.PdfReadError: If there's an error reading the PDF.
        """
        # Extract text from PDF
        chunks = self.pdf_processor.extract_text(pdf_path)
        
        # Store mapping of chunks to source file
        for chunk in chunks:
            self.file_chunks[chunk] = pdf_path
        
        # Generate and store embeddings
        await self.embedding_manager.generate_embeddings(chunks)

    async def _get_query_embedding(self, query: str) -> List[float]:
        """
        Get embedding for a query string.

        Args:
            query (str): Query string to get embedding for.

        Returns:
            List[float]: Query embedding vector.
        """
        response = await aembedding(**self.embedding_config.model_dump(exclude_none=True), input=query)
        
        # Extract embedding from litellm.types.utils.EmbeddingResponse
        if hasattr(response, 'data') and isinstance(response.data, list) and response.data:
            embedding_data = response.data[0]
            if isinstance(embedding_data, dict) and 'embedding' in embedding_data:
                return embedding_data['embedding']
        
        raise ValueError(f"Unexpected embedding response format: {response}")

    async def context(self, query: str, k: int = 5) -> RAGContext:
        """
        Get relevant context for a query.

        Args:
            query (str): The query prompt.
            k (int): Number of similar chunks to return.

        Returns:
            RAGContext: Context information including relevant chunks and metadata.
        """
        # Get query embedding
        query_embedding = await self._get_query_embedding(query)
        
        # Find relevant chunks
        relevant_chunks = self.embedding_manager.find_similar_chunks(query_embedding, k)
        
        # Create document chunks
        chunks = [
            DocumentChunk(
                file=self.file_chunks.get(chunk, 'Unknown source'),
                content=chunk
            )
            for chunk in relevant_chunks
        ]
        
        # Create and store context
        self.current_context = RAGContext(
            query=query,
            chunks=chunks,
            files=list(set(chunk.file for chunk in chunks)),
            total_chunks=len(chunks)
        )
        
        return self.current_context

    async def chat(self, prompt: str, k: int = 5, stream: bool = False) -> Union[str, Iterator[str]]:
        """
        Generate a response using the LLM based on context from the prompt.

        Args:
            prompt (str): The user's prompt.
            k (int): Number of similar chunks to use for context.
            stream (bool): Whether to stream the response.

        Returns:
            Union[str, Iterator[str]]: The LLM's response.

        Raises:
            ValueError: If no LLM configuration is provided.
        """
        if not self.llm_config:
            raise ValueError("LLM configuration is required for chat functionality")

        # Get fresh context for the prompt
        context = await self.context(prompt, k)
        
        # Create system message with context
        messages = [
            {
                "role": "system",
                "content": f"You are a helpful assistant. Use the following context to answer the user's question:\n\n{context.to_string()}"
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        # Get LLM response
        response = await acompletion(
            messages=messages,
            stream=stream,
            **self.llm_config.model_dump(exclude_none=True)
        )

        if stream:
            async def response_generator():
                async for chunk in response:
                    if hasattr(chunk, 'choices') and chunk.choices:
                        content = chunk.choices[0].delta.get('content', '')
                        if content:
                            yield content
            return response_generator()
        else:
            return response.choices[0].message.content

    def to_string(self) -> str:
        """
        Convert the current context to a string representation.

        Returns:
            str: String representation of the current context.
        """
        if not self.current_context:
            return "No context available"
        return self.current_context.to_string()
