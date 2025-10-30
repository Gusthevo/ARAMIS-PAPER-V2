from abc import ABC, abstractmethod
from typing import List, Dict

class BaseAgent(ABC):
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    async def analyze(self, text: str, context: Dict) -> Dict:
        pass
    
AGENTS_INFO = [
    {
        "name": "GrammarAgent",
        "path": "../agents/grammar_agent.py",
        "description": "Corrige erros gramaticais e sugere melhorias linguísticas.",
        "capabilities": ["Correção gramatical", "Sugestões de estilo", "Padronização de linguagem"]
    },
    {
        "name": "LogicalFlowAgent",
        "path": "../agents/logical_flow.py",
        "description": "Avalia a coerência e coesão lógica de textos.",
        "capabilities": ["Verificação de fluxo lógico", "Identificação de contradições", "Sugestões de reestruturação"]
    },
    {
        "name": "MethodologicalRigorAgent",
        "path": "../agents/methodological_rigor.py",
        "description": "Analisa a estrutura metodológica de textos acadêmicos.",
        "capabilities": ["Validação de metodologia", "Checagem de consistência", "Sugestões de aprimoramento"]
    }
]
