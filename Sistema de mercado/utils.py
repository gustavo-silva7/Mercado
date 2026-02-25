"""Funções utilitárias para o sistema de mercado."""

from datetime import datetime


def calcular_idade(data_nascimento):
    """Calcula a idade a partir da data de nascimento.
    
    Args:
        data_nascimento (str): Data no formato YYYY-MM-DD
        
    Returns:
        int: Idade em anos
    """
    try:
        nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y")
        hoje = datetime.now()
        idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        return idade
    except ValueError:
        return 0


def validar_email(email):
    """Valida se o email tem formato básico correto.
    
    Args:
        email (str): Email a validar
        
    Returns:
        bool: True se válido, False caso contrário
    """
    return "@" in email and "." in email


def validar_telefone(telefone):
    """Valida se o telefone contém apenas dígitos.
    
    Args:
        telefone (str): Telefone a validar
        
    Returns:
        bool: True se válido, False caso contrário
    """
    return telefone.isdigit() and len(telefone) >= 10


def validar_preco(preco_str):
    """Converte e valida preço.
    
    Args:
        preco_str (str): Preço como string
        
    Returns:
        float or None: Preço convertido ou None se inválido
    """
    try:
        preco = float(preco_str.replace(",", "."))
        return preco if preco > 0 else None
    except ValueError:
        return None


def validar_estoque(estoque_str):
    """Converte e valida estoque.
    
    Args:
        estoque_str (str): Estoque como string
        
    Returns:
        int or None: Estoque convertido ou None se inválido
    """
    try:
        estoque = int(estoque_str)
        return estoque if estoque > 0 else None
    except ValueError:
        return None


def validar_data(data_str):
    """Valida se a data está no formato correto.
    
    Args:
        data_str (str): Data no formato YYYY-MM-DD
        
    Returns:
        bool: True se válida, False caso contrário
    """
    try:
        datetime.strptime(data_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False
