"""
Este módulo serve como ponto de entrada para a execução do sistema.

Ele importa e executa a função 'start' do módulo 'process_handle'.
"""

from src.main.process_handle import start
from db import db, Usuario

db.connect()
db.create_tables([Usuario])


if __name__ == "__main__":
    start()
