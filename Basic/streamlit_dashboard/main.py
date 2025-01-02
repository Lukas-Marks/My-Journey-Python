import streamlit as st 
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar: 
    st.title("Analise de Lucro")
    
    uploaded_file = st.file_uploader("Coloque seu arquivo aqui")
    
if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    
    with st.sidebar:
        
        district_regions = df["Region"].unique().tolist()
        
        region_selected = st.selectbox("Região Especifica", district_regions)
        
        seller_selected = st.radio("Prioridade", ["H","C", "M", "L"], index=None)
        
        if region_selected:
            df = df[df["Region"] == region_selected]
            
        if seller_selected:
            df = df[df["Order Priority"] == seller_selected]
            
    st.write("Lucro por tipo de item")
        
    st.bar_chart(df, x="Item Type", y="Total Profit")
        
    st.dataframe(df, use_container_width=True)    