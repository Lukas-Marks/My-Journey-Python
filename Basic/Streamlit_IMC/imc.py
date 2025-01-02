import streamlit as st 

with st.sidebar:
    st.title("Calculadora IMC")
    
    st.header("IMC: definicao:")
    
    st.write("Indice de massa corporal - IMC")
    
    st.write("É o indice que relaciona o peso e altura")
    
st.title("Calculadora")

peso = st.number_input(label="Digite o Seu peso em kg", min_value=0.0)

altura = st.number_input(label="Digite sua Altura em Metros", min_value=0.0)

if st.button("Calcular"):
    
    imc = peso / (altura ** 2)
    
    st.write(f"Seu IMC é: {imc}")