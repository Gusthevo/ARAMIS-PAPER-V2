import os
from typing import Dict, Any

def render_prompt(file_path: str, context: Dict[str, Any]) -> str:
    """
    Lê um arquivo de template .txt e substitui os placeholders {{chave}}
    pelos valores fornecidos no dicionário 'context'.
    """
    try:
        if not os.path.exists(file_path):
            # Fallback ou erro se o arquivo não existir
            print(f"⚠️ AVISO: Arquivo de prompt '{file_path}' não encontrado.")
            return "Você é um assistente útil."

        with open(file_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
            print(f"Arquivo de prompt '{file_path}' lido e variáveis sendo preenchidas.")

        # Realiza a substituição das variáveis
        rendered_content = template_content
        for key, value in context.items():
            placeholder = "{{" + key + "}}"  # Ex: {{area_conhecimento_tcc}}
            # Garante que o valor seja string para evitar erros
            rendered_content = rendered_content.replace(placeholder, str(value))

        return rendered_content

    except Exception as e:
        print(f"❌ Erro ao renderizar prompt: {e}")
        return "Erro ao carregar instruções do agente."