GreenFlow - API de Insights Sustentáveis

Este projeto é uma solução para o desafio descrito no PDF Startup Data Challenge – Insights Sustentáveis com Parquet.A aplicação carrega dados de sensores a partir de um ficheiro Parquet e fornece insights agregados por meio de uma API construída com FastAPI.

Índice

Visão Geral do Projeto

Estrutura de Pastas

Pré-Requisitos

Instalação e Execução (Local)

Execução com Docker

Endpoints Disponíveis

Referência às Secções do PDF

Observações

Visão Geral do Projeto

Objetivo: Transformar dados brutos de sensores ambientais em insights de sustentabilidade.

Principais Métricas:

energia_kwh

agua_m3

co2_emissoes

Estrutura de Pastas

├── data/
│   └── dados_sensores_5000.parquet
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md

data/ contém o ficheiro de dados (.parquet).

main.py é o script principal FastAPI.

Dockerfile para containerizar a aplicação.

requirements.txt lista de dependências (caso queira instalar via pip install -r requirements.txt).

README.md este ficheiro.

Pré-Requisitos

Python 3.9+ instalado localmente

pip (gestor de pacotes do Python)

(Opcional) Docker caso deseje executar via container

Instalação e Execução (Local)

Clonar o repositório:

git clone https://github.com/seu-usuario/greenflow-challenge.git
cd greenflow-challenge

Criar e ativar ambiente virtual (opcional mas recomendado):

python -m venv venv
venv\Scripts\activate  (Windows)
# source venv/bin/activate (macOS/Linux)

Instalar dependências:

pip install -r requirements.txt

Se preferir, use diretamente pip install fastapi uvicorn pandas pyarrow.

Executar a aplicação:

uvicorn main:app --reload

A API estará disponível em http://127.0.0.1:8000.

Testar endpoints:

Root file: http://127.0.0.1:8000/

Documentação interativa: http://127.0.0.1:8000/docs

Insights: http://127.0.0.1:8000/insights

Execução com Docker

Instale o Docker se ainda não tiver.

Construa a imagem:

docker build -t greenflow-api .

Execute o container:

docker run -p 8000:8000 greenflow-api

Aceda à API:

http://127.0.0.1:8000
http://127.0.0.1:8000/docs

Endpoints Disponíveis

GET /
Mensagem de boas-vindas e instrução de uso.

GET /insights
Retorna as métricas agregadas por setor e a empresa de maior consumo por métrica, caso a coluna empresa exista.

Referência às Secções do PDF

(1) Explorar os DadosNo main.py, a função load_and_process_data() carrega o Parquet, imprime as colunas e remove dados ausentes.
(2) Descobrir e Criar InsightsAinda em load_and_process_data(), o código agrega as métricas (energia_kwh, agua_m3, co2_emissoes) por setor e identifica a empresa com maior consumo, se disponível.
(3) Desenvolver uma Solução para Compartilhar os InsightsO FastAPI expõe dois endpoints ("/" e "/insights") para que os usuários possam consumir os dados processados.
(4) Implementação TécnicaInclui o uso de uvicorn para executar a aplicação, bem como a containerização via Docker para fácil distribuição.

Observações

Caso o ficheiro .parquet tenha colunas diferentes das previstas (energia_kwh, agua_m3, co2_emissoes), ajuste o código para refletir a nomenclatura correta.

Se desejar ignorar o ficheiro de dados grande no Git, adicione data/ ao seu .gitignore.

Para dúvidas adicionais, consulte a documentação oficial do FastAPI e do Pandas.

Divirta-se explorando os dados e construindo insights sustentáveis!

