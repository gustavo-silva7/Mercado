"""Sistema de Mercado - Menu Principal"""

from clientes import menu_clientes
from produtos import menu_produtos


def exibir_menu_principal():
    """Exibe o menu principal do sistema."""
    print("\n" + "="*50)
    print("🛒 SISTEMA DE MERCADO 🛒")
    print("="*50)
    print("1 - Gerenciar Clientes")
    print("2 - Gerenciar Produtos")
    print("0 - Sair")
    print("="*50)


def main():
    """Função principal que controla o loop do sistema."""
    while True:
        exibir_menu_principal()
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "0":
            print("\n👋 Encerrando o sistema... Até logo!")
            break
        else:
            print("\n❌ Opção inválida! Tente novamente.")
            input("Pressione ENTER para continuar...")


if __name__ == "__main__":
    main()
