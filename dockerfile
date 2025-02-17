# (4) Implementação Técnica: Containerizar aplicação
# Usa uma imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia e instala as dependências diretamente
RUN pip install --no-cache-dir fastapi uvicorn pandas pyarrow

# Copia todo o conteúdo do projeto para /app
COPY . /app

# Expõe a porta 8000 para o FastAPI
EXPOSE 8000

# Comando para iniciar o servidor uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
