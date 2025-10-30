from pydantic import BaseModel
from typing import Optional, List

class AnalysisRequest(BaseModel):
    text: str
    section: str
    title: Optional[str] = None
    area_knowledge: Optional[str] = None  # ← Corrigido o nome
    course: Optional[str] = None
    rigor: str = "medium"
    agents: List[str] = []  # ← Lista dos agentes selecionados

class AnalysisResponse(BaseModel):
    analysis_id: str
    original_text: str
    section: str
    corrections: List[str]
    suggestions: List[str]
    score: float
    summary: str