import os
import json
import re
import time
from scripts.prompt_manager import render_prompt
from agno.agent import Agent
#from agno.models.openai import OpenAIChat
from agno.models.huggingface import HuggingFace
#from agno.models.google import Gemini
from dotenv import load_dotenv

load_dotenv()

def clean_json_string(raw_str: str):
    match = re.search(r"```json\s*([\s\S]*?)\s*```", raw_str, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_str.strip()


class GrammarCorrectionAgent:

    def __init__(self):
        self.instructions_file = os.path.join(
            os.path.dirname(__file__),
            "../prompts/raw_prompts/v3/grammatical_correction_v3.txt"
        )

        self.model = HuggingFace(
            id="openai/gpt-oss-20b",
            #max_tokens = 65536,
            #base_url=os.getenv("GROQ_BASE_URL"),
            api_key=os.getenv("HUGGINGFACE_API_KEY"),

            #api_key= os.getenv("OPENAI_API_KEY")
        )

    async def analyze(self, text: str, context: dict) -> dict:
        """
        Método chamado pela orquestração.
        Gera o prompt final, executa o agente e retorna JSON limpinho.
        """
        #start_time = time.monotonic()

        # 1. Renderiza o prompt baseado nos dados do frontend
        instructions = render_prompt(self.instructions_file, {
            "area_conhecimento_tcc": context["area_knowledge"],
            "secao_desejada": context["section"],
            "titulo_tcc": context["title_tcc"],
            "nivel_rigor_modelo": context["model_rigor"],
            "texto_tcc": text
        })

        agent = Agent(
            id="grammar_agent",
            name="Agente de Correção Gramatical",
            model=self.model,
            system_message_role="user",
            markdown=True,
            instructions=instructions
        )

        # 2. Roda o agente
        response = agent.run("Analise o texto fornecido no contexto e gere o JSON de revisão.", stream=False)
        raw_content = response.content
        json_cleaned = clean_json_string(raw_content)

        result = json.loads(json_cleaned)

        #end_time = time.monotonic()
        #duration = end_time - start_time
        
        # 3. Normaliza a resposta para o formato esperado pelo orquestrador
        return {
            "corrections": result,
        }


# Instância única exportada
agent_os_grammar = GrammarCorrectionAgent()
