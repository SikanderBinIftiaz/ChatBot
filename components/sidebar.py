"""
============================================================
AI FAQ Chatbot - Sidebar Component

Professional ChatGPT-style sidebar
============================================================
"""


import streamlit as st

from utils.session import clear_chat_history



# ============================================================
# SIDEBAR RENDER FUNCTION
# ============================================================


def render_sidebar():

    sidebar_state = {}



    with st.sidebar:



        # ----------------------------------------------------
        # BRAND HEADER
        # ----------------------------------------------------

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:15px;
            ">

            <h1 style="
                font-size:28px;
                margin-bottom:5px;
            ">
            🤖 AI FAQ
            </h1>

            <p style="
                color:#94a3b8;
                font-size:14px;
            ">
            Intelligent Assistant
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )



        st.divider()



        # ----------------------------------------------------
        # NEW CHAT
        # ----------------------------------------------------

        st.subheader("💬 Chat")


        if st.button(
            "➕ New Conversation",
            use_container_width=True
        ):

            clear_chat_history()

            st.rerun()



        st.divider()



        # ----------------------------------------------------
        # CHAT SETTINGS
        # ----------------------------------------------------

        st.subheader("⚙️ Preferences")



        theme_options = [
            "🌙 Dark",
            "☀️ Light"
        ]


        current_theme = st.session_state.get(
            "theme",
            theme_options[0]
        )


        if current_theme not in theme_options:
            current_theme = theme_options[0]


        current_index = theme_options.index(current_theme)


        theme = st.selectbox(
            "Theme",
            theme_options,
            index=current_index
        )


        if theme != st.session_state.get("theme"):

            st.session_state.theme = theme

            st.rerun()


        sidebar_state["theme"] = theme



        st.divider()



        # ----------------------------------------------------
        # FILE UPLOAD
        # ----------------------------------------------------

        st.subheader("📂 Upload Files")


        uploaded_file = st.file_uploader(
            "Upload document",
            type=[
                "txt",
                "pdf",
                "json",
                "csv"
            ]
        )


        sidebar_state["uploaded_file"] = uploaded_file



        st.divider()



        # ----------------------------------------------------
        # TOOLS
        # ----------------------------------------------------

        st.subheader("🛠 Tools")



        export_option = st.selectbox(
            "Export Chat",
            [
                "None",
                "TXT",
                "PDF",
                "JSON"
            ]
        )


        sidebar_state["export"] = export_option



        st.divider()



        # ----------------------------------------------------
        # ANALYTICS CARD
        # ----------------------------------------------------

        st.subheader("📊 Analytics")


        message_count = len(
            st.session_state.get(
                "messages",
                []
            )
        )


        st.markdown(
            f"""
            <div class="dashboard-card">

            <div class="dashboard-card-title">
            Messages
            </div>

            <div class="dashboard-card-value">
            {message_count}
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )



        st.divider()



        # ----------------------------------------------------
        # ABOUT
        # ----------------------------------------------------

        st.markdown(
            """
            <div style="
                text-align:center;
                color:#94a3b8;
                font-size:12px;
            ">

            <b>AI FAQ Chatbot</b><br>

            CodeAlpha Internship Project<br>

            Python • Streamlit • Gemini AI

            </div>
            """,
            unsafe_allow_html=True
        )



    return sidebar_state