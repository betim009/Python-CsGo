import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

from request_api import (
    get_random_weapon,
    get_random_class,
    get_specific_skin,
    get_random_skin,
)


def create_excel(data_frame):
    if os.path.exists("weapons.xlsx"):
        df_read = pd.read_excel("weapons.xlsx")
        df_update = pd.concat([df_read, data_frame])
        return df_update.to_excel("weapons.xlsx", index=False)
    else:
        return data_frame.to_excel("weapons.xlsx", index=False)


def main():
    file_path = "weapons.xlsx"
    start = True
    menu = """Escolha alguma das opções:
[A] Buscar por uma arma aleatória.
[B] Buscar por uma classe de arma aleatória.
[C] Buscar por uma arma específica.
[D] Busca Totalmente aleatória.
[E] Exibir gráfico de preços.
[F] Encerrar o programa.
"""

    menu_a = """Sugestões de armas:
Rifles: AK-47, M4A4
"""
    menu_b = """Sugestões de classes:
Rifle
Knife
Pistol
"""

    menu_c = """Sugestões de armas específicas:
AK-47_Panthera_onca
"""

    while start:
        print(menu)

        option = input("Escolha uma opção: ")

        # Comparando a opção se é igual a E ou E - Encerra o programa
        if option == "F" or option == "f":
            start = False
            print("Programa Encerrado.")

        if option == "A" or option == "a":
            print(menu_a)
            option_a = input("Escolha uma arma: ")

            result_weapon = get_random_weapon(option_a)
            df_weapon = pd.DataFrame([result_weapon])

            print("Resultado da busca: \n", df_weapon)
            print("[S] Salvar - [N] Não salvar")
            save = input("Opção: ")

            if save == "S" or save == "s":
                create_excel(df_weapon)

            start = False

        if option == "B" or option == "b":
            print(menu_b)
            option_b = input("Escolha uma Classe: ")

            result_weapon = get_random_class(option_b)
            df_weapon = pd.DataFrame([result_weapon])

            print("Resultado da busca: \n", df_weapon)
            print("[S] Salvar - [N] Não salvar")
            save = input("Opção: ")

            if save == "S" or save == "s":
                create_excel(df_weapon)

            start = False

        if option == "C" or option == "c":
            print(menu_c)
            option_c = input("Nome: ")

            result_weapon = get_specific_skin(option_c)
            df_weapon = pd.DataFrame([result_weapon])

            print("Resultado da busca: \n", df_weapon)
            print("[S] Salvar - [N] Não salvar")
            save = input("Opção: ")

            if save == "S" or save == "s":
                create_excel(df_weapon)

            start = False

        if option == "D" or option == "d":
            result_weapon = get_random_skin()[0][1]
            df_weapon = pd.DataFrame([result_weapon])

            print("Resultado da busca: \n", df_weapon)
            print("[S] Salvar - [N] Não salvar")
            save = input("Opção: ")

            if save == "S" or save == "s":
                create_excel(df_weapon)

            start = False

        if option == "E" or option == "e":
            if os.path.exists(file_path):
                file = pd.read_excel(file_path)

                names = file["name"]
                prices = file["price"]

                horizontal = np.array(names)
                vertical = np.array(prices)

                # Adicionando rótulos e título
                plt.xlabel("Armas")
                plt.ylabel("Preços")
                plt.title("Gráfico de Preços das Armas")

                plt.bar(horizontal, vertical)
                plt.show()
                
            else:
                print("Não existe dados ainda.\n\n")


main()
