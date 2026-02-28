import os, re
from datetime import datetime

'''Verifica se os arquivos .txt existem, se não, cria o arquivo'''
def arquivo_existe(nome_arquivo):
    if not os.path.exixte(nome_arquivo):
        open(nome_arquivo,'w').close()

'''Valida E-mail'''
def valida_email(email):
    return '@' in email and '.' in email and len(email) > 5

def valida_telefone(telefone):
    padrao = r"^\(\d{2}\)\s\d\s\d{4}-\d{4}$"
    return re.match(padrao, telefone) is not None