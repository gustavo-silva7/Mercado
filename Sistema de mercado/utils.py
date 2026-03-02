import os, re
from datetime import datetime

CLIENTES_FILE = "cliente.txt"
PRODUTOS_FILE = "produtos.txt"

'''Verifica se os arquivos .txt existem, se não, cria o arquivo'''
def arquivo_existe(nome_arquivo):
    if not os.path.exixte(nome_arquivo):
        open(nome_arquivo,'w').close()

'''Valida E-mail'''
def valida_email(email):
    return '@' in email and '.' in email and len(email) > 5

'''Valida telefone, se está no formato desejado'''
def valida_telefone(telefone):
    padrao = r"^\(\d{2}\)\s\d\s\d{4}-\d{4}$"
    return re.match(padrao, telefone) is not None

'''Valida data se esta no formato desejado'''
def valida_data(data):
    try:
        datetime.strftime(data, '%d-%M-%Y')
        return True
    except ValueError:
        return False

