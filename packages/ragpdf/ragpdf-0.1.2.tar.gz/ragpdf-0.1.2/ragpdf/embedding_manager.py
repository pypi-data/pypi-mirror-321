"""Module for managing embeddings generation and storage."""

import asyncio
import os
import numpy as np
from typing import List, Dict, Any, Optional
import faiss
from litellm import aembedding


class EmbeddingManager:
    """Manages embedding generation and storage for PDF chunks."""

    def __init__(self, embedding_config: Dict[str, Any], index_path: Optional[str] = None):
        """
        Initialize the EmbeddingManager.

        Args:
            embedding_config (Dict[str, Any]): Configuration for the embedding model:
                - model: Model name
                - api_key: API key
                - base_url: Base URL for the API (optional)
            index_path (Optional[str]): Path to save/load the FAISS index file. If None,
                                      the index will be kept in memory only.
        """
        self.embedding_config = embedding_config
        self.index_path = index_path
        self.embeddings = None
        self.chunks = []
        self.index = None
        
        # Create the directory for the index if it doesn't exist
        if self.index_path:
            os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
            self._load_index()
    
    def _load_index(self) -> None:
        """Load the FAISS index from disk if it exists."""
        if not self.index_path:
            return
            
        try:
            if os.path.exists(self.index_path):
                print(f"Loading existing index from {self.index_path}")
                self.index = faiss.read_index(self.index_path)
                print("Index loaded successfully")
        except Exception as e:
            print(f"Error loading index from {self.index_path}: {str(e)}")
            self.index = None
    
    def _save_index(self) -> None:
        """Save the FAISS index to disk if index_path is configured."""
        if not self.index_path or not self.index:
            return
            
        try:
            print(f"Saving index to {self.index_path}")
            faiss.write_index(self.index, self.index_path)
            print("Index saved successfully")
        except Exception as e:
            print(f"Error saving index to {self.index_path}: {str(e)}")
        
    async def _generate_single_embedding(self, chunk: str) -> List[float]:
        """
        Generate embedding for a single chunk of text.

        Args:
            chunk (str): Text chunk to generate embedding for.

        Returns:
            List[float]: The embedding vector.
        """
        try:
            response = await aembedding(**self.embedding_config, input=chunk)
            
            # Extract embedding from litellm.types.utils.EmbeddingResponse
            if hasattr(response, 'data') and isinstance(response.data, list) and response.data:
                embedding_data = response.data[0]
                if isinstance(embedding_data, dict) and 'embedding' in embedding_data:
                    return embedding_data['embedding']
            
            raise ValueError(f"Unexpected embedding response format: {response}")
        except Exception as e:
            print(f"Error generating embedding: {str(e)}")
            raise

    async def generate_embeddings(self, chunks: List[str]) -> None:
        """
        Generate embeddings for text chunks and store them.

        Args:
            chunks (List[str]): List of text chunks to generate embeddings for.
        """
        # Generate embeddings for all chunks concurrently
        print("Generating embeddings for chunks...")
        tasks = [self._generate_single_embedding(chunk) for chunk in chunks]
        embeddings = await asyncio.gather(*tasks)
        print("Embeddings generated successfully")
        
        # Store chunks and embeddings
        self.chunks = chunks
        self.embeddings = np.array(embeddings)
        
        # Create FAISS index
        dimension = len(embeddings[0])
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings)
        print("FAISS index created and embeddings added")
        
        # Save index if path is provided
        self._save_index()

    def find_similar_chunks(self, query_embedding: List[float], k: int = 5) -> List[str]:
        """
        Find the k most similar chunks to a query embedding.

        Args:
            query_embedding (List[float]): Query embedding vector.
            k (int): Number of similar chunks to return.

        Returns:
            List[str]: List of similar text chunks.
        """
        if self.index is None or not self.chunks:
            return []

        # Convert query embedding to numpy array
        query_embedding_np = np.array([query_embedding], dtype=np.float32)
        
        # Search for similar vectors
        distances, indices = self.index.search(query_embedding_np, k)
        
        # Return corresponding chunks
        return [self.chunks[i] for i in indices[0]]
