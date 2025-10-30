import mysql.connector
import os
import logging

'''
# Configurar o logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
'''

'''
# Adicionar handler para escrever logs em arquivo
file_handler = logging.FileHandler('server.log')
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
'''

def get_db():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST', 'mysql'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE'),
            port=3306
        )
        print("Conexão realizada com sucesso!")
        return connection
    except Exception as e:
        print("Erro ao conectar ao Bando de Dados.")
