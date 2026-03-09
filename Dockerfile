# Versão do Python do container
FROM python:3.12-slim  
# Diretório de trabalho dentro do container
WORKDIR /sge
# Variáveis de ambiente para logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Copia os arquivos do host para o container
COPY . .
# Atualiza o PIP
RUN pip install --upgrade pip
# Instala as dependências do requirements 
RUN pip install -r requirements.txt
# Expoe a porta 8000 dentro do container
EXPOSE 8000
# Executa o sistema na porta 8000 dentro do container
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000