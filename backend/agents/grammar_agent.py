import sys
import os
import json
import re
from datetime import datetime
import threading # Necessário para rodar o salvamento e o servidor juntos
import time      # Pequena pausa entre geração da revisão e salvamento


current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(current_dir)
sys.path.append(backend_dir)
from scripts.prompt_manager import render_prompt

from agno.agent import Agent
from agno.models.google import Gemini
from agno.os import AgentOS
import uvicorn
from dotenv import load_dotenv

load_dotenv()

# Função de limpeza
def clean_json_string(raw_str: str):
    match = re.search(r"```json\s*([\s\S]*?)\s*```", raw_str, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_str.strip()

output_dir = os.path.join(backend_dir, "./reviews_outputs/reviews_grammaticals")

def load_tcc_text(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"⚠️ AVISO: Arquivo '{file_path}' não encontrado.")
        return "Texto do TCC não fornecido."
    
#Variável de chamada dos arquivos de texto
instructions_file = "../prompts/raw_prompts/v3/grammatical_correction_v3.txt"
input_text_file = "../data/processed_tccs/2025_tcc_aexoliveira.md"
texto_do_tcc = load_tcc_text(input_text_file)

dados_do_frontend = {
    "area_conhecimento_tcc": "Segurança da Informação",
    "secao_desejada": "Fundamentação Teórica",
    "titulo_tcc": "FORTALECENDO A PRIVACIDADE E SEGURANÇA EM VPN: EXPLORANDO BLOCKCHAIN E PROVA DE CONHECIMENTO ZERO COMO SOLUÇÃO",
    "nivel_rigor_modelo": "Rigoroso",
   #"informacoes_adicionais": "Não há informações adicionais",
    "texto_tcc": texto_do_tcc,
}

#Variável que passa o prompt + os dados do sistema necessários para o modelo analisar
system_prompt_final = render_prompt(instructions_file, dados_do_frontend)

print(" === PROMPT RENDERIZADO (PREVIEW) ===")
print(system_prompt_final[:100])
print("====================================")

logical_flow_agent = Agent(
    id="grammatical_correction_agentid",
    name="Agente de Correção Gramatical do ARAMIS",
    model=Gemini(id="gemini-2.5-pro"), # Definição do modelo
    markdown=True,
    instructions= system_prompt_final,
    reasoning= True,
)

# --- Lógica de salvamento ---
def run_and_save_review():
    """Esta função contém a lógica de execução e salvamento."""
    print("\n" + "="*50)
    print(f"🚀 INICIANDO REVISÃO COM {logical_flow_agent.model.id} (em background)")
    print("="*50 + "\n")
    os.makedirs(output_dir, exist_ok=True)
    try:
        # Executa o agente
        response = logical_flow_agent.run(
            "Analise o texto fornecido no contexto e gere o JSON de revisão.",
            stream=False
        )

        raw_content = response.content
        
        # O resto da lógica de salvamento
        json_content_str = clean_json_string(raw_content)
        json_data = json.loads(json_content_str)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"review_grammatical_correction{timestamp}.json"
        file_path = os.path.join(output_dir, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)
        print(f"\n✅ Sucesso! Revisão salva em:\n📂 {file_path}")
        
    except json.JSONDecodeError as e:
        print(f"\n❌ Erro ao decodificar JSON: {e}")
        print(f"Conteúdo recebido:\n{raw_content}")
    except Exception as e:
        print(f"\n❌ Erro inesperado durante a revisão: {e}")


# --- Servidor Agno ---
agent_os = AgentOS(agents=[logical_flow_agent])
app = agent_os.get_app()

if __name__ == "__main__":
    
    # Inicia a função de salvamento em paralelo para não ser bloqueada pelo servidor
    review_thread = threading.Thread(target=run_and_save_review)
    review_thread.start()
    time.sleep(1)

    # Inicia o servidor Uvicorn
    print(f"\n🚀 Servidor Agno iniciando na porta 8002...")
    uvicorn.run(app, host="0.0.0.0", port=8002)