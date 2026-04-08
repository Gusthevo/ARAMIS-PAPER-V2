from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import info, change_informations, auth, analysis
import logging
import sys

# Configuração global do logger
logging.basicConfig(
    level=logging.INFO,  # nível mínimo que será exibido
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]  # manda para stdout (terminal)
)


app = FastAPI(
    title="ARAMIS API",
    description="Smart System for Paper Correction With A Specialized Agent",
    version="2.0.0"
)

# 🔥 CONFIGURAÇÃO CORS COMPLETA PARA CONTAINERS DIFERENTES
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8501",      # Frontend local
        "http://127.0.0.1:8501",      # Frontend local alternativo  
        "http://frontend:8501",       # Frontend no container Docker
        "http://localhost:3000",      # Caso tenha outro frontend
    ],
    allow_credentials=True,           # 🔥 IMPORTANTE para cookies/sessões
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],              # Permite todos os headers
)

# Inclua as rotas
app.include_router(auth.router, prefix="/api/auth")
app.include_router(change_informations.router, prefix="/api/change")
app.include_router(info.router, prefix="/api/info")  
app.include_router(analysis.router, prefix="/api/analysis")

@app.get("/")
async def root():
    return {
        "message": "ARAMIS API - Paper Correction System",
        "version": "2.0.0", 
        "endpoints": {
            "documentation": "/docs",
            "about": "/about",
            "health": "/health",
            "auth": "/api/auth",
            "change_informations": "/api/change"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ARAMIS Backend", 
        "timestamp": "2024-01-15T10:30:00Z"
    }

@app.get("/about")
async def about():
    return {
        "platform": {
            "name": "ARAMIS",
            "description": "Automated Review Agents for Methodological Improvements",
            "version": "2.0.0"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="debug"
    )