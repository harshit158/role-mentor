import streamlit as st
import sys
import streamlit.web.cli as stcli
from src.frontend import utils
from src.models import Message

st.set_page_config(layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []

utils.display_logo_in_center()
st.divider()

pg = st.navigation(["views/Profile.py",
                    "views/Home.py"])

pg.run()

def main():
    sys.argv = ["streamlit", "run", "src/frontend/app.py"]
    sys.exit(stcli.main())