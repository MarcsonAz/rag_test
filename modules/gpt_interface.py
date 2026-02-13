import json
import yaml
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(dotenv_path="env/.env") 
#config = dotenv_values('env/.env')

print(os.getenv("MINHA_CHAVE_SECRETA"))

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)

with open("config/prompts.yaml", encoding="utf-8") as f:
    prompts = yaml.safe_load(f)

def extrair_parametros(pergunta):
    prompt = prompts["consulta_template"].format(input=pergunta)
    
    print('\n ------ \n')
    print("Prompt enviado para o modelo:")
    print(prompt)

    response = client.responses.create(
        model="gpt-3.5-turbo",
        input = prompt,
        max_output_tokens=150,
        temperature=0.2
    )

    response_dict = response.model_dump()
    try:
        output_list = response_dict.get("output", [])
        primeiro_output = output_list[0] # Pega o dicionário no índice 0
        
        content_list = primeiro_output.get("content", [])
        primeiro_content = content_list[0] # Pega o dicionário no índice 0
        
        texto = primeiro_content.get("text", "Texto não encontrado")

        usage = response_dict.get("usage", {})
    except (IndexError, KeyError, TypeError):
        texto = "Erro na estrutura dos dados"

    print('\n ------ \n')
    print(texto)

    with open("log/token_log.csv", "a", encoding="utf-8") as log:
        log.write(f'{pergunta},"{texto}",{usage["input_tokens"]},{usage["output_tokens"]},{usage["total_tokens"]}\n')

    return texto
    
    
    ## TypeError: the JSON object must be str, bytes or bytearray, not list


    #return json.loads(texto)
    #return json.dumps(texto)
