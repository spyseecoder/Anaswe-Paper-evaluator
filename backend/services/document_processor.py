import pdfplumber
from pathlib import Path
from typing import List, Tuple
import io


class DocumentProcessor:
    @staticmethod
    def extract_text_from_pdf(pdf_path: str) -> str:
        """Extract text from PDF file"""
        try:
            text = []
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)
            return '\n\n'.join(text)
        except Exception as e:
            raise Exception(f"PDF Processing Error: {str(e)}")

    @staticmethod
    def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
        """Extract text from PDF bytes"""
        try:
            text = []
            with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)
            return '\n\n'.join(text)
        except Exception as e:
            raise Exception(f"PDF Processing Error: {str(e)}")

    @staticmethod
    def extract_pages_from_pdf(pdf_path: str) -> List[str]:
        """Extract text from each page separately"""
        try:
            pages = []
            with pdfplumber.open(pdf_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        pages.append(page_text)
            return pages
        except Exception as e:
            raise Exception(f"PDF Processing Error: {str(e)}")

    @staticmethod
    def get_file_type(file_path: str) -> str:
        """Get file extension"""
        return Path(file_path).suffix.lower()
