import json
import yaml
import os
from openai import OpenAI
#from dotenv import dotenv_values

#config = dotenv_values('.env')

client = OpenAI(
    # This is the default and can be omitted
    #api_key=os.environ.get("OPENAI_API_KEY"),
)

with open("config/prompts.yaml", encoding="utf-8") as f:
    prompts = yaml.safe_load(f)

def extrair_parametros(pergunta):
    prompt = prompts["consulta_template"].format(input=pergunta)
    response = client.responses.create(
        model="gpt-3.5-turbo",
        #input = prompt,

        input="Return a simple and random  JSON with 2 key values. place, placename and value,value in integer.",
        max_output_tokens=150,
        temperature=0.2
    )

    response_dict = response.model_dump()

    print(response_dict)
    texto = response_dict["output"]
    #texto = response_dict.output_text
    usage = response_dict["usage"]

    print(texto)

    with open("log/token_log.csv", "a", encoding="utf-8") as log:
        log.write(f'{pergunta},"{texto}",{usage["input_tokens"]},{usage["output_tokens"]},{usage["total_tokens"]}\n')
    ## TypeError: the JSON object must be str, bytes or bytearray, not list
    return json.loads(texto)
    #return json.dumps(texto)
