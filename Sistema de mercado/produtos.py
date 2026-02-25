"""Módulo para gerenciamento de produtos."""

import os
from utils import validar_preco, validar_estoque

ARQUIVO_PRODUTOS = "produtos.txt"
LIMITE_ESTOQUE_BAIXO = 10


def _garantir_arquivo():
    """Garante que o arquivo de produtos existe."""
    if not os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
            pass


def _ler_produtos():
    """Lê todos os produtos do arquivo.
    
    Returns:
        list: Lista de dicionários com dados dos produtos
    """
    _garantir_arquivo()
    produtos = []
    
    try:
        with open(ARQUIVO_PRODUTOS, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha:
                    partes = linha.split(";")
                    if len(partes) == 4:
                        produtos.append({
                            "id": int(partes[0]),
                            "nome": partes[1],
                            "preco": float(partes[2]),
                            "estoque": int(partes[3]),
                        })
    except (ValueError, IOError):
        pass
    
    return produtos


def _gerar_id():
    """Gera o próximo ID disponível.
    
    Returns:
        int: Próximo ID
    """
    produtos = _ler_produtos()
    if not produtos:
        return 1
    return max(produto["id"] for produto in produtos) + 1


def _salvar_produtos(produtos):
    """Salva lista de produtos no arquivo.
    
    Args:
        produtos (list): Lista de dicionários com dados dos produtos
    """
    try:
        with open(ARQUIVO_PRODUTOS, "w", encoding="utf-8") as f:
            for produto in produtos:
                linha = f"{produto['id']};{produto['nome']};{produto['preco']:.2f};{produto['estoque']}\n"
                f.write(linha)
    except IOError as e:
        print(f"❌ Erro ao salvar produtos: {e}")


def cadastrar_produto():
    """Cadastra um novo produto com validações."""
    print("\n" + "="*50)
    print("CADASTRAR NOVO PRODUTO")
    print("="*50)
    
    try:
        nome = input("Nome do produto: ").strip()
        if not nome:
            print("❌ Nome não pode estar vazio!")
            return
        
        preco_str = input("Preço (use . ou ,): ").strip()
        preco = validar_preco(preco_str)
        if preco is None:
            print("❌ Preço inválido! Deve ser um número positivo.")
            return
        
        estoque_str = input("Quantidade em estoque: ").strip()
        estoque = validar_estoque(estoque_str)
        if estoque is None:
            print("❌ Estoque inválido! Deve ser um número inteiro positivo.")
            return
        
        novo_produto = {
            "id": _gerar_id(),
            "nome": nome,
            "preco": preco,
            "estoque": estoque,
        }
        
        produtos = _ler_produtos()
        produtos.append(novo_produto)
        _salvar_produtos(produtos)
        
        print(f"✅ Produto cadastrado com sucesso! ID: {novo_produto['id']}")
        
    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada.")
    except Exception as e:
        print(f"❌ Erro ao cadastrar produto: {e}")


def listar_produtos():
    """Lista todos os produtos."""
    print("\n" + "="*50)
    print("LISTA DE PRODUTOS")
    print("="*50)
    
    produtos = _ler_produtos()
    
    if not produtos:
        print("📭 Nenhum produto cadastrado.")
        return
    
    print(f"\n{'ID':<5} {'Nome':<25} {'Preço':<12} {'Estoque':<10} {'Status':<15}")
    print("-" * 70)
    
    for produto in produtos:
        preco_formatado = f"R$ {produto['preco']:.2f}"
        status = "⚠️ BAIXO" if produto["estoque"] <= LIMITE_ESTOQUE_BAIXO else "✅ OK"
        print(f"{produto['id']:<5} {produto['nome']:<25} {preco_formatado:<12} {produto['estoque']:<10} {status:<15}")
    
    print()


def atualizar_estoque():
    """Atualiza o estoque de um produto."""
    print("\n" + "="*50)
    print("ATUALIZAR ESTOQUE")
    print("="*50)
    
    try:
        id_produto = int(input("ID do produto: ").strip())
    except ValueError:
        print("❌ ID deve ser um número!")
        return
    
    produtos = _ler_produtos()
    produto = next((p for p in produtos if p["id"] == id_produto), None)
    
    if not produto:
        print(f"❌ Produto com ID {id_produto} não encontrado!")
        return
    
    print(f"\nProduto encontrado: {produto['nome']}")
    print(f"Estoque atual: {produto['estoque']}")
    
    try:
        novo_estoque_str = input("Novo estoque: ").strip()
        novo_estoque = validar_estoque(novo_estoque_str)
        
        if novo_estoque is None:
            print("❌ Estoque inválido! Deve ser um número inteiro positivo.")
            return
        
        produto["estoque"] = novo_estoque
        _salvar_produtos(produtos)
        
        print(f"✅ Estoque atualizado com sucesso! Novo estoque: {novo_estoque}")
        
    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada.")
    except Exception as e:
        print(f"❌ Erro ao atualizar estoque: {e}")


def remover_produto():
    """Remove um produto pelo ID."""
    print("\n" + "="*50)
    print("REMOVER PRODUTO")
    print("="*50)
    
    try:
        id_produto = int(input("ID do produto a remover: ").strip())
    except ValueError:
        print("❌ ID deve ser um número!")
        return
    
    produtos = _ler_produtos()
    produto = next((p for p in produtos if p["id"] == id_produto), None)
    
    if not produto:
        print(f"❌ Produto com ID {id_produto} não encontrado!")
        return
    
    confirmacao = input(f"Tem certeza que deseja remover '{produto['nome']}'? (s/n): ").strip().lower()
    
    if confirmacao != "s":
        print("⚠️ Operação cancelada.")
        return
    
    produtos = [p for p in produtos if p["id"] != id_produto]
    _salvar_produtos(produtos)
    
    print(f"✅ Produto '{produto['nome']}' removido com sucesso!")


def relatorio_estoque_baixo():
    """Mostra relatório de produtos com estoque baixo."""
    print("\n" + "="*50)
    print("RELATÓRIO DE ESTOQUE BAIXO")
    print(f"(Limite: {LIMITE_ESTOQUE_BAIXO} unidades)")
    print("="*50)
    
    produtos = _ler_produtos()
    baixos = [p for p in produtos if p["estoque"] <= LIMITE_ESTOQUE_BAIXO]
    
    if not baixos:
        print("✅ Todos os produtos têm estoque adequado!")
        return
    
    print(f"\n{'ID':<5} {'Nome':<25} {'Preço':<12} {'Estoque':<10}")
    print("-" * 55)
    
    for produto in baixos:
        preco_formatado = f"R$ {produto['preco']:.2f}"
        print(f"{produto['id']:<5} {produto['nome']:<25} {preco_formatado:<12} {produto['estoque']:<10}")
    
    print(f"\n⚠️ Total de produtos com estoque baixo: {len(baixos)}")
    print()


def menu_produtos():
    """Menu de gerenciamento de produtos."""
    while True:
        print("\n" + "="*50)
        print("GERENCIAR PRODUTOS")
        print("="*50)
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Atualizar Estoque")
        print("4 - Remover Produto")
        print("5 - Relatório de Estoque Baixo")
        print("0 - Voltar ao Menu Principal")
        print("="*50)
        
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
            print("❌ Opção inválida! Tente novamente.")
        
        input("\nPressione ENTER para continuar...")
