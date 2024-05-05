import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles.csv')  # lendo os dados

# Cabeçalho
st.header('Visualização de alguns dados referente ao anúncio de vendas de carros')
st.header('Aqui você verá três tipos de graficos')

# criar um botão
hist_button = st.button('Criar Gráfico - Odometer')
scatter_button = st.button('Criar Gráfico de Dispersão')
bar_button = st.button('Criar um Gráfico de Barra')
bar_button2 = st.button('Criar um Gráfico de Barra - Cores')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criar um grafico de disperção para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de disperção
    fig = px.scatter(car_data, x="model_year", y="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if bar_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de barra para o conjunto de dados de anúncios de vendas de carros')

    # criar um gráfico de barras
    fig1 = px.bar(car_data, x='paint_color',
                  template='none', color='paint_color')
    fig1.update_layout(title='Contagem de Veículos por Cor',
                       autosize=False, width=500, height=500)

    # exibir um gráfico ploply interativo
    st.plotly_chart(fig1, use_container_width=True)

if bar_button2:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um gráfico de barra para o conjunto de dados de anúncios de vendas de carros')

    # criar um grafico de barras
    car_data = car_data.value_counts()

    # redefinir o índice para garantir que não seja um MultiIndex
    car_data = car_data.reset_index(drop=True)

    # criar um grafico de barras
    fig2 = px.bar(car_data, barmode='group', text_auto=True)
    fig2.update_layout(title='Cores dos Carros',
                       autosize=False, width=500, height=500)

    # exibir um gráfico ploply interativo
    st.ploply_chart(fig2, use_container_width=True)
