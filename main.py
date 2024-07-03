import streamlit as st
from app import get_few_shot_db_chain

# Set the page configuration
st.set_page_config(
    page_title="Inventory Management",
    page_icon=":tshirt:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Set custom CSS to enhance visual appearance
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
    </style>
    """, unsafe_allow_html=True)

# App title and description
st.title("🛍️ Inventory Management System")
st.write("Welcome to the Inventory Management System! Ask any question regarding the inventory, and get the answer instantly.")

# Input box for user question
question = st.text_input("Enter your question below:")

# Process the question and display the answer
if question:
    chain = get_few_shot_db_chain()
    with st.spinner("Fetching the answer..."):
        response = chain.run(question)
    
    st.header("Answer")
    st.success(response)
