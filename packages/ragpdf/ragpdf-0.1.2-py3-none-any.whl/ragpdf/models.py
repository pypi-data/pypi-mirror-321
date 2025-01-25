"""Models for the RAGPDF package."""

from typing import List, Optional, Union
from pydantic import BaseModel, Field, HttpUrl, field_validator


class BaseConfig(BaseModel):
    """Base configuration model."""
    model: str = Field(..., description="Model name to use")
    api_key: str = Field("", description="API key for authentication")
    api_base: Optional[str] = Field(None, description="Base URL for the API")

    @field_validator('api_base')
    @classmethod
    def validate_api_base(cls, v: Optional[str]) -> Optional[str]:
        """Validate api_base URL."""
        if v:
            # Only validate non-empty strings
            try:
                HttpUrl(v)
            except ValueError as e:
                raise ValueError(f"Invalid URL: {e}")
        return v


class EmbeddingConfig(BaseConfig):
    """Configuration for embedding model."""
    model: str = Field(..., description="Embedding model name (e.g., 'text-embedding-ada-002')")


class LLMConfig(BaseConfig):
    """Configuration for language model."""
    model: str = Field(..., description="LLM model name (e.g., 'gpt-3.5-turbo')")
    temperature: Optional[float] = Field(0.7, description="Temperature for response generation", ge=0, le=2)
    max_tokens: Optional[int] = Field(None, description="Maximum tokens in response", gt=0)


class DocumentChunk(BaseModel):
    """A chunk of text from a document with its source."""
    file: str
    content: str
    page: Optional[int] = None


class RAGContext(BaseModel):
    """Context information for RAG operations."""
    query: str
    chunks: List[DocumentChunk]
    files: List[str]
    total_chunks: int
    
    def to_string(self) -> str:
        """Convert the context to a readable string format."""
        chunks_str = "\n\n".join([
            f"From {chunk.file}" + (f" (page {chunk.page})" if chunk.page else "") + f":\n{chunk.content}"
            for chunk in self.chunks
        ])
        
        return (
            f"Query: {self.query}\n\n"
            f"Found {self.total_chunks} relevant chunks from {len(self.files)} files:\n"
            f"{', '.join(self.files)}\n\n"
            f"{chunks_str}"
        )
    
    def to_json(self) -> str:
        """Convert the context to a JSON string."""
        return self.model_dump_json(indent=2)
