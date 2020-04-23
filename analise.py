import streamlit as st
import pandas as pd
import base64

def main():
    st.title('Analisando Dados')
    st.image('imagens/python.png')
    file = st.file_uploader('Choose your file :', type = 'csv')
    if file is not None:
        st.markdown('Selecione a quantidade de linhas para visualizar: ')
        slider = st.slider('Valores', 1, 1000)
        df = pd.read_csv(file)
        st.dataframe(df.head(slider))
        #st.markdown('Tabela')
        #st.table(df.head(slider))
        st.markdown('As colunas existentes no dataset :')
        st.write(df.columns)



if __name__ == '__main__':
    main()
