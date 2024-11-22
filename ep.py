# -*- coding: utf-8 -*-
"""
Created on  21/11/2024

@author: nereu


def page2():
    st.title("Second page")

pg = st.navigation([
    st.Page("teste.py", title="Emendas Parlamentares - Portal Transparencia", icon="🔥"),
    st.Page(page2, title="Second page", icon=":material/favorite:"),
])
pg.run()


"""
import pandas as pd
import streamlit as st
import numpy as np

link_dados_em_parlamentar = 'https://portaldatransparencia.gov.br/download-de-dados/emendas-parlamentares/EmendasParlamentares.zip'

df = pd.read_csv(link_dados_em_parlamentar,
                sep=";",
                low_memory=False,
                encoding ='latin-1',
                decimal=',') # informa decimal como

df['Ano da Emenda'] = df['Ano da Emenda'].astype(str)


autores = list(df['Nome do Autor da Emenda'].unique())
anos = list(df['Ano da Emenda'].unique())
localidades = list(df['Localidade do gasto'].unique())
funcoes = list(df['Nome Função'].unique())
subfuncoes = list(df['Nome Subfunção'].unique())

st.title("portaldatransparencia.gov.br - :blue[Emendas Parlamentares] :sunglasses:" )
#st.info('portaldatransparencia.gov.br - Emendas Parlamentares', icon="ℹ️")
# st.warning('This is a warning', icon="⚠️")

#e = RuntimeError("This is an exception of type RuntimeError")
#st.exception(e)

# st.snow()
autor = st.sidebar.selectbox('Escolha o Autor',['Todos'] + autores)
ano = st.sidebar.selectbox('Escolha o Ano',['Todos'] + anos)
local = st.sidebar.selectbox('Escolha a localidade',['Todas'] + localidades)
funcao = st.sidebar.selectbox('Escolha a Função',['Todas'] + funcoes)
subfuncao = st.sidebar.selectbox('Escolha a Subfunção',['Todas'] + subfuncoes)


if (autor != 'Todos'):
    st.subheader('Mostrando Resultado para ' + autor)
    df = df[df['Nome do Autor da Emenda']== autor]
else: st.text('Mostrando todos Autores')


if (ano != 'Todos'):
    st.subheader('Mostrando Resultado para ' + ano)
    df = df[df['Ano da Emenda']== ano]
else: st.text('Mostrando todos os Anos')


if (local != 'Todas'):
    st.subheader('Mostrando Resultado para ' + local)
    df = df[df['Localidade do gasto']== local]
else: st.text('Mostrando todas Localidades')


if (funcao != 'Todas'):
    st.subheader('Mostrando Resultado para ' + funcao)
    df = df[df['Nome Função']== funcao]
else: st.text('Mostrando todas Funções')


if (subfuncao != 'Todas'):
    st.subheader('Mostrando Resultado para ' + subfuncao)
    df = df[df['Nome Subfunção']== subfuncao]
else: st.text('Mostrando todas Subfunções')


# st.df(data=None, width=None, height=None, use_container_width=False, hide_index=None, column_order=None, column_config=None, key=None, on_select="rerun", selection_mode="multi-row")

st.dataframe(df, hide_index=True)

st.sidebar.success('Carregado com Sucesso!', icon="✅")

st.sidebar.html(
    "<p><span style='text-decoration: underline underline;'>@ Nereu - </span> 11/2024.</p>"
)

# source venv/bin/activate
# streamlit run app.py
# streamlit run c:\users\nereu\.spyder-py3\projetos\p1\teste.py