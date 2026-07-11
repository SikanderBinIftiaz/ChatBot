import streamlit as st


# ============================================================
# INITIALIZE SESSION
# ============================================================

def initialize_session():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "theme" not in st.session_state:
        st.session_state.theme = "🌙 Dark"

    if "total_questions" not in st.session_state:
        st.session_state.total_questions = 0

    if "total_responses" not in st.session_state:
        st.session_state.total_responses = 0

    if "feedback" not in st.session_state:
        st.session_state.feedback = {}

    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []

    if "last_question" not in st.session_state:
        st.session_state.last_question = ""

    if "last_response" not in st.session_state:
        st.session_state.last_response = ""


# ============================================================
# ADD MESSAGE
# ============================================================

def add_message(role, content):

    st.session_state.messages.append(
        {
            "role": role,
            "content": content
        }
    )


# ============================================================
# CLEAR CHAT HISTORY
# ============================================================

def clear_chat_history():

    st.session_state.messages = []

    st.session_state.total_questions = 0

    st.session_state.total_responses = 0

    st.session_state.last_question = ""

    st.session_state.last_response = ""

    st.session_state.feedback = {}


# ============================================================
# SAVE QUESTION
# ============================================================

def save_question(question):

    st.session_state.last_question = question

    st.session_state.total_questions += 1


# ============================================================
# SAVE RESPONSE
# ============================================================

def save_response(response):

    st.session_state.last_response = response

    st.session_state.total_responses += 1


# ============================================================
# SAVE FEEDBACK
# ============================================================

def save_feedback(message_id, feedback):

    if "feedback" not in st.session_state:
        st.session_state.feedback = {}

    st.session_state.feedback[message_id] = feedback


# ============================================================
# GET CHAT HISTORY
# ============================================================

def get_chat_history():

    return st.session_state.get(
        "messages",
        []
    )