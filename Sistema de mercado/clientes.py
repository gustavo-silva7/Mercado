'''CADASTRAR E VALIDAR CLIENTE'''
def cadastra_cliente():
    print("\n=== CADASTRAR CLIENTE ===")

    nome = input("Nome completo: ").strip()
    if not nome or len(nome) < 3:
        print("Nome invalido!!...")
        pausa()
        return
    
    telefone = input("Telefone (formato: (99) 9 9912-3456): ").strip
    if not valida_telefone():
        print("Telefone invalido!!...")

    email = input("Digite o e-mail: ").strip
    if not valida_email():
        print("E-mail invalido!!...")
    
    cpf = input("Digite o CPF: ").strip
    if not valida_cpf():
        print("CPF invalido!!...")
