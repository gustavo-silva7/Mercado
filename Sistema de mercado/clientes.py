'''CADASTRAR E VALIDAR CLIENTE'''
def cadastra_cliente():
    print("\n=== CADASTRAR CLIENTE ===")

    nome = input("Nome completo: ").strip()
    if not nome or len(nome) < 3:
        print("Nome invalido!!...")
        pausa()
        return
    
    telefone = input("Telefone (formato: (99) 9 9912-3456): ").strip
    if not valida_telefone(telefone):
        print("Telefone invalido!!...")
        pausa()
        return

    email = input("Digite o e-mail: ").strip
    if not valida_email(email):
        print("E-mail invalido!!...")
        pausa()
        return
    
    cpf = input("Digite o CPF (formato: 000.000.000.00): ").strip
    if not valida_cpf(cpf):
        print("CPF invalido!!...")
        pausa()
        return
    
    nascimento = input("Digite a data de nascimento (dd-mm-aaaa): ")
    if not valida_data(nascimento):
        print("Data invalida!!")
        pausa()
        return