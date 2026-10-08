import streamlit as st

st.title('CALCULADORA DE MÉDIA')


nota1 = st.number_input('nota 1', value = 0.0)
nota2 = st.number_input('nota 2', value = 0.0)
nota3 = st.number_input('nota 3', value = 0.0)

media = (nota1 + nota2 + nota3) /3

if st.button('calcular'):
    st.write(media)
