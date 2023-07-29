# syntax=docker/dockerfile:1

# Use a imagem base do Python
FROM python:3.8-slim-buster

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório /app no contêiner
COPY requirements.txt requirements.txt

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o diretório src para o diretório /app/src no contêiner
COPY main.py .

# Expõe a porta 8000, que é a porta padrão do Uvicorn
EXPOSE 8000

# Comando para executar a aplicação usando o Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]