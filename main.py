from fastapi import FastAPI
import uvicorn
import pandas as pd
from pathlib import Path

"""
====================================================
GreenFlow - API de Insights Sustentáveis
====================================================

Este ficheiro implementa a solução para o desafio descrito no PDF.
Cada parte do código faz referência às secções do exercício:

1. Explorar os Dados
2. Descobrir e Criar Insights
3. Desenvolver uma Solução para Compartilhar os Insights
4. Implementação Técnica

"""

# (3) Desenvolver uma Solução para Compartilhar os Insights:
# Aqui criamos uma instância do FastAPI para disponibilizar os dados via endpoints.
app = FastAPI(title="GreenFlow - API de Insights Sustentáveis")

@app.get("/")
def read_root():
    """
    Rota raiz para verificar se a API está funcional.
    Retorna uma mensagem simples de boas-vindas.
    """
    return {"message": "Bem-vindo à API GreenFlow! Aceda a /docs para a documentação da API. Aceda a /insights para visualizar os resultados da análise."}


def load_and_process_data():
    """
    (1) Explorar os Dados:
    - Carrega o ficheiro Parquet usando um caminho relativo.
    - Imprime as colunas disponíveis para confirmar a estrutura.

    (2) Descobrir e Criar Insights:
    - Limpa dados ausentes.
    - Agrega métricas (energia_kwh, agua_m3, co2_emissoes) por setor.
    - Identifica a empresa com maior consumo em cada métrica, se disponível.
    """
    # Caminho base relativo ao ficheiro atual
    base_dir = Path(__file__).parent
    data_file = base_dir / "data" / "dados_sensores_5000.parquet"

    # (1) Carrega o dataset num DataFrame
    df = pd.read_parquet(data_file)

    # (1) Explorar os Dados - Verificar as colunas do dataset
    print("\n--- Colunas Disponíveis no Dataset ---")
    print(df.columns)

    # (2) Descobrir e Criar Insights - Remover linhas com dados ausentes
    df_clean = df.dropna()

    # (2) Descobrir e Criar Insights - Agregar métricas por setor
    insights_by_setor = df_clean.groupby("setor").agg({
        "energia_kwh": "sum",
        "agua_m3": "sum",
        "co2_emissoes": "sum"
    }).reset_index()

    # (2) Descobrir e Criar Insights - Se existir coluna 'empresa', calcular o maior consumo
    top_consumption = None
    if "empresa" in df_clean.columns:
        top_consumption = {
            metric: df_clean.groupby("empresa")[metric].sum().idxmax()
            for metric in ["energia_kwh", "agua_m3", "co2_emissoes"]
        }

    return insights_by_setor, top_consumption


# (2) Descobrir e Criar Insights - Carregamos e processamos os dados na inicialização
insights_by_setor, top_consumption = load_and_process_data()

@app.get("/insights")
def get_insights():
    """
    (3) Desenvolver uma Solução para Compartilhar os Insights:
    Endpoint que retorna os insights agregados por 'setor' e o maior consumo, se houver.

    Retorna:
    - insights_by_setor: lista de dicionários com consumo total por setor.
    - top_consumption: dicionário com a empresa de maior consumo para cada métrica (se disponível).
    """
    # Converter o DataFrame para uma lista de dicionários
    setor_data = insights_by_setor.to_dict(orient="records")
    return {"insights_by_setor": setor_data, "top_consumption": top_consumption}


if __name__ == "__main__":
    """
    (4) Implementação Técnica:
    - Executar a aplicação FastAPI usando uvicorn
    - Parâmetro reload=True para facilitar desenvolvimento
    """
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
