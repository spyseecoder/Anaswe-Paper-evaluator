import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Upload", layout="centered")
st.title("Upload Documents")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Marking Scheme")
    marking_scheme_file = st.file_uploader("Upload Marking Scheme (PDF/Image)", type=["pdf", "png", "jpg", "jpeg"])
    
    if marking_scheme_file:
        st.success("Marking scheme selected")
        if st.button("Upload Marking Scheme", key="upload_scheme"):
            with st.spinner("Uploading..."):
                files = {"file": marking_scheme_file}
                response = requests.post(f"{API_BASE_URL}/api/upload/marking-scheme", files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    st.session_state.scheme_id = result["scheme_id"]
                    st.success(f"Uploaded! Scheme ID: {st.session_state.scheme_id}")
                else:
                    st.error(f"Upload failed: {response.text}")

with col2:
    st.subheader("Answer Scripts")
    answer_scripts = st.file_uploader("Upload Answer Scripts (PDF/Image)", type=["pdf", "png", "jpg", "jpeg"], accept_multiple_files=True)
    
    if answer_scripts:
        st.info(f"{len(answer_scripts)} file(s) selected")
        
        if st.button("Upload Answer Scripts", key="upload_scripts"):
            if "scheme_id" not in st.session_state:
                st.error("Please upload marking scheme first!")
            else:
                with st.spinner("Uploading..."):
                    files = [("files", file) for file in answer_scripts]
                    params = {"scheme_id": st.session_state.scheme_id}
                    response = requests.post(f"{API_BASE_URL}/api/upload/answer-scripts", files=files, params=params)
                    
                    if response.status_code == 200:
                        result = response.json()
                        st.session_state.batch_id = result["batch_id"]
                        st.success(f"Uploaded! Batch ID: {st.session_state.batch_id}")
                    else:
                        st.error(f"Upload failed: {response.text}")
