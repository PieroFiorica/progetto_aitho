import streamlit as st
from langchain_core.messages import HumanMessage
from graph import graph

st.set_page_config(page_title="Lista della Spesa AI", page_icon="🛍️")
st.title("🛒 Lista della Spesa con Agente AI")

user_input = st.text_input("Cosa vuoi fare?", placeholder="Es: aggiungi pasta, rimuovi latte")

col1, col2 = st.columns([3, 1])

with col1:
    if st.button("Invia") and user_input:
        with st.spinner("Sto pensando..."):
            result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
            st.success(result["messages"][-1].content)

with col2:
    if st.button("📋 Visualizza Lista"):
        with st.spinner("Sto recuperando la lista..."):
            result = graph.invoke({"messages": [HumanMessage(content="mostra la lista")]})
            st.info(result["messages"][-1].content)
