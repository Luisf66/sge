# Versão do Python do container
FROM python:3.11-slim  
# Diretório de trabalho dentro do container
WORKDIR /sge
# Copia os arquivos do host para o container
COPY . .
# Atualiza o PIP
RUN pip install --upgrade
# Instala as dependências do requirements 
RUN pip install -r requirements.txt
# Aplica as tabelas do banco
RUN python manage.py migrate
# Expoe a porta 8000 dentro do container
EXPOSE 8000
# Executa o sistema na porta 8000 dentro do container
RUN python manage.py runserver 0.0.0.0:8000