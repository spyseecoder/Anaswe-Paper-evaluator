import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Evaluate", layout="centered")
st.title("Evaluate Answer Papers")

st.markdown("---")

batch_id = st.text_input("Enter Batch ID", placeholder="Batch ID from upload")

if batch_id:
    if st.button("Start Evaluation", key="start_eval"):
        if "scheme_id" not in st.session_state:
            st.error("Please upload documents first!")
        else:
            with st.spinner("Starting evaluation..."):
                response = requests.post(
                    f"{API_BASE_URL}/api/evaluate/start",
                    params={"batch_id": batch_id, "scheme_id": st.session_state.scheme_id}
                )
                
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"Evaluation started! {data.get('message', '')}")
                    st.info(f"Total papers to evaluate: {data.get('total_scripts', 0)}")
                    st.info("Go to Results tab to view progress and results (auto-refresh every 5 seconds)")
                else:
                    st.error(f"Error: {response.text}")
