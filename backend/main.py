from fastapi import FastAPI
from api import info, change_informations, auth, analysis

app = FastAPI(
    title="ARAMIS API",
    description="Sistema inteligente de correção de TCCs com múltiplos agentes especializados",
    version="1.0.0"
)

# Inclua as rotas
app.include_router(auth.router, prefix="/api/auth")
app.include_router(change_informations.router, prefix="/api/change")
app.include_router(info.router, prefix= "/api/info")  
app.include_router(analysis.router, prefix= "/api/analysis")

@app.get("/")
async def root():
    return {
        "message": "ARAMIS API - Sistema de Correção de TCCs",
        "version": "1.0.0", 
        "endpoints": {
            "documentation": "/docs",
            "about": "/about",
            "health": "/health",
            "auth": "/api/auth",
            "change_informations": "/api/change_informations"
        }
    }

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ARAMIS Backend", 
        "timestamp": "2024-01-15T10:30:00Z"
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