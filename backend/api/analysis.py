from fastapi import APIRouter, HTTPException
import logging
from core.connection import get_db
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
            raise HTTPException(status_code=400, detail="Preencha o campo Texto para a analise")
        
        if len(request.text) < 25:
            raise HTTPException(status_code=400, detail="Texto muito curto (mínimo 25 caracteres)")
        
        if not request.agents:
            raise HTTPException(status_code=400, detail="Selecione pelo menos um agente")
        
        logger.info(f"Análise solicitada - Seção: {request.section}, Agentes: {request.agents}")
        
        result = await analysis_service.analyze_text(request)
        
        logger.info(f"Resultado da análise: {result}")
        
        return result

        
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
            {"id": "resumo", "name": "Resumo", "description": "Resumo Geral do Trabalho"},
            {"id": "introducao", "name": "Introdução", "description": "Apresentação do tema e objetivos"},
            {"id": "fundamentacao_teorica", "name": "Fundamentação Teórica/Estado da Arte", "description": "Fundamentação teórica do trabalho"},
            {"id": "trabalhos_relacionados", "name": "Trabalhos Relacionados", "description": "Trabalhos Relacionados do trabalho"},
            {"id": "metodologia", "name": "Metodologia", "description": "Descrição dos métodos e procedimentos"},
            {"id": "proposta", "name": "Proposta", "description": "Descrição da solução proposta no trabalho"},
            {"id": "resultados", "name": "Resultados", "description": "Apresentação dos dados e achados"},
            {"id": "conclusao", "name": "Conclusão", "description": "Considerações finais e encaminhamentos futuros"}
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
            {"id": "baixo", "name": "Baixo", "description": "Foco em problemas críticos"},
            {"id": "médio", "name": "Médio", "description": "Análise balanceada"},
            {"id": "alto", "name": "Alto", "description": "Análise detalhada e rigorosa"}
        ]
    }

@router.get("/corrections/{user_id}")
def get_user_corrections(user_id: int):
    connection = get_db()
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute(
            """
            SELECT 
                *
            FROM corrections
            WHERE user_id = %s
            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        results = cursor.fetchall()

        return {
            "user_id": user_id,
            "total": len(results),
            "corrections": results
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        cursor.close()
        connection.close()