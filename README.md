# rag_test
Teste para a produção de um RAG para o Léo Mello

26/07 - inicio, carregando arquivos, montando estrutura
27/07 - primeiros testes com a API da IA
22/09 - aplica contexto com a api da open ai, e pega colunas selecionadas, aplica o filtro na tabela e o retorno é tratado para texto.
22/09 - consulta simples de tamanho da população de municípios de acordo com dados do IBGE de 2024.
22/09 - encerramenro do produção de serviço

## para rodar

1. abrir o terminal e carregar o ambiente - ./rag_test/.venv/Scripts/Activate.ps1

2. rodar no terminal: python app.py

Se funcionar: Running on http://127.0.0.1:5000

## Serviço

Coloque o nome de um município do Brasil em texto, e ele irá retornar o tamanho da população estimada pelo IBGE em 2024.

O sistema é um teste de rag de dados estruturados.

Processo: 

1. com o serviço ativo, na home page, pedir o tamananho da população de um município.

2. por trás, é preparado um prompt com a pergunta e um contexto que detalha o tipo de tabela e pede uma query sql de retorno.

3. é enviado o prompt para api da open ai e aplicado no modelo gpt-3.5-turbo (serviço pago, mas é bem barato, detalhes no fim)

3. é carregado o dataframe em memória

4. a query sql retornado do llm é aplicada com o pandas nos dados

5. com o filtro aplicado, a linha de retorno da tabela passa por um template de resposta


### O serviço está encerrado, pois foi concluído o propósito inicial de testes

## Pode ser feito

Retorno de informações para mais de um município.

## Custos

Nos testes, com mais de 3 mil tokesn usados, o consumo foi de menos de um centavo de dólar.

25 requests
3.05K input tokens

- https://platform.openai.com/docs/overview
