import sys
import os
import json
import re
from datetime import datetime
from zoneinfo import ZoneInfo
import threading # Necessário para rodar o salvamento e o servidor juntos
import time      # Pequena pausa entre geração da revisão e salvamento


current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(current_dir)
sys.path.append(backend_dir)
from scripts.prompt_manager import render_prompt

from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.openai import OpenAIChat
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

#Diretório de salvamento das revisões geradas
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
input_text_file = "../data/processed_tccs/2025_tcc_rmmelo.md"
texto_do_tcc = load_tcc_text(input_text_file)

dados_do_frontend = {
    "area_conhecimento_tcc": "Internet das Coisas",
    "secao_desejada": "Fundamentação Teórica",
    "titulo_tcc": "SISTEMA DE MONITORAMENTO DE ABELHAS APIS MELLIFERA",
    "nivel_rigor_modelo": "Rigoroso",
   #"informacoes_adicionais": "Não há informações adicionais",
    "texto_tcc": texto_do_tcc,
}

#Variável que passa o prompt + os dados do sistema necessários para o modelo analisar
system_prompt_final = render_prompt(instructions_file, dados_do_frontend)

print(" === PROMPT RENDERIZADO (PREVIEW) ===")
print(system_prompt_final[:100])
print("====================================")

grammatical_corrector_agent = Agent(
    id="grammatical_correction_agentid",
    name="Agente de Correção Gramatical do ARAMIS",
    model=OpenAIChat(id="gpt-4o-mini"), # Definição do modelo
    markdown=True,
    instructions= system_prompt_final,
    reasoning= True,
)

# --- Lógica de salvamento ---
def run_and_save_review():
    """Esta função contém a lógica de execução e salvamento."""
    print("\n" + "="*50)
    print(f"🚀 INICIANDO REVISÃO GRAMATICAL COM {grammatical_corrector_agent.model.id} (em background)")
    print(f"📄 Arquivo de Entrada: {input_text_file}")
    print("="*50 + "\n")
    os.makedirs(output_dir, exist_ok=True)
    try:
        start_time = time.monotonic()
        
        print("⏳ Gerando revisão gramatical...")
        response = grammatical_corrector_agent.run(
            "Analise o texto fornecido no contexto e gere o JSON de revisão.",
            stream=False
        )

        end_time = time.monotonic()
        duration = end_time - start_time
        print(f"⏱️ Tempo de Geração: {duration:.2f} segundos")

        raw_content = response.content
        json_content_str = clean_json_string(raw_content)
        
        # O JSON que o Gemini retornou
        resultado_revisao = json.loads(json_content_str)
        

        # 1. Cria o dicionário completo com os metadados
        json_final_completo = {
            "metadados_da_revisao": {
                "arquivo_fonte_tcc": os.path.basename(input_text_file),
                "titulo_tcc": dados_do_frontend.get("titulo_tcc"),
                "agente_utilizado": grammatical_corrector_agent.name, # Pega o nome do agente
                "modelo_llm": grammatical_corrector_agent.model.id,   # Pega o ID do modelo
                "prompt_utilizado": instructions_file,
                "nivel_rigor": dados_do_frontend.get("nivel_rigor_modelo"),
                "data_revisao_utc": datetime.now(ZoneInfo("America/Sao_Paulo")).isoformat(),
                "tempo_de_geracao_segundos": round(duration, 2)
            },
            "resultado_da_revisao": resultado_revisao # Aninha o resultado do LLM aqui
        }

        # 2. Cria o nome do arquivo mais descritivo
        tcc_filename_base = os.path.splitext(os.path.basename(input_text_file))[0]
        rigor_level = dados_do_frontend.get("nivel_rigor_modelo", "NivelNaoDefinido")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Adapta o nome para o agente gramatical
        filename = f"review_gramatical_{tcc_filename_base}_{rigor_level}_{timestamp}.json"
        file_path = os.path.join(output_dir, filename)

        # 3. Salva o JSON final e completo
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(json_final_completo, f, ensure_ascii=False, indent=4)
            
        print(f"\n✅ Sucesso! Revisão salva em:\n📂 {file_path}")
        
    except json.JSONDecodeError as e:
        print(f"\n❌ Erro ao decodificar JSON: {e}")
        print(f"Conteúdo recebido:\n{raw_content}")
    except Exception as e:
        print(f"\n❌ Erro inesperado durante a revisão: {e}")


# --- Servidor Agno ---
agent_os = AgentOS(agents=[grammatical_corrector_agent])
app = agent_os.get_app()

if __name__ == "__main__":
    
    # Inicia a função de salvamento em paralelo para não ser bloqueada pelo servidor
    review_thread = threading.Thread(target=run_and_save_review)
    review_thread.start()
    time.sleep(1)

    # Inicia o servidor Uvicorn
    print(f"\n🚀 Servidor Agno iniciando na porta 8002...")
    uvicorn.run(app, host="0.0.0.0", port=8002)