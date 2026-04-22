from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")


# -------------------------------------UI Setup---------------------------------------------------
st.set_page_config(page_title="AI Research Assistant", page_icon="🔬")
st.title('🔬 Smart Research Tool')
st.markdown("---")

st.sidebar.header("Pre-Loaded Papers")
papers_input = [
    "Select...", "Attention Is All You Need (Transformer Architecture)", "Generative Adversarial Networks (GANs)", "Gemini 1.5: Technical Report",
    "Sparks of Artificial General Intelligence (GPT-4 Study)"
]
selected_paper = st.sidebar.selectbox('Quick Research:', papers_input)
user_input = st.text_area('Enter your specific research query or topic:', placeholder="e.g., Explain the impact of Quantum Computing on Cybersecurity...")

style_input = st.selectbox('Select a writing style:', ["Professional", "Friendly", "Hinglish"])
length_input = st.selectbox('Select summary length:', ["Short (1-2 lines)", "Medium (5-7 lines)", "Long (8+ lines)"])
# -------------------------------------UI Setup---------------------------------------------------

#template
template = load_prompt('template.json')
#template


if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input': selected_paper if selected_paper != "Select..." else user_input,
        'style': style_input,
        'length': length_input
    })
    st.write(result.content)
    
# Working we are asking user input from dropdown after that we are filling the place holders in the template with the user inputs and then we are passing the filled template to the model and then we are showing the result on the screen.






# _______________________________________________________________________
# ************************************************************************
#                      STATIC PROMPT                                     
# _______________________________________________________________________
# ************************************************************************

# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import streamlit as st

# load_dotenv()
# model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# st.header('Research Tool')

# user_input = st.text_input('Enter your research query:')

# if st.button('Summarize'):
#     if user_input:
#         with st.spinner('Researching...'): # Yeh loading bar dikhayega
#             result = model.invoke(user_input)
            
#             if result.content:
#                 st.subheader("Results:")
#                 st.write(result.content)
#             else:
#                 st.error("No results found. Please try again.")
#     else:
#         st.warning("Please Enter a query.")