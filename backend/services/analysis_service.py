import logging
import time
from typing import List, Dict
from agents.iclr_agent import agent_os_iclr
from core.connection import get_db
from models.analysis_model import AnalysisRequest, AnalysisResponse

logger = logging.getLogger(__name__)

class AnalysisService:
    def __init__(self):
        self.agents = {
            "paper_correction": agent_os_iclr
        }
    
    async def analyze_text(self, request: AnalysisRequest) -> AnalysisResponse:
        start_time = time.monotonic()
        logger.info(f"Analisando texto para seção: {request.section}")
        
        # Contexto com todas as informações do usuário
        context = {
            #"section": request.section,
            "title_paper": request.title,
            "area_knowledge": request.area,
            #"model_rigor": request.rigor
        }
        
        # Coleta resultados dos agentes selecionados
        all_corrections = []
        
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
                "INSERT INTO corrections (user_id, title, section, correction, analysis_time) VALUES (%s, %s, %s, %s, %s)",
                (request.user_id, request.title, request.section, json.dumps(all_corrections), duration)
            )
            connection.commit()
        except Exception as e:
            logger.error(f"Erros saving correction in database: {e}")
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