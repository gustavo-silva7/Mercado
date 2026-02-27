"""Gerenciamento de clientes do sistema."""

from utils import (
    CLIENTES_FILE, gerar_proximo_id, ler_linhas, escrever_linhas,
    validar_email, validar_telefone, validar_data, calcular_idade,
    buscar_by_id, pausa
)


def cadastrar_cliente():
    """Cadastra novo cliente com validação completa."""
    print("\n=== CADASTRAR CLIENTE ===")
    
    nome = input("Nome completo: ").strip()
    if not nome or len(nome) < 3:
        print("❌ Nome deve ter pelo menos 3 caracteres!")
        pausa()
        return
    
    telefone = input("Telefone (10+ dígitos): ").strip()
    if not validar_telefone(telefone):
        print("❌ Telefone inválido! Use apenas números (mínimo 10 dígitos).")
        pausa()
        return
    
    email = input("Email: ").strip()
    if not validar_email(email):
        print("❌ Email inválido!")
        pausa()
        return
    
    # Verificar se email já existe
    if email_existe(email):
        print("❌ Este email já está cadastrado!")
        pausa()
        return
    
    data_nascimento = input("Data de nascimento (AAAA-MM-DD): ").strip()
    if not validar_data(data_nascimento):
        print("❌ Data inválida! Use o formato AAAA-MM-DD")
        pausa()
        return
    
    # Gerar novo ID
    novo_id = gerar_proximo_id(CLIENTES_FILE)
    
    # Criar linha do cliente
    linha_cliente = f"{novo_id};{nome};{telefone};{email};{data_nascimento}"
    
    # Adicionar ao arquivo
    linhas = ler_linhas(CLIENTES_FILE)
    linhas.append(linha_cliente)
    escrever_linhas(CLIENTES_FILE, linhas)
    
    print(f"✅ Cliente cadastrado com sucesso! (ID: {novo_id})")
    pausa()


def listar_clientes():
    """Lista todos os clientes com idade calculada."""
    print("\n=== LISTAR CLIENTES ===")
    
    linhas = ler_linhas(CLIENTES_FILE)
    
    if not linhas:
        print("📭 Nenhum cliente cadastrado.")
        pausa()
        return
    
    print("\n{:<5} {:<25} {:<15} {:<25} {:<6}".format(
        "ID", "Nome", "Telefone", "Email", "Idade"
    ))
    print("-" * 80)
    
    for linha in linhas:
        partes = linha.split(';')
        if len(partes) < 5:
            continue
        
        id_cliente, nome, telefone, email, data_nasc = partes[:5]
        idade = calcular_idade(data_nasc)
        idade_str = str(idade) if idade else "?"
        
        print("{:<5} {:<25} {:<15} {:<25} {:<6}".format(
            id_cliente, nome[:24], telefone, email[:24], idade_str
        ))
    
    pausa()


def buscar_cliente():
    """Busca cliente por nome ou telefone."""
    print("\n=== BUSCAR CLIENTE ===")
    
    print("1 - Buscar por nome")
    print("2 - Buscar por telefone")
    opcao = input("Escolha: ").strip()
    
    if opcao == "1":
        termo = input("Digite o nome (ou parte dele): ").strip().lower()
        linhas = ler_linhas(CLIENTES_FILE)
        
        resultados = []
        for linha in linhas:
            partes = linha.split(';')
            if len(partes) >= 2 and termo in partes[1].lower():
                resultados.append(linha)
        
        if resultados:
            print(f"\n📌 Encontrados {len(resultados)} resultado(s):\n")
            print("{:<5} {:<25} {:<15} {:<25} {:<6}".format(
                "ID", "Nome", "Telefone", "Email", "Idade"
            ))
            print("-" * 80)
            
            for linha in resultados:
                partes = linha.split(';')
                if len(partes) >= 5:
                    id_cliente, nome, telefone, email, data_nasc = partes[:5]
                    idade = calcular_idade(data_nasc)
                    idade_str = str(idade) if idade else "?"
                    print("{:<5} {:<25} {:<15} {:<25} {:<6}".format(
                        id_cliente, nome[:24], telefone, email[:24], idade_str
                    ))
        else:
            print("❌ Nenhum cliente encontrado com esse nome.")
    
    elif opcao == "2":
        termo = input("Digite o telefone: ").strip()
        linhas = ler_linhas(CLIENTES_FILE)
        
        resultados = []
        for linha in linhas:
            partes = linha.split(';')
            if len(partes) >= 3 and termo in partes[2]:
                resultados.append(linha)
        
        if resultados:
            print(f"\n📌 Encontrados {len(resultados)} resultado(s):\n")
            print("{:<5} {:<25} {:<15} {:<25} {:<6}".format(
                "ID", "Nome", "Telefone", "Email", "Idade"
            ))
            print("-" * 80)
            
            for linha in resultados:
                partes = linha.split(';')
                if len(partes) >= 5:
                    id_cliente, nome, telefone, email, data_nasc = partes[:5]
                    idade = calcular_idade(data_nasc)
                    idade_str = str(idade) if idade else "?"
                    print("{:<5} {:<25} {:<15} {:<25} {:<6}".format(
                        id_cliente, nome[:24], telefone, email[:24], idade_str
                    ))
        else:
            print("❌ Nenhum cliente encontrado com esse telefone.")
    
    else:
        print("❌ Opção inválida!")
    
    pausa()


def remover_cliente():
    """Remove um cliente pelo ID."""
    print("\n=== REMOVER CLIENTE ===")
    
    listar_clientes_simples()
    
    try:
        id_remover = int(input("\nDigite o ID do cliente a remover: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        pausa()
        return
    
    idx, linha = buscar_by_id(CLIENTES_FILE, id_remover)
    
    if idx is None:
        print("❌ Cliente não encontrado!")
        pausa()
        return
    
    print(f"\n⚠️  Confirmar remoção do cliente:\n{linha}")
    confirma = input("Remover? (s/n): ").strip().lower()
    
    if confirma != 's':
        print("❌ Operação cancelada.")
        pausa()
        return
    
    linhas = ler_linhas(CLIENTES_FILE)
    linhas.pop(idx)
    escrever_linhas(CLIENTES_FILE, linhas)
    
    print(f"✅ Cliente removido com sucesso!")
    pausa()


def email_existe(email):
    """Verifica se email já existe."""
    linhas = ler_linhas(CLIENTES_FILE)
    for linha in linhas:
        partes = linha.split(';')
        if len(partes) >= 4 and partes[3] == email:
            return True
    return False


def listar_clientes_simples():
    """Lista clientes de forma simples (sem pausa)."""
    linhas = ler_linhas(CLIENTES_FILE)
    
    if not linhas:
        print("📭 Nenhum cliente cadastrado.")
        return
    
    print("\n{:<5} {:<25} {:<15} {:<25}".format(
        "ID", "Nome", "Telefone", "Email"
    ))
    print("-" * 75)
    
    for linha in linhas:
        partes = linha.split(';')
        if len(partes) >= 4:
            id_cliente, nome, telefone, email = partes[:4]
            print("{:<5} {:<25} {:<15} {:<25}".format(
                id_cliente, nome[:24], telefone, email[:24]
            ))


def menu_clientes():
    """Menu principal de clientes."""
    while True:
        print("\n╔════════════════════════════════╗")
        print("║   GERENCIAR CLIENTES            ║")
        print("╠════════════════════════════════╣")
        print("║ 1 - Cadastrar                   ║")
        print("║ 2 - Listar                      ║")
        print("║ 3 - Buscar                      ║")
        print("║ 4 - Remover                     ║")
        print("║ 0 - Voltar                      ║")
        print("╚════════════════════════════════╝")
        
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
            print("❌ Opção inválida!")
