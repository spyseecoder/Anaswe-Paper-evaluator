import easyocr
from PIL import Image
import io
from pathlib import Path
from typing import List, Tuple


class OCRService:
    def __init__(self, languages: List[str] = None):
        self.languages = languages or ["en"]
        self.reader = easyocr.Reader(self.languages)

    def extract_text_from_image(self, image_path: str) -> str:
        """Extract text from image file using EasyOCR"""
        try:
            result = self.reader.readtext(image_path, detail=0)
            text = '\n'.join(result)
            return text
        except Exception as e:
            raise Exception(f"OCR Error: {str(e)}")

    def extract_text_from_bytes(self, image_bytes: bytes) -> str:
        """Extract text from image bytes"""
        try:
            image = Image.open(io.BytesIO(image_bytes))
            temp_path = "/tmp/temp_ocr.png"
            image.save(temp_path)
            text = self.extract_text_from_image(temp_path)
            Path(temp_path).unlink()
            return text
        except Exception as e:
            raise Exception(f"OCR Error: {str(e)}")

    def extract_text_from_multiple_images(self, image_paths: List[str]) -> str:
        """Extract text from multiple images"""
        all_text = []
        for path in image_paths:
            try:
                text = self.extract_text_from_image(path)
                all_text.append(text)
            except Exception as e:
                print(f"Warning: Could not process {path}: {str(e)}")
        return '\n\n'.join(all_text)
