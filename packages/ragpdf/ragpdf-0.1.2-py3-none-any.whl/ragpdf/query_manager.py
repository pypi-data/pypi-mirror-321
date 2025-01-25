"""Module for processing queries and generating responses."""

from typing import List, Iterator, Union, Dict, Any
from litellm import completion, acompletion


class QueryManager:
    """Processes user queries and generates responses using LLM."""

    def __init__(self, llm_config: Dict[str, Any]):
        """
        Initialize the QueryManager.

        Args:
            llm_config (Dict[str, Any]): Configuration for the language model including:
                - model: Model name
                - api_key: API key
                - base_url: Base URL for the API (optional)
        """
        self.llm_config = llm_config

    def generate_response(
        self, prompt: str, context_chunks: List[str], stream: bool = False
    ) -> Union[str, Iterator[str]]:
        """
        Generate a response using the LLM based on the query and context.

        Args:
            prompt (str): The user's query.
            context_chunks (List[str]): Relevant context chunks from PDFs.
            stream (bool): Whether to stream the response.

        Returns:
            Union[str, Iterator[str]]: The generated response or a stream of response chunks.
        """
        # Prepare the system message with context
        messages = self._prepare_messages(prompt, context_chunks)

        # Generate response
        response = completion(**self.llm_config, messages=messages, stream=stream)
        
        if stream:
            return (chunk.choices[0].delta.content for chunk in response if chunk.choices[0].delta.content is not None)
        else:
            return response.choices[0].message.content

    async def agenerate_response(
        self, prompt: str, context_chunks: List[str], stream: bool = False
    ) -> Union[str, Iterator[str]]:
        """
        Asynchronously generate a response using the LLM based on the query and context.

        Args:
            prompt (str): The user's query.
            context_chunks (List[str]): Relevant context chunks from PDFs.
            stream (bool): Whether to stream the response.

        Returns:
            Union[str, Iterator[str]]: The generated response or a stream of response chunks.
        """
        # Prepare the system message with context
        messages = self._prepare_messages(prompt, context_chunks)

        # Generate response asynchronously
        response = await acompletion(**self.llm_config, messages=messages, stream=stream)
        
        if stream:
            return (chunk.choices[0].delta.content for chunk in response if chunk.choices[0].delta.content is not None)
        else:
            return response.choices[0].message.content

    def _prepare_messages(self, prompt: str, context_chunks: List[str]) -> List[Dict[str, str]]:
        """
        Prepare messages for the LLM with context and prompt.

        Args:
            prompt (str): The user's query.
            context_chunks (List[str]): Relevant context chunks from PDFs.

        Returns:
            List[Dict[str, str]]: List of messages for the LLM.
        """
        context = "\n".join(context_chunks)
        return [
            {"role": "system", "content": "You are a helpful assistant. Use the following context to answer the question. If you cannot find the answer in the context, say so."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {prompt}"}
        ]
