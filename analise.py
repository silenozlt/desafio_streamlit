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
        st.markdown('Conhecendo as colunas do dataset :')
        st.write(df.columns)
        st.markdown('Verificando a quantidade de linhas :')
        st.write(len(df))




    if file is None:
        st.warning("Ocorreu algum erro !")

    if st.button('Like'):
        st.write('Obrigado pela visita')
    else:
        st.warning('This is a warning')


if __name__ == '__main__':
    main()
