# Usar uma imagem oficial do Python como base
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Definir variáveis de ambiente
# Previne que o Python gere arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Garante que a saída do console seja exibida imediatamente
ENV PYTHONUNBUFFERED 1

# Instalar dependências do sistema necessárias para o Pillow e outras libs
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar as dependências do projeto
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código do projeto para o container
COPY . /app/

# Coletar arquivos estáticos (se necessário, descomente se usar WhiteNoise)
# RUN python manage.py collectstatic --noinput

# Expor a porta que o Django utiliza
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
