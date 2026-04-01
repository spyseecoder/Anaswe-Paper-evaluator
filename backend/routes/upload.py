from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import os
from services.document_processor import DocumentProcessor
from services.db_service import DatabaseService

router = APIRouter(prefix="/api/upload", tags=["upload"])
db = DatabaseService()

ALLOWED_EXTENSIONS = {'.pdf', '.png', '.jpg', '.jpeg', '.gif', '.tiff'}


@router.post("/marking-scheme")
async def upload_marking_scheme(file: UploadFile = File(...)):
    """Upload marking scheme document"""
    try:
        if not any(file.filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS):
            raise HTTPException(status_code=400, detail="File type not supported")
        
        content = await file.read()
        file_ext = os.path.splitext(file.filename)[1].lower()
        
        if file_ext == '.pdf':
            text = DocumentProcessor.extract_text_from_pdf_bytes(content)
        else:
            from services.ocr_service import OCRService
            ocr = OCRService()
            text = ocr.extract_text_from_bytes(content)
        
        scheme_id = db.save_marking_scheme(file.filename, text)
        
        return {
            "status": "success",
            "scheme_id": scheme_id,
            "file_name": file.filename,
            "message": "Marking scheme uploaded successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/answer-scripts")
async def upload_answer_scripts(files: List[UploadFile] = File(...), scheme_id: str = None):
    """Upload multiple answer scripts"""
    try:
        if not scheme_id:
            raise HTTPException(status_code=400, detail="scheme_id is required")
        
        batch_id = db.create_batch(scheme_id, len(files))
        
        return {
            "status": "success",
            "batch_id": batch_id,
            "total_files": len(files),
            "message": "Answer scripts uploaded successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
