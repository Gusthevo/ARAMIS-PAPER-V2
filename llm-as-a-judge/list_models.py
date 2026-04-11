import openai
from dotenv import load_dotenv
import os
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# openai.api_key = "SUA_CHAVE_AQUI"

models = openai.models.list()
for model in models.data:
    print(model.id)
