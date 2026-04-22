from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.header('Research Tool')

user_input = st.text_input('Enter your research query:')

if st.button('Summarize'):
    if user_input:
        with st.spinner('Researching...'): # Yeh loading bar dikhayega
            result = model.invoke(user_input)
            
            if result.content:
                st.subheader("Results:")
                st.write(result.content)
            else:
                st.error("No results found. Please try again.")
    else:
        st.warning("Pehle kuch query toh likho bhai!")