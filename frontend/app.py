import streamlit as st
import requests
from pathlib import Path

st.set_page_config(page_title="Answer Paper Evaluation System", layout="wide")

st.title("Answer Paper Evaluation System")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.info("Upload marking scheme and answer papers for automatic evaluation using AI")

with col2:
    st.warning("Ensure MongoDB is running at localhost:27017")

st.markdown("---")

if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload", "Evaluate", "Results"])

st.session_state.current_page = page

if page == "Home":
    st.markdown("""
    ## Welcome to the Answer Paper Evaluation System
    
    This system uses AI-powered RAG (Retrieval-Augmented Generation) to evaluate answer papers
    based on a marking scheme.
    
    ### Features:
    - Upload marking scheme (PDF/Image)
    - Upload up to 100 answer scripts
    - AI-powered evaluation with Gemini 3.1 Pro
    - Detailed results and feedback
    - MongoDB integration for data persistence
    
    ### Steps:
    1. Go to **Upload** and upload your marking scheme
    2. Upload your answer papers
    3. Go to **Evaluate** to start the evaluation process
    4. Check **Results** for detailed evaluation reports
    """)
    
elif page == "Upload":
    st.switch_page("pages/upload.py")
    
elif page == "Evaluate":
    st.switch_page("pages/evaluate.py")
    
elif page == "Results":
    st.switch_page("pages/results.py")
