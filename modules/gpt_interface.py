import os
import openai
from dotenv import load_dotenv
import json
import yaml

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

with open("config/prompts.yaml", encoding="utf-8") as f:
    prompts = yaml.safe_load(f)

def extrair_parametros(pergunta):
    prompt = prompts["consulta_template"].format(input=pergunta)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um extrator de parâmetros de consultas populacionais."},
            {"role": "user", "content": prompt}
        ]
    )
    texto = response["choices"][0]["message"]["content"]
    usage = response["usage"]
    with open("log/token_log.csv", "a", encoding="utf-8") as log:
        log.write(f'{pergunta},"{texto}",{usage["prompt_tokens"]},{usage["completion_tokens"]},{usage["total_tokens"]}\n')
    return json.loads(texto)
