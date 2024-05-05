import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')  # lendo os dados

# Cabeçalho
st.header('Encontre seu carro .NET')


 # criar um botão
hist_button = st.button('Criar Grafico - odometer')
scatter_button = st.button('Criar gráfico de dispersão')


if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    # escrever uma mensagem
    st.write('Criar um grafico de disperção para o conjunto de dados de anúncios de vendas de carros')
    # criar um grafico de disperção
    fig = px.scartter(car_data, x="odometer", y="price")
    #exibir um grafico Plotly interativo
    str.plotly(fig, use_container_width=True)