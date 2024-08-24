# Usar uma imagem base do Python
FROM python:3.11

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de requisitos para o diretório de trabalho
COPY ./requirements.txt ./requirements.txt

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da API para o diretório de trabalho
COPY ./src ./src

# Expor a porta em que o Django será executado
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]