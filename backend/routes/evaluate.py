from fastapi import APIRouter, HTTPException, BackgroundTasks
from services.db_service import DatabaseService
from services.evaluation_service import EvaluationService
from services.rag_service import RAGService
import asyncio
import json

router = APIRouter(prefix="/api/evaluate", tags=["evaluate"])
db = DatabaseService()
eval_service = EvaluationService()
rag_service = RAGService()


def perform_evaluation(batch_id: str, scheme_id: str):
    """Background task to perform evaluation"""
    try:
        batch = db.get_batch(batch_id)
        scheme = db.get_marking_scheme(scheme_id)
        
        if not batch or not scheme:
            db.update_batch_status(batch_id, "failed")
            return
        
        marking_scheme = scheme.get("content", "")
        
        # Simulate evaluation for demo
        # In production, would process actual uploaded papers
        for i in range(batch.get("total_scripts", 0)):
            try:
                # Demo evaluation result
                result = {
                    "score": 75 + (i * 2),  # Mock scores
                    "max_score": 100,
                    "percentage": (75 + (i * 2)),
                    "feedback": f"Paper {i+1} evaluation - Good understanding of concepts",
                    "confidence_score": 0.85
                }
                
                db.save_evaluation(batch_id, f"paper_{i+1}", result)
                
            except Exception as e:
                print(f"Error evaluating paper {i+1}: {str(e)}")
        
        db.update_batch_status(batch_id, "completed", batch.get("total_scripts", 0))
        
    except Exception as e:
        print(f"Evaluation Error: {str(e)}")
        db.update_batch_status(batch_id, "failed")


@router.post("/start")
async def start_evaluation(batch_id: str, scheme_id: str, background_tasks: BackgroundTasks):
    """Start evaluation for a batch"""
    try:
        batch = db.get_batch(batch_id)
        if not batch:
            raise HTTPException(status_code=404, detail="Batch not found")
        
        db.update_batch_status(batch_id, "processing")
        
        # Add background task to perform evaluation
        background_tasks.add_task(perform_evaluation, batch_id, scheme_id)
        
        return {
            "status": "success",
            "batch_id": batch_id,
            "message": "Evaluation started in background",
            "total_scripts": batch.get("total_scripts", 0)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
