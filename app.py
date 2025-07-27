from flask import Flask, request, render_template
from modules.input_handler import limpar_entrada
from modules.gpt_interface import extrair_parametros
from modules.data_query import carregar_dados, consultar
from modules.query_builder import construir_filtro
from modules.response_formatter import formatar_resposta

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/consultar", methods=["POST"])
def consultar_populacao():
    pergunta = request.form["pergunta"]
    pergunta_limpo = limpar_entrada(pergunta)
    parametros = extrair_parametros(pergunta_limpo)
    #dados = carregar_dados()
    #dados_filtrados = construir_filtro(dados, parametros)
    #resposta = formatar_resposta(dados_filtrados)
    #return render_template("index.html", resposta=resposta)
    print(parametros)
    return render_template("index.html", resposta=parametros)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
