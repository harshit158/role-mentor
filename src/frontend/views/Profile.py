import streamlit as st
import time

cols = st.columns([25, 50, 25])
with cols[1]:
    file = st.file_uploader("Upload your resume", type=["pdf"])
    if file:
        with st.spinner("Parsing your resume..."):
            time.sleep(5)