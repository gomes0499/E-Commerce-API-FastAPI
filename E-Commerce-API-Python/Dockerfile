# Use uma imagem base oficial de Python
FROM python:3.9-slim

# Defina a variável de ambiente para garantir que a saída python seja enviada diretamente para o terminal sem buffer
ENV PYTHONUNBUFFERED 1

# Crie e defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copie o conteúdo do diretório atual para o contêiner
COPY . .

# Comando para executar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
