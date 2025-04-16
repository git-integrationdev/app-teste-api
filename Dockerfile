# Imagem base Python
FROM python:3.9-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Instala as dependências
RUN pip install flask

# Expõe a porta 5001 que é usada pelo Flask
EXPOSE 5001

# Comando para executar a aplicação
CMD ["python", "app.py"]