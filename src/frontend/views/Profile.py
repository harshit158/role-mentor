import streamlit as st

cols = st.columns([25, 50, 25])
with cols[1]:
    file = st.file_uploader("Upload your resume", type=["pdf"])
    if file:
        with st.popover("Resume preview", width="stretch"):
            st.pdf(file)