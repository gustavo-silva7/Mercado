"""Módulo para gerenciamento de clientes."""

import os
from utils import (
    calcular_idade,
    validar_email,
    validar_telefone,
    validar_data,
)

ARQUIVO_CLIENTES = "clientes.txt"


def _garantir_arquivo():
    """Garante que o arquivo de clientes existe."""
    if not os.path.exists(ARQUIVO_CLIENTES):
        with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as f:
            pass


def _ler_clientes():
    """Lê todos os clientes do arquivo.
    
    Returns:
        list: Lista de dicionários com dados dos clientes
    """
    _garantir_arquivo()
    clientes = []
    
    try:
        with open(ARQUIVO_CLIENTES, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(";")
                    if len(partes) == 5:
                        clientes.append({
                            "id": int(partes[0]),
                            "nome": partes[1],
                            "telefone": partes[2],
                            "email": partes[3],
                            "data_nascimento": partes[4],
                        })
    except (ValueError, IOError):
        pass
    
    return clientes


def _gerar_id():
    """Gera o próximo ID disponível.
    
    Returns:
        int: Próximo ID
    """
    clientes = _ler_clientes()
    if not clientes:
        return 1
    return max(cliente["id"] for cliente in clientes) + 1


def _salvar_clientes(clientes):
    """Salva lista de clientes no arquivo.
    
    Args:
        clientes (list): Lista de dicionários com dados dos clientes
    """
    try:
        with open(ARQUIVO_CLIENTES, "w", encoding="utf-8") as f:
            for cliente in clientes:
                linha = f"{cliente['id']};{cliente['nome']};{cliente['telefone']};{cliente['email']};{cliente['data_nascimento']}\n"
                f.write(linha)
    except IOError as e:
        print(f"❌ Erro ao salvar clientes: {e}")


def cadastrar_cliente():
    """Cadastra um novo cliente com validações."""
    print("\n" + "="*50)
    print("CADASTRAR NOVO CLIENTE")
    print("="*50)
    
    try:
        nome = input("Nome: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        telefone = input("Telefone: ").strip()
        if not validar_telefone(telefone):
            print("❌ Telefone inválido! Use apenas dígitos (mín. 10).")
            return
        
        email = input("Email: ").strip()
        if not validar_email(email):
            print("❌ Email inválido!")
            return
        
        data_nascimento = input("Data de nascimento (YYYY-MM-DD): ").strip()
        if not validar_data(data_nascimento):
            print("❌ Data inválida! Use o formato YYYY-MM-DD")
            return
        
        # Verifica email duplicado
        clientes = _ler_clientes()
        if any(cliente["email"] == email for cliente in clientes):
            print("❌ Email já cadastrado!")
            return
        
        novo_cliente = {
            "id": _gerar_id(),
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "data_nascimento": data_nascimento,
        }
        
        clientes.append(novo_cliente)
        _salvar_clientes(clientes)
        
        print(f"✅ Cliente cadastrado com sucesso! ID: {novo_cliente['id']}")
        
    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada.")
    except Exception as e:
        print(f"❌ Erro ao cadastrar cliente: {e}")


def listar_clientes():
    """Lista todos os clientes com idade calculada."""
    print("\n" + "="*50)
    print("LISTA DE CLIENTES")
    print("="*50)
    
    clientes = _ler_clientes()
    
    if not clientes:
        print("📭 Nenhum cliente cadastrado.")
        return
    
    print(f"\n{'ID':<5} {'Nome':<20} {'Idade':<6} {'Telefone':<15} {'Email':<25}")
    print("-" * 80)
    
    for cliente in clientes:
        idade = calcular_idade(cliente["data_nascimento"])
        print(f"{cliente['id']:<5} {cliente['nome']:<20} {idade:<6} {cliente['telefone']:<15} {cliente['email']:<25}")
    
    print()


def buscar_cliente():
    """Busca cliente por nome ou telefone."""
    print("\n" + "="*50)
    print("BUSCAR CLIENTE")
    print("="*50)
    
    criterio = input("Digite o nome ou telefone: ").strip()
    if not criterio:
        print("❌ Campo não pode estar vazio!")
        return
    
    clientes = _ler_clientes()
    resultados = [c for c in clientes if criterio.lower() in c["nome"].lower() or criterio in c["telefone"]]
    
    if not resultados:
        print(f"🔍 Nenhum cliente encontrado com '{criterio}'")
        return
    
    print(f"\n{'ID':<5} {'Nome':<20} {'Idade':<6} {'Telefone':<15} {'Email':<25}")
    print("-" * 80)
    
    for cliente in resultados:
        idade = calcular_idade(cliente["data_nascimento"])
        print(f"{cliente['id']:<5} {cliente['nome']:<20} {idade:<6} {cliente['telefone']:<15} {cliente['email']:<25}")
    
    print()


def remover_cliente():
    """Remove um cliente pelo ID."""
    print("\n" + "="*50)
    print("REMOVER CLIENTE")
    print("="*50)
    
    try:
        id_cliente = int(input("ID do cliente a remover: ").strip())
    except ValueError:
        print("❌ ID deve ser um número!")
        return
    
    clientes = _ler_clientes()
    cliente_encontrado = next((c for c in clientes if c["id"] == id_cliente), None)
    
    if not cliente_encontrado:
        print(f"❌ Cliente com ID {id_cliente} não encontrado!")
        return
    
    confirmacao = input(f"Tem certeza que deseja remover '{cliente_encontrado['nome']}'? (s/n): ").strip().lower()
    
    if confirmacao != "s":
        print("⚠️ Operação cancelada.")
        return
    
    clientes = [c for c in clientes if c["id"] != id_cliente]
    _salvar_clientes(clientes)
    
    print(f"✅ Cliente '{cliente_encontrado['nome']}' removido com sucesso!")


def menu_clientes():
    """Menu de gerenciamento de clientes."""
    while True:
        print("\n" + "="*50)
        print("GERENCIAR CLIENTES")
        print("="*50)
        print("1 - Cadastrar Cliente")
        print("2 - Listar Clientes")
        print("3 - Buscar Cliente")
        print("4 - Remover Cliente")
        print("0 - Voltar ao Menu Principal")
        print("="*50)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            buscar_cliente()
        elif opcao == "4":
            remover_cliente()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")
