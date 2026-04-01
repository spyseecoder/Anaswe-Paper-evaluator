import streamlit as st
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Results", layout="wide")
st.title("Evaluation Results")

st.markdown("---")

batch_id = st.text_input("Enter Batch ID to view results", placeholder="Batch ID from evaluation")

if batch_id:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        fetch_button = st.button("Fetch Results", key="fetch_results")
    
    with col2:
        auto_refresh = st.checkbox("Auto-refresh (5s)", value=False)
    
    if fetch_button or auto_refresh:
        placeholder = st.empty()
        
        while True:
            with placeholder.container():
                with st.spinner("Fetching results..."):
                    # Get batch summary
                    summary_response = requests.get(f"{API_BASE_URL}/api/results/summary/{batch_id}")
                    
                    if summary_response.status_code == 200:
                        summary_data = summary_response.json()
                        batch = summary_data
                        
                        st.success("Results loaded!")
                        
                        # Display metrics
                        col1, col2, col3, col4 = st.columns(4)
                        with col1:
                            st.metric("Total Scripts", batch.get("total_scripts", 0))
                        with col2:
                            st.metric("Evaluated", batch.get("evaluated_scripts", 0))
                        with col3:
                            st.metric("Status", batch.get("evaluation_status", "pending"))
                        with col4:
                            progress = batch.get("evaluated_scripts", 0) / max(batch.get("total_scripts", 1), 1)
                            st.metric("Progress", f"{progress*100:.1f}%")
                        
                        # Progress bar
                        progress = batch.get("evaluated_scripts", 0) / max(batch.get("total_scripts", 1), 1)
                        st.progress(progress)
                        
                        st.markdown("---")
                        
                        # Get detailed evaluations
                        eval_response = requests.get(f"{API_BASE_URL}/api/results/evaluations/{batch_id}")
                        
                        if eval_response.status_code == 200:
                            eval_data = eval_response.json()
                            evaluations = eval_data.get("evaluations", [])
                            
                            if evaluations:
                                st.subheader(f"Evaluations ({len(evaluations)})")
                                for idx, eval_item in enumerate(evaluations, 1):
                                    with st.expander(f"Paper {idx}: {eval_item.get('script_name', 'Unknown')}"):
                                        result = eval_item.get("result", {})
                                        
                                        col1, col2, col3 = st.columns(3)
                                        with col1:
                                            st.metric("Score", f"{result.get('score', 0)}/{result.get('max_score', 100)}")
                                        with col2:
                                            st.metric("Percentage", f"{result.get('percentage', 0):.1f}%")
                                        with col3:
                                            st.metric("Confidence", f"{result.get('confidence_score', 0):.2f}")
                                        
                                        st.write("Feedback:", result.get("feedback", "No feedback"))
                            else:
                                st.info("No evaluations yet. Check back in a moment...")
                    else:
                        st.error(f"Error: {summary_response.text}")
                        break
            
            if not auto_refresh:
                break
            
            time.sleep(5)  # Auto-refresh every 5 seconds
