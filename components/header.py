"""
============================================================
AI FAQ Chatbot - Header Component
============================================================
"""

import streamlit as st


def render_header():

    st.markdown(
        """
        <div style="
            background:linear-gradient(135deg,#312e81,#1e293b);
            padding:35px;
            border-radius:20px;
            color:white;
            margin-bottom:20px;
        ">

            <div style="
                display:flex;
                align-items:center;
                gap:20px;
            ">

                <div style="
                    font-size:60px;
                ">
                    🤖
                </div>


                <div>

                    <h1 style="
                        margin:0;
                        font-size:42px;
                    ">
                        AI FAQ Chatbot
                    </h1>


                    <p style="
                        color:#cbd5e1;
                        font-size:18px;
                    ">
                        Your intelligent assistant powered by Python + Gemini AI
                    </p>

                </div>

            </div>


            <br>


            <span style="
                background:#166534;
                padding:8px 15px;
                border-radius:20px;
                margin-right:10px;
            ">
                🟢 AI Online
            </span>


            <span style="
                background:#3730a3;
                padding:8px 15px;
                border-radius:20px;
                margin-right:10px;
            ">
                ✨ Smart FAQ Matching
            </span>


            <span style="
                background:#0369a1;
                padding:8px 15px;
                border-radius:20px;
            ">
                🚀 Gemini Powered
            </span>


        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        <p style="
            text-align:center;
            color:#94a3b8;
            font-size:15px;
        ">
        Ask questions, get intelligent answers,
        upload documents, and interact with your AI assistant.
        </p>
        """,
        unsafe_allow_html=True
    )