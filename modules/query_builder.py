def construir_filtro(dados, parametros):
    municipios = parametros.get("municipios", [])
    if municipios:
        dados_filtrados = dados[dados["municipio"].str.lower().isin([m.lower() for m in municipios])]
        return dados_filtrados
    return dados
