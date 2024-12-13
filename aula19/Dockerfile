# Dockerfile

# Imagem base
FROM python:3.12

# instalando poetry
RUN pip install poetry

# copiar conteúdo do diretório atual para o container
COPY . /src

# Definir o diretório de trabalho no container
WORKDIR /app

# instalar dependencias com poetry
RUN poetry install

# expor a porta que a aplicação estará escutando
EXPOSE 8501

# definir entrypoint para executar servidor uvicorn
ENTRYPOINT [ "poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8501"]