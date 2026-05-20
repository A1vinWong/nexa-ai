import streamlit as st

st.set_page_config(page_title="Nexa AI Studio", layout="wide")

st.title("⚡ NexaEdge AI Studio")

prompt = st.text_input("Describe what you want to create")

if st.button("Generate"):
    st.write("AI output will appear here")

