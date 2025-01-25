"""Module for handling PDF text extraction."""

import PyPDF2
from typing import List


class PDFProcessor:
    """Handles text extraction from PDFs."""

    @staticmethod
    def extract_text(pdf_path: str) -> List[str]:
        """
        Extract text from a PDF file.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            List[str]: List of text chunks from the PDF.

        Raises:
            FileNotFoundError: If the PDF file doesn't exist.
            PyPDF2.PdfReadError: If there's an error reading the PDF.
        """
        chunks = []
        try:
            with open(pdf_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                for page in pdf_reader.pages:
                    text = page.extract_text()
                    if text.strip():  # Only add non-empty chunks
                        # Split into smaller chunks if needed
                        chunks.extend([chunk.strip() for chunk in text.split('\n\n') if chunk.strip()])
            return chunks
        except FileNotFoundError:
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        except PyPDF2.PdfReadError as e:
            raise PyPDF2.PdfReadError(f"Error reading PDF {pdf_path}: {str(e)}")
