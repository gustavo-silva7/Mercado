"""Sistema de Mercado - Menu Principal"""

from clientes import menu_clientes
from produtos import menu_produtos
from utils import limpar_tela


def exibir_titulo():
    """Exibe o título do sistema."""
    print("\n" + "="*50)
    print("🛒 SISTEMA DE MERCADO 🛒".center(50))
    print("="*50)


def menu_principal():
    """Menu principal do sistema."""
    while True:
        exibir_titulo()
        print("\n╔════════════════════════════════╗")
        print("║      MENU PRINCIPAL             ║")
        print("╠════════════════════════════════╣")
        print("║ 1 - Gerenciar Clientes          ║")
        print("║ 2 - Gerenciar Produtos          ║")
        print("║ 0 - Sair                        ║")
        print("╚════════════════════════════════╝")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            menu_clientes()
        elif opcao == "2":
            menu_produtos()
        elif opcao == "0":
            print("\n👋 Até logo! Sistema finalizado.")
            break
        else:
            print("❌ Opção inválida!")
            input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    menu_principal()
