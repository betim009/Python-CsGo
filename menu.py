"""
Esse arquivo é responsavel pelo menu do app
"""
from tabela import tabela


def menu():
    start = True
    menu_painel = """
Escolha alguma das opções:
[A] Weapon.
[B] Classe.
[C] Específico.
[D] Aleatório.
[E] Gráficos.
[F] Encerrar o programa.
"""

    menu_painel_a = """
[A] Buscar por uma arma.
[B] Exibir gráfico por arma.
[C] Sair.    
"""

    menu_painel_b = """
[A] Buscar por uma classe.
[B] Exibir gráfico por classe.
[C] Sair.    
"""

    menu_painel_c = """
[A] Buscar por uma arma específica.
[B] Exibir gráfico de uma arma específica.
[C] Sair.  
"""
    while start:
        print(menu_painel)
        option_menu = input("Escolha uma das opções: ")

        if option_menu == "A" or option_menu == "a":
            print(menu_painel_a)
            option = input("Escolha sua opção: ")

            if option == "A" or option == "a":
                query = input("Digite o valor: ")
                tabela(query, "A")

        if option_menu == "B" or option_menu == "b":
            print(menu_painel_b)

        if option_menu == "C" or option_menu == "c":
            print(menu_painel_c)

        if option_menu == "F" or option_menu == "f":
            print("O pograma foi encerrado!")
            start = False
