import streamlit as st
from read_weapons import read_weapons

st.set_page_config(page_title="Meu Aplicativo Streamlit", layout="wide")


def main():
    st.title("App Cs-Go Skins")
    st.write("Bem-vindo!")

    data = read_weapons()

    if not data:
        st.write("Nenhum dado encontrado.")
        return

    num_columns = 4
    columns = st.columns(num_columns)

    for index, weapon in enumerate(data):
        col = columns[index % num_columns]
        with col:
            st.image(weapon["img"], caption=weapon["name"])
            st.write(f"**Nome:** {weapon['name']}")
            st.write(f"**Arma:** {weapon['weapon']}")
            st.write(f"**Preço:** {weapon['price']}")
            st.write(f"**Classe:** {weapon['class']}")


if __name__ == "__main__":
    main()
