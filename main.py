import streamlit as st
from langchain_core.messages import HumanMessage
from graph import graph

# ===== Streamlit UI =====

st.set_page_config(page_title="Lista della Spesa AI", page_icon="🛍️")
st.title("🛒 Lista della Spesa con Agente AI")

user_input = st.text_input("Cosa vuoi fare?", placeholder="Es: aggiungi pasta, rimuovi latte, mostra lista")

if st.button("Invia") and user_input:
    with st.spinner("Sto pensando..."):
        result = graph.invoke({"messages": [HumanMessage(content=user_input)]})
        output = result["messages"][-1].content
        st.success(output)
