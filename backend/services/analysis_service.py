import logging
from typing import List, Dict
from agents.grammar_agent import agent_os_grammar
from agents.logical_agent import agent_os_logical
from agents.rigor_agent import agent_os_rigor
from models.analysis_model import AnalysisRequest, AnalysisResponse

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        self.agents = {
            "grammar_correction": agent_os_grammar,
            "logical_flow": agent_os_logical,
            "methodological_rigor": agent_os_rigor
        }
    
    async def analyze_text(self, request: AnalysisRequest) -> AnalysisResponse:
        logger.info(f"Analisando texto para seção: {request.section}")
        
        # Contexto com todas as informações do usuário
        context = {
            "section": request.section,
            "title_tcc": request.title,
            "area_knowledge": request.area,
            "model_rigor": request.rigor
        }
        
        # Coleta resultados dos agentes selecionados
        all_corrections = []
        
        # ✅ CORREÇÃO: Usar request.agents (lista de strings) em vez de criar dict
        for agent_name in request.agents:
            if agent_name in self.agents:
                agent = self.agents[agent_name]
                result = await agent.analyze(request.text, context)
                correction = result.get("corrections")
            if correction:
                all_corrections.append(correction)

        return AnalysisResponse(
            analysis_id=f"analysis_{len(request.text)}",
            original_text=request.text[:100] + "..." if len(request.text) > 100 else request.text,
            section=request.section,
            correction=all_corrections,
        )

# Instância global
analysis_service = AnalysisService()