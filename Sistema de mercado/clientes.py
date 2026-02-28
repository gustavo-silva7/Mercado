def cadastra_cliente():
    print("\n=== CADASTRAR CLIENTE ===")

    nome = input("Nome completo: ").strip()
    if not nome or len(nome) < 3:
        print("!!lindomarb pNome invalido!!")