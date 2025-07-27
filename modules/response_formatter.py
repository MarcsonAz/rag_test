import json

with open("config/messages.json", encoding="utf-8") as f:
    mensagens = json.load(f)

def formatar_resposta(resultados):
    if resultados.empty:
        return mensagens["no_result"]
    linhas = []
    for _, row in resultados.iterrows():
        linhas.append(f'{row["nome_municipio"]}: {row["populacao"]}')
    return "<br>".join(linhas)
