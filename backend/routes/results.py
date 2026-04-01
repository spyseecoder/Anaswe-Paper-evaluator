from fastapi import APIRouter, HTTPException
from services.db_service import DatabaseService

router = APIRouter(prefix="/api/results", tags=["results"])
db = DatabaseService()


@router.get("/batch/{batch_id}")
async def get_batch_results(batch_id: str):
    """Get evaluation results for a batch"""
    try:
        batch = db.get_batch(batch_id)
        if not batch:
            raise HTTPException(status_code=404, detail="Batch not found")
        
        # Serialize the batch document
        batch_data = db.serialize_doc(batch)
        
        return {
            "status": "success",
            "batch": batch_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/summary/{batch_id}")
async def get_batch_summary(batch_id: str):
    """Get summary statistics for a batch"""
    try:
        batch = db.get_batch(batch_id)
        if not batch:
            raise HTTPException(status_code=404, detail="Batch not found")
        
        return {
            "status": "success",
            "batch_id": batch.get("batch_id", batch_id),
            "total_scripts": batch.get("total_scripts", 0),
            "evaluated_scripts": batch.get("evaluated_scripts", 0),
            "evaluation_status": batch.get("status", "pending")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/evaluations/{batch_id}")
async def get_evaluations(batch_id: str):
    """Get all evaluations for a batch"""
    try:
        evaluations = list(db.evaluations.find({"batch_id": batch_id}))
        
        # Serialize documents
        eval_list = []
        for eval_doc in evaluations:
            eval_data = db.serialize_doc(eval_doc)
            eval_list.append(eval_data)
        
        return {
            "status": "success",
            "batch_id": batch_id,
            "evaluations": eval_list,
            "total_evaluations": len(eval_list)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
