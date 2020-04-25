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
            st.markdown('Conhecendo as colunas do Dataset :')
            st.write(df.columns)

        tips_var = st.sidebar.checkbox('Tipo de variaveis no Dataset')
        if tips_var is not False:
            st.markdown('Tipos de variaveis :')
            st.write(df.dtypes)

        descricao = st.sidebar.checkbox('Descrição do dataset :')
        if descricao is not False:
            st.markdown('Describe :')
            st.write(df.describe())

        desvio_padrao = st.sidebar.checkbox('Descrição de variaveis :')
        if desvio_padrao is not False:
            st.markdown('Descrive :')
            selecao = st.multiselect('Selecione a(s) variaveis : ', list(df.columns))
            st.write(df[selecao].describe())


    if st.sidebar.button('Contatos'):
        st.write('GitHub: https://github.com/silenozlt')
        st.write(('linkedin : https://www.linkedin.com/in/cassio-placido-4a950261/'))
    else:
        st.text(' ')


if __name__ == '__main__':
    main()
