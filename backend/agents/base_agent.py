from agno.agent import Agent
from agno.models.google import Gemini
from agno.os import AgentOS
import uvicorn

#import google.generativeai as genai
#import os
from dotenv import load_dotenv

load_dotenv()


'''
# Certifique-se de que sua GOOGLE_API_KEY está configurada como variável de ambiente
try:
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
except KeyError:
    print("Chave de API do Google não encontrada. Por favor, configure a variável de ambiente GOOGLE_API_KEY.")
    exit()

print("Modelos do Gemini disponíveis para uso no Agno:")

for model in genai.list_models():
  # Filtra para mostrar os modelos mais comuns para geração de conteúdo
  if 'generateContent' in model.supported_generation_methods:
    # Imprime o nome que você usará na configuração do Agno
    print(f"- {model.name}")
'''

agent = Agent (
    name = "Agente Gentil",
    model = Gemini(id= "gemini-2.5-pro"),
    instructions= "Aja como um grande poeta brasileiro.",
    markdown= True,
)

#agent.print_response ("Conta uma piada do joãozinho", stream= True)


agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
