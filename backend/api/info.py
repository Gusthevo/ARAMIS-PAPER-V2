from fastapi import APIRouter
from datetime import datetime
import os

router = APIRouter()

@router.get("/about")
async def about():
    """Retorna informações sobre a plataforma em formato JSON"""
    current_year = datetime.now().year
    version = os.getenv("APP_VERSION", "1.0.0")
    
    return {
        "platform": {
            "name": "ARAMIS",
            "full_name": "Automated Review Agents for Methodological Improvements",
            "version": version,
            "description": "Sistema de Análise e Revisão Automatizada de TCCs de alunos de graduação",
            "purpose": "Auxiliar estudantes de graduação na melhoria dos textos acadêmicos",
            "year": current_year
        },
        "features": [
            {
                "name": "Correção Gramatical",
                "description": "Análise de ortografia, gramática e pontuação",
                "icon": "📝"
            },
            {
                "name": "Encadeamento Lógico", 
                "description": "Verificação de coerência e coesão textual",
                "icon": "🔗"
            },
            {
                "name": "Rigor Metodológico",
                "description": "Análise da estrutura acadêmica e metodologia",
                "icon": "📊"
            }
        ],
        "technology_stack": {
            "backend": ["FastAPI", "Python", "MySQL"],
            "frontend": ["Streamlit"],
            "infrastructure": ["Docker", "Docker Compose"],
            "ai_components": ["LLMs", "NLP", "Marker PDF"]
        },
        "target_audience": [
            "Estudantes de graduação",
            "Pesquisadores"
        ],
        "statistics": {
            "active_agents": 3,
            "supported_languages": ["Português"],
            "availability": "24/7"
        },
        "development": {
            "project_type": "Trabalho de Conclusão de Curso (TCC)",
            "status": "Em desenvolvimento",
            "repository": "Privado"
        }
    }