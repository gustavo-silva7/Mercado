"""Gerenciamento de produtos do sistema."""

from utils import (
    PRODUTOS_FILE, gerar_proximo_id, ler_linhas, escrever_linhas,
    validar_preco, validar_estoque, buscar_by_id, pausa
)


def cadastrar_produto():
    """Cadastra novo produto com validação completa."""
    print("\n=== CADASTRAR PRODUTO ===")
    
    nome = input("Nome do produto: ").strip()
    if not nome or len(nome) < 3:
        print("❌ Nome deve ter pelo menos 3 caracteres!")
        pausa()
        return
    
    preco_input = input("Preço (use . para decimal): ").strip()
    valido, preco = validar_preco(preco_input)
    if not valido:
        print("❌ Preço inválido! Use formato numérico (ex: 25.90)")
        pausa()
        return
    
    estoque_input = input("Quantidade em estoque: ").strip()
    valido, estoque = validar_estoque(estoque_input)
    if not valido:
        print("❌ Estoque inválido! Use um número inteiro maior que 0")
        pausa()
        return
    
    # Gerar novo ID
    novo_id = gerar_proximo_id(PRODUTOS_FILE)
    
    # Criar linha do produto
    linha_produto = f"{novo_id};{nome};{preco:.2f};{estoque}"
    
    # Adicionar ao arquivo
    linhas = ler_linhas(PRODUTOS_FILE)
    linhas.append(linha_produto)
    escrever_linhas(PRODUTOS_FILE, linhas)
    
    print(f"✅ Produto cadastrado com sucesso! (ID: {novo_id})")
    pausa()


def listar_produtos():
    """Lista todos os produtos."""
    print("\n=== LISTAR PRODUTOS ===")
    
    linhas = ler_linhas(PRODUTOS_FILE)
    
    if not linhas:
        print("📭 Nenhum produto cadastrado.")
        pausa()
        return
    
    print("\n{:<5} {:<30} {:<12} {:<12}".format(
        "ID", "Nome", "Preço", "Estoque"
    ))
    print("-" * 62)
    
    for linha in linhas:
        partes = linha.split(';')
        if len(partes) < 4:
            continue
        
        id_produto, nome, preco_str, estoque_str = partes[:4]
        
        try:
            preco = float(preco_str)
            estoque = int(estoque_str)
            print("{:<5} {:<30} R$ {:<10.2f} {:<12}".format(
                id_produto, nome[:29], preco, estoque
            ))
        except ValueError:
            continue
    
    pausa()


def atualizar_estoque():
    """Atualiza estoque de um produto."""
    print("\n=== ATUALIZAR ESTOQUE ===")
    
    listar_produtos_simples()
    
    try:
        id_produto = int(input("\nDigite o ID do produto: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        pausa()
        return
    
    idx, linha = buscar_by_id(PRODUTOS_FILE, id_produto)
    
    if idx is None:
        print("❌ Produto não encontrado!")
        pausa()
        return
    
    print(f"\n📦 Produto atual: {linha}")
    
    novo_estoque_input = input("Novo estoque (quantidade): ").strip()
    valido, novo_estoque = validar_estoque(novo_estoque_input)
    
    if not valido:
        print("❌ Estoque inválido!")
        pausa()
        return
    
    # Atualizar linha
    partes = linha.split(';')
    if len(partes) < 4:
        print("❌ Erro ao processar produto!")
        pausa()
        return
    
    id_p, nome, preco = partes[0], partes[1], partes[2]
    linha_atualizada = f"{id_p};{nome};{preco};{novo_estoque}"
    
    # Reescrever arquivo
    linhas = ler_linhas(PRODUTOS_FILE)
    linhas[idx] = linha_atualizada
    escrever_linhas(PRODUTOS_FILE, linhas)
    
    print(f"✅ Estoque atualizado com sucesso!")
    pausa()


def remover_produto():
    """Remove um produto pelo ID."""
    print("\n=== REMOVER PRODUTO ===")
    
    listar_produtos_simples()
    
    try:
        id_remover = int(input("\nDigite o ID do produto a remover: ").strip())
    except ValueError:
        print("❌ ID inválido!")
        pausa()
        return
    
    idx, linha = buscar_by_id(PRODUTOS_FILE, id_remover)
    
    if idx is None:
        print("❌ Produto não encontrado!")
        pausa()
        return
    
    print(f"\n⚠️  Confirmar remoção do produto:\n{linha}")
    confirma = input("Remover? (s/n): ").strip().lower()
    
    if confirma != 's':
        print("❌ Operação cancelada.")
        pausa()
        return
    
    linhas = ler_linhas(PRODUTOS_FILE)
    linhas.pop(idx)
    escrever_linhas(PRODUTOS_FILE, linhas)
    
    print(f"✅ Produto removido com sucesso!")
    pausa()


def relatorio_estoque_baixo():
    """Mostra relatório de estoque baixo (< 10 unidades)."""
    print("\n=== RELATÓRIO DE ESTOQUE BAIXO ===")
    
    linhas = ler_linhas(PRODUTOS_FILE)
    
    if not linhas:
        print("📭 Nenhum produto cadastrado.")
        pausa()
        return
    
    baixo_estoque = []
    
    for linha in linhas:
        partes = linha.split(';')
        if len(partes) < 4:
            continue
        
        try:
            id_produto = partes[0]
            nome = partes[1]
            preco = float(partes[2])
            estoque = int(partes[3])
            
            if estoque < 10:
                baixo_estoque.append((id_produto, nome, preco, estoque))
        except ValueError:
            continue
    
    if not baixo_estoque:
        print("✅ Todos os produtos têm estoque adequado!")
        pausa()
        return
    
    print(f"\n⚠️  {len(baixo_estoque)} produto(s) com estoque baixo:\n")
    print("{:<5} {:<30} {:<12} {:<12}".format(
        "ID", "Nome", "Preço", "Estoque"
    ))
    print("-" * 62)
    
    for id_prod, nome, preco, estoque in baixo_estoque:
        print("{:<5} {:<30} R$ {:<10.2f} {:<12}".format(
            id_prod, nome[:29], preco, estoque
        ))
    
    pausa()


def listar_produtos_simples():
    """Lista produtos de forma simples (sem pausa)."""
    linhas = ler_linhas(PRODUTOS_FILE)
    
    if not linhas:
        print("📭 Nenhum produto cadastrado.")
        return
    
    print("\n{:<5} {:<30} {:<12} {:<12}".format(
        "ID", "Nome", "Preço", "Estoque"
    ))
    print("-" * 62)
    
    for linha in linhas:
        partes = linha.split(';')
        if len(partes) >= 4:
            try:
                id_prod = partes[0]
                nome = partes[1]
                preco = float(partes[2])
                estoque = int(partes[3])
                print("{:<5} {:<30} R$ {:<10.2f} {:<12}".format(
                    id_prod, nome[:29], preco, estoque
                ))
            except ValueError:
                continue


def menu_produtos():
    """Menu principal de produtos."""
    while True:
        print("\n╔════════════════════════════════╗")
        print("║   GERENCIAR PRODUTOS            ║")
        print("╠════════════════════════════════╣")
        print("║ 1 - Cadastrar                   ║")
        print("║ 2 - Listar                      ║")
        print("║ 3 - Atualizar Estoque           ║")
        print("║ 4 - Remover                     ║")
        print("║ 5 - Relatório Estoque Baixo     ║")
        print("║ 0 - Voltar                      ║")
        print("╚════════════════════════════════╝")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            atualizar_estoque()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            relatorio_estoque_baixo()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida!")
