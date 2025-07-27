import pandas as pd

def carregar_dados():
    return pd.read_csv("data/populacao.csv")

def consultar(dados, parametros):
    return dados  # Aqui você poderá customizar por tipo/ano/etc.
