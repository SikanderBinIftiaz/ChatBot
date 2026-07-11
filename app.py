"""
============================================================
AI FAQ Chatbot - Main Streamlit Application
CodeAlpha Internship Project

Main application controller
============================================================
"""


import os
import streamlit as st

from chatbot import FAQChatbot

from components.sidebar import render_sidebar
from components.header import render_header
from components.cards import render_dashboard_cards
from components.chat import render_chat_interface
from components.export import generate_export

from themes.theme import apply_theme

from utils.session import (
    initialize_session,
    clear_chat_history
)

from themes.theme import apply_theme
initialize_session()
apply_theme()

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)



# ============================================================
# LOAD CUSTOM CSS
# ============================================================

def load_css():

    css_file = "styles.css"

    if os.path.exists(css_file):

        with open(css_file, "r", encoding="utf-8") as file:

            st.markdown(
                f"""
                <style>
                {file.read()}
                </style>
                """,
                unsafe_allow_html=True
            )



load_css()



# ============================================================
# SESSION INITIALIZATION
# ============================================================

initialize_session()



# ============================================================
# APPLY THEME
# ============================================================

apply_theme()



# ============================================================
# LOAD CHATBOT ENGINE
# ============================================================

@st.cache_resource
def load_chatbot():

    return FAQChatbot()



chatbot = load_chatbot()



# ============================================================
# SIDEBAR
# ============================================================

sidebar_data = render_sidebar()



# ============================================================
# EXPORT HANDLING
# ============================================================

if sidebar_data.get("export") != "None":

    conversation = st.session_state.get("messages", [])

    if conversation:

        try:

            file_bytes, filename, mime_type = generate_export(
                conversation,
                sidebar_data["export"]
            )

            if file_bytes:

                with st.sidebar:

                    st.download_button(
                        label=f"⬇️ Download {sidebar_data['export']}",
                        data=file_bytes,
                        file_name=filename,
                        mime=mime_type,
                        use_container_width=True
                    )

        except Exception as exc:

            with st.sidebar:

                st.error(f"Export failed: {exc}")

    else:

        with st.sidebar:

            st.warning("No conversation to export yet.")



# ============================================================
# HEADER
# ============================================================

render_header()



# ============================================================
# DASHBOARD SECTION
# ============================================================

render_dashboard_cards()



st.divider()



# ============================================================
# CHAT SECTION
# ============================================================

render_chat_interface(
    chatbot=chatbot
)



# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div style="
        text-align:center;
        margin-top:40px;
        color:#94a3b8;
        font-size:14px;
    ">
    🚀 AI FAQ Chatbot |
    Built for CodeAlpha Internship |
    Powered by Python + Gemini AI
    </div>
    """,
    unsafe_allow_html=True
)