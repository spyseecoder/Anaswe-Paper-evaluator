from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class MarkingScheme(BaseModel):
    file_name: str
    content: str
    embeddings: Optional[List[float]] = None


class AnswerScript(BaseModel):
    file_name: str
    content: str
    page_number: Optional[int] = None


class EvaluationRequest(BaseModel):
    marking_scheme_id: str
    answer_scripts: List[AnswerScript]


class EvaluationResult(BaseModel):
    script_name: str
    score: float
    max_score: float
    percentage: float
    feedback: str
    evaluation_details: dict = {}
    confidence_score: float


class EvaluationBatch(BaseModel):
    batch_id: str
    marking_scheme_id: str
    total_scripts: int
    evaluated_scripts: int
    results: List[EvaluationResult] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = "pending"  # pending, processing, completed, failed
