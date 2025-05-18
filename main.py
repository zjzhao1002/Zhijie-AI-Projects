import os
import streamlit as st
import pdg_query
import publications_rag
from dotenv import load_dotenv

load_dotenv()
if not os.getenv("GOOGLE_API_KEY"):
    st.error("Cannot find the GOOGLE_API_KEY")

st.set_page_config(
    page_title="Zhijie's AI Projects", page_icon=":scientist:", layout="centered"
)

st.title("Zhijie's AI Projects")
st.markdown("By this App, you can query the PDG Database or ask questions for Zhijie's publications")

question = st.text_input("Input your question here: ")

button1 = st.button("I want to query the PDG Database")
button2 = st.button("I am interested in Zhijie's publications")

if button1:
    try:
        answer = pdg_query.run_pdg_query(question)
        st.markdown("### AI's Response")
        st.markdown(answer)
    except Exception as e:
        st.error(f"An error occured: {str(e)}")

if button2:
    try:
        answer = publications_rag.run_pdf_rag(question)
        st.markdown("### AI's Response")
        st.markdown(answer)
    except Exception as e:
        st.error(f"An error occured: {str(e)}")