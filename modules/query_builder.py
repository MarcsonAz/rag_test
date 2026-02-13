""" def construir_filtro(dados, parametros):
    municipios = parametros.get("municipios", [])
    if municipios:
        dados_filtrados = dados[dados["municipio"].str.lower().isin([m.lower() for m in municipios])]
        return dados_filtrados
    return "Não palicado filtro com a consulta!" """

import json
import pandas as pd

def filtrar_por_retorno(df,retorno_list):
    """
    retorno_list: lista retornada pelo entedimento do LLM
    df: DataFrame original com os dados
    
    Retorna: DataFrame filtrado conforme os parâmetros extraídos do retorno_list
    """

    try:
        if not retorno_list or not isinstance(retorno_list, str):
            raise ValueError("Lista de retorno do LLM está vazia ou malformada.")
        
        # somente para 1 mensagem
        #texto_json = retorno_list[0]['content'][0]['text']
        print('\n ------------------M------------------------------ \n')

        print(retorno_list)
        filtros = json.loads(retorno_list)
        df_filtrado = df.copy()
        
        # Para cada chave vinda do LLM, ver se tem mapeamento para coluna no DF
        for chave_llm, valor in filtros.items():
            coluna_df = mapear_chave_llm_para_df(chave_llm)

            if coluna_df and coluna_df in df_filtrado.columns and valor:
                df_filtrado = df_filtrado[df_filtrado[coluna_df] == valor]
            

            #if coluna_df == 'sigla_uf':
             #   df_filtrado = df_filtrado[df_filtrado[coluna_df] == valor]
 
            if len(df_filtrado) == 1:
                    break
        
        return df_filtrado
    
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        print(f"Erro ao processar retorno: {e}")
        return pd.DataFrame()  # Retorna vazio no erro

# auxiliar.py
def mapear_chave_llm_para_df(chave_llm):
    """
    Recebe uma chave retornada pelo LLM e retorna o nome da coluna no DF.
    Caso não encontre, retorna None.
    """
    mapa = {
        "estado": "sigla_uf",
        "uf": "sigla_uf", 
        "municipio": "nome_municipio",
        "cidade": "nome_municipio",
        "codigo_municipio": "codigo_municipio",
        "cod_municipio": "codigo_municipio"
    }

    chave_llm_lower = chave_llm.lower().strip()
    return mapa.get(chave_llm_lower, None)
