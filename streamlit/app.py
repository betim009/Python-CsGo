import streamlit as st
import requests

# Função para processar o valor
def processar_valor(valor):
    headers = {
        "x-rapidapi-key": "3be01a29a9msh1147fa36f6934f8p13aa60jsn802d2dd1cc9f",
        "x-rapidapi-host": "cs-skin-api.p.rapidapi.com",
    }
    
    url = f"https://cs-skin-api.p.rapidapi.com/random/{valor}"
    response = requests.get(url, headers=headers)
    return response.json()

# Título do aplicativo
st.title("Coletar Valor com Input e Botão")

# Campo de entrada para coletar um valor
input_valor = st.text_input("Digite um valor:")

# Botão para submeter o valor
if st.button("Submeter"):
    # Verifica se o valor foi inserido
    if input_valor:
        # Chama a função para processar o valor
        resultado = processar_valor(input_valor)
        
        # Verifica se a resposta é um dicionário
        if isinstance(resultado, dict):
            # Exibe o resultado em uma estrutura similar a uma tabela
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(resultado['img'], width=150)
            with col2:
                st.write(f"**Nome:** {resultado['name']}")
                st.write(f"**Preço:** {resultado['price']}")
                st.write(f"**Arma:** {resultado['weapon']}")
                st.write(f"**Classe:** {resultado['class']}")
        else:
            st.error("Resposta inesperada da API.")
    else:
        st.error("Por favor, insira um valor antes de submeter.")
