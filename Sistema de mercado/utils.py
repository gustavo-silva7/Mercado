"""Funções utilitárias para o sistema de mercado."""

import os
from datetime import datetime


CLIENTES_FILE = "clientes.txt"
PRODUTOS_FILE = "produtos.txt"


def garantir_arquivo_existe(nome_arquivo):
    """Cria arquivo vazio se não existir."""
    if not os.path.exists(nome_arquivo):
        open(nome_arquivo, 'w').close()


def ler_linhas(nome_arquivo):
    """Lê todas as linhas do arquivo e retorna lista."""
    garantir_arquivo_existe(nome_arquivo)
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()
    return [linha.strip() for linha in linhas if linha.strip()]


def escrever_linhas(nome_arquivo, linhas):
    """Escreve linhas no arquivo, sobrescrevendo conteúdo."""
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for linha in linhas:
            arquivo.write(linha + '\n')


def gerar_proximo_id(nome_arquivo):
    """Gera próximo ID único lendo maior ID do arquivo."""
    linhas = ler_linhas(nome_arquivo)
    
    if not linhas:
        return 1
    
    maior_id = 0
    for linha in linhas:
        partes = linha.split(';')
        if partes:
            try:
                id_item = int(partes[0])
                if id_item > maior_id:
                    maior_id = id_item
            except ValueError:
                continue
    
    return maior_id + 1


def validar_email(email):
    """Valida se email tem formato básico correto."""
    return '@' in email and '.' in email and len(email) > 5


def validar_telefone(telefone):
    """Valida se telefone tem apenas dígitos."""
    return telefone.isdigit() and len(telefone) >= 10


def validar_data(data_str):
    """Valida formato de data AAAA-MM-DD e retorna True se válida."""
    try:
        datetime.strptime(data_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def calcular_idade(data_nascimento):
    """Calcula idade a partir de data no formato AAAA-MM-DD."""
    try:
        data_nasc = datetime.strptime(data_nascimento, '%Y-%m-%d')
        hoje = datetime.now()
        idade = hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))
        return idade
    except ValueError:
        return None


def validar_preco(preco_str):
    """Valida se é um preço numérico válido (float)."""
    try:
        preco = float(preco_str)
        return preco > 0, preco
    except ValueError:
        return False, None


def validar_estoque(estoque_str):
    """Valida se é um estoque inteiro válido (> 0)."""
    try:
        estoque = int(estoque_str)
        return estoque > 0, estoque
    except ValueError:
        return False, None


def buscar_by_id(nome_arquivo, id_procurado):
    """Busca item por ID no arquivo. Retorna (índice, linha) ou (None, None)."""
    linhas = ler_linhas(nome_arquivo)
    
    for idx, linha in enumerate(linhas):
        partes = linha.split(';')
        if partes and partes[0] == str(id_procurado):
            return idx, linha
    
    return None, None


def limpar_tela():
    """Limpa a tela do terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pausa():
    """Faz pausa para o usuário ver a mensagem."""
    input("\nPressione ENTER para continuar...")
