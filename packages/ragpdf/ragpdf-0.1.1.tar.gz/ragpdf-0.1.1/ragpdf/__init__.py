"""
RAGPDF - A package for retrieval-augmented generation using PDFs.

This package enables users to:
1. Add PDFs for retrieval-augmented generation (RAG)
2. Query the added PDFs using a provided prompt
3. Stream responses from the query
"""

from .ragpdf import RAGPDF

__version__ = "0.1.0"
__all__ = ["RAGPDF"]
