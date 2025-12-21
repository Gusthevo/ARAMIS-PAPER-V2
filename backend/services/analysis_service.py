import logging
import time
from typing import List, Dict
from agents.grammar_agent import agent_os_grammar
from agents.logical_agent import agent_os_logical
from agents.rigor_agent import agent_os_rigor
from core.connection import get_db
from models.analysis_model import AnalysisRequest, AnalysisResponse
import json

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        self.agents = {
            "grammar_correction": agent_os_grammar,
            "logical_flow": agent_os_logical,
            "methodological_rigor": agent_os_rigor
        }
    
    async def analyze_text(self, request: AnalysisRequest) -> AnalysisResponse:
        start_time = time.monotonic()
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
        
        # ✅ CORREÇÃO: Usar request.agents (lista de strings) em vez de criar dict
        for agent_name in request.agents:
            if agent_name in self.agents:
                agent = self.agents[agent_name]
                result = await agent.analyze(request.text, context)
                correction = result.get("corrections")
            if correction:
                all_corrections.append(correction)
        
        end_time = time.monotonic()
        duration = end_time - start_time

        connection = get_db() 
        cursor = connection.cursor(dictionary=True)

        try:
            # Insere a correção no banco de dados
            cursor.execute(
                "INSERT INTO corrections (user_id, correction, analysis_time) VALUES (%s, %s, %s)",
                (request.user_id, json.dumps(all_corrections),duration)
            )
            connection.commit()
        except Exception as e:
            logger.error(f"Erro ao salvar correção no banco de dados: {e}")
        finally:
            cursor.close()
            connection.close()

        return AnalysisResponse(
            analysis_id=f"analysis_{len(request.text)}",
            original_text=request.text[:100] + "..." if len(request.text) > 100 else request.text,
            section=request.section,
            correction=all_corrections,
        )

# Instância global
analysis_service = AnalysisService()