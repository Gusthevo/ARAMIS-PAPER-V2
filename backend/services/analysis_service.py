import logging
from typing import List, Dict
from agents.grammar_agent import agent_os_grammar
from agents.logical_flow import agent_os_flow
from agents.methodological_rigor import agent_os_rigor
from models.analysis_model import AnalysisRequest, AnalysisResponse

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        self.agents = {
            "grammar_correction": agent_os_grammar,
            "logical_flow": agent_os_flow,
            "methodological_rigor": agent_os_rigor
        }
    
    async def analyze_text(self, request: AnalysisRequest) -> AnalysisResponse:
        logger.info(f"Analisando texto para seção: {request.section}")
        
        # Contexto com todas as informações do usuário
        context = {
            "section": request.section,
            "title_tcc": request.title,
            "area_knowledge": request.area,
            #"course_name": request.course,
            "model_rigor": request.rigor
        }
        
        # Coleta resultados dos agentes selecionados
        all_corrections = []
        all_suggestions = []
        confidences = []
        
        # ✅ CORREÇÃO: Usar request.agents (lista de strings) em vez de criar dict
        for agent_name in request.agents:
            if agent_name in self.agents:
                agent = self.agents[agent_name]
                result = await agent.analyze(request.text, context)
                
                all_corrections.extend(result.get("corrections", []))
                all_suggestions.extend(result.get("suggestions", []))
                confidences.append(result.get("confidence", 0.5))
        
        # Calcula score médio
        avg_confidence = sum(confidences) / len(confidences) if confidences else 0.5
        
        return AnalysisResponse(
            analysis_id=f"analysis_{len(request.text)}",
            original_text=request.text[:100] + "..." if len(request.text) > 100 else request.text,
            section=request.section,
            corrections=all_corrections,
            suggestions=all_suggestions,
            score=avg_confidence,
            summary=f"Análise da {request.section} com {len(request.agents)} agentes"
        )

# Instância global
analysis_service = AnalysisService()