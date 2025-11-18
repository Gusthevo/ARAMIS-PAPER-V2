from fastapi import APIRouter, HTTPException
import logging
from services.analysis_service import analysis_service
from models.analysis_model import AnalysisRequest, AnalysisResponse

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(request: AnalysisRequest):
    """
    Rota para análise de texto acadêmico com pré-configuração do usuário
    """
    try:
        # Validações
        if not request.text.strip():
            raise HTTPException(status_code=400, detail="Texto vazio")
        
        if len(request.text) < 25:
            raise HTTPException(status_code=400, detail="Texto muito curto (mínimo 25 caracteres)")
        
        if not request.agents:
            raise HTTPException(status_code=400, detail="Selecione pelo menos um agente")
        
        logger.info(f"Análise solicitada - Seção: {request.section}, Agentes: {request.agents}")
        
        return await analysis_service.analyze_text(request)
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro na análise: {str(e)}")
        raise HTTPException(status_code=500, detail="Erro interno")

@router.get("/sections")
async def get_sections():
    """Retorna seções disponíveis para análise"""
    return {
        "sections": [
            {"id": "introducao", "name": "Introdução", "description": "Apresentação do tema e objetivos"},
            {"id": "revisao_teorica", "name": "Revisão Teórica", "description": "Fundamentação teórica do trabalho"},
            {"id": "metodologia", "name": "Metodologia", "description": "Descrição dos métodos e procedimentos"},
            {"id": "resultados", "name": "Resultados", "description": "Apresentação dos dados e achados"},
            {"id": "discussao", "name": "Discussão", "description": "Análise e interpretação dos resultados"},
            {"id": "conclusao", "name": "Conclusão", "description": "Considerações finais e encaminhamentos"}
        ]
    }

@router.get("/agents")
async def get_agents():
    """Retorna agentes disponíveis para seleção"""
    return {
        "agents": [
            {
                "id": "grammar_correction",
                "name": "Correção Gramatical", 
                "description": "Analisa ortografia, gramática e pontuação"
            },
            {
                "id": "logical_flow", 
                "name": "Encadeamento Lógico",
                "description": "Verifica coerência e coesão textual"
            },
            {
                "id": "methodological_rigor",
                "name": "Rigor Metodológico",
                "description": "Analisa estrutura metodológica e acadêmica"
            }
        ]
    }

@router.get("/rigor-levels")
async def get_rigor_levels():
    """Retorna níveis de rigor disponíveis"""
    return {
        "rigor_levels": [
            {"id": "low", "name": "Baixo", "description": "Foco em problemas críticos"},
            {"id": "medium", "name": "Médio", "description": "Análise balanceada"},
            {"id": "high", "name": "Alto", "description": "Análise detalhada e rigorosa"}
        ]
    }