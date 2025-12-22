from pydantic import BaseModel
from typing import Optional, List, Any

class AnalysisRequest(BaseModel):
    user_id: int
    text: str
    section: str
    title: Optional[str] = None
    area: Optional[str] = None  # ← Corrigido o nome
    course: Optional[str] = None
    rigor: str = "medium"
    agents: List[str] = []  # ← Lista dos agentes selecionados

class AnalysisResponse(BaseModel):
    analysis_id: str
    original_text: str
    section: str
    correction: Any 