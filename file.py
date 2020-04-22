import os

with open(os.path.join('/Users/cassiophilipe/Projetos/desafio_streamlit', 'Procfile'), "w") as file1:
    toFile = 'web: sh setup.sh && streamlit run analise.py'

file1.write(toFile)
