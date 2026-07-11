"""
============================================================
AI FAQ Chatbot - Chat Interface Component
CodeAlpha Internship Project
============================================================
"""

import time
import html
from datetime import datetime

import streamlit as st
import streamlit.components.v1 as components

from utils.session import (
    add_message,
    save_question,
    save_response,
    save_feedback,
    clear_chat_history,
    get_chat_history
)


USER_AVATAR = "🧑"
AI_AVATAR = "🤖"


def _now():
    return datetime.now().strftime("%I:%M %p")


def _new_id():
    return f"msg-{time.time_ns()}"


def _safe_get_answer(chatbot, question):

    try:
        answer, confidence = chatbot.get_answer(question)

        if not answer:
            return "Sorry, I could not find an answer.", 0.0

        return answer, confidence

    except Exception as e:

        return (
            f"⚠️ Error generating response: {str(e)}",
            0.0
        )


def _stream_words(text, placeholder):

    words = text.split()

    output = ""

    for word in words:

        output += word + " "

        placeholder.markdown(output + "▌")

        time.sleep(0.03)

    placeholder.markdown(output)


def _render_typing_indicator(placeholder):

    for dots in [".", "..", "..."]:

        placeholder.markdown(
            f"*AI typing{dots}*"
        )

        time.sleep(0.2)


def _render_confidence_badge(confidence):

    try:

        value = float(confidence) * 100

        st.caption(
            f"🤖 Confidence: {value:.1f}%"
        )

    except:

        pass


def _render_copy_button(message_id, content):

    safe_text = html.escape(content)

    components.html(
        f"""
        <button onclick="
        navigator.clipboard.writeText(`{safe_text}`)
        ">
        📋 Copy
        </button>
        """,
        height=40
    )


def _render_feedback_controls(message_id):

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "👍",
            key=f"like_{message_id}"
        ):

            save_feedback(
                message_id,
                "like"
            )


    with col2:

        if st.button(
            "👎",
            key=f"dislike_{message_id}"
        ):

            save_feedback(
                message_id,
                "dislike"
            )


def _render_message(message):

    role = message.get(
        "role",
        "assistant"
    )

    content = message.get(
        "content",
        ""
    )

    avatar = (
        USER_AVATAR
        if role == "user"
        else AI_AVATAR
    )


    with st.chat_message(
        role,
        avatar=avatar
    ):

        st.markdown(content)

        if message.get("timestamp"):
            st.caption(
                message["timestamp"]
            )

        if role == "assistant":

            if message.get("confidence"):
                _render_confidence_badge(
                    message["confidence"]
                )

            if message.get("id"):

                _render_copy_button(
                    message["id"],
                    content
                )

                _render_feedback_controls(
                    message["id"]
                )



def _handle_user_input(user_input, chatbot):

    add_message(
        "user",
        user_input
    )

    save_question(
        user_input
    )

    st.session_state.messages[-1]["timestamp"] = _now()
    st.session_state.messages[-1]["id"] = _new_id()


    answer, confidence = _safe_get_answer(
        chatbot,
        user_input
    )


    add_message(
        "assistant",
        answer
    )

    save_response(
        answer
    )


    st.session_state.messages[-1]["timestamp"] = _now()

    st.session_state.messages[-1]["confidence"] = confidence

    st.session_state.messages[-1]["id"] = _new_id()



def render_chat_history(chatbot=None):

    for message in get_chat_history():

        _render_message(
            message
        )



def render_chat_input(chatbot):

    user_input = st.chat_input(
        "Ask me anything..."
    )


    if user_input:

        _handle_user_input(
            user_input,
            chatbot
        )

        st.rerun()



def render_chat_interface(chatbot):

    st.markdown(
        "### 💬 Chat"
    )


    if st.button(
        "🗑️ Clear Conversation"
    ):

        clear_chat_history()

        st.rerun()



    render_chat_history(
        chatbot
    )


    render_chat_input(
        chatbot
    )