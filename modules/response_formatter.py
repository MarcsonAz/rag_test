import json

with open("config/messages.json", encoding="utf-8") as f:
    mensagens = json.load(f)

def formatar_resposta(resultados):
    if resultados.empty:
        return mensagens["no_result"]
    linhas = []
    for _, row in resultados.iterrows():
        populacao_formatada = f'{row["populacao"]:,}'.replace(',', '.')
        linhas.append(f'{row["nome_municipio"]}: {populacao_formatada}')
    return "<br>".join(linhas)