import streamlit as st
import pandas as pd
import base64
# import matplotlib.pyplot as plt
import seaborn as sns


def main():
    st.title('Analisando Dados')
    st.image('imagens/python.png')
    file = st.file_uploader('Choose your file :', type='csv')
    if file is not None:
        st.success('Carregado com sucesso !')
        st.markdown('Selecione a quantidade de linhas para visualizar: ')
        slider = st.slider('Valores', 1, 1000)
        df = pd.read_csv(file)
        # st.dataframe(df.head(slider))
        # st.markdown('Dados apresenteados formato tabela')
        st.table(df.head(slider))


        # AQUI TUDO QUE FOR FICAR DENTRO DO SIDEBAR
        st.sidebar.subheader('Selecione como conhecer os dados:')
        linhas = st.sidebar.checkbox('Linhas do dataset : ')
        if linhas is not False:
            st.markdown('Quantidade de linhas: ')
            st.write(len(df))
        colunas = st.sidebar.checkbox('Colunas : ')
        if colunas is not False:
            st.markdown('Conhecendo as colunas do dataset :')
            st.write(df.columns)

    if st.sidebar.button('Like'):
        st.write('Obrigado pela visita')
    #else:
    #   st.sidebar.warning('This is a warning')


if __name__ == '__main__':
    main()
