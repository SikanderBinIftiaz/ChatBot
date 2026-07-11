import json
import streamlit as st


# ============================================================
# DASHBOARD CARDS
# ============================================================

def render_dashboard_cards():

    messages = st.session_state.get(
        "messages",
        []
    )


    user_messages = len(
        [
            msg for msg in messages
            if msg.get("role") == "user"
        ]
    )


    ai_messages = len(
        [
            msg for msg in messages
            if msg.get("role") == "assistant"
        ]
    )


    faq_count = 0


    try:

        with open(
            "faq_data.json",
            "r",
            encoding="utf-8"
        ) as file:

            faq_data = json.load(file)


            if isinstance(faq_data, list):

                faq_count = len(
                    faq_data
                )


            elif isinstance(faq_data, dict):

                faq_count = len(
                    faq_data.keys()
                )


    except Exception:

        faq_count = 0



    col1, col2, col3, col4 = st.columns(4)



    cards = [

        {
            "column": col1,
            "title": "💬 Questions",
            "value": user_messages
        },

        {
            "column": col2,
            "title": "🤖 AI Responses",
            "value": ai_messages
        },

        {
            "column": col3,
            "title": "📚 FAQ Knowledge",
            "value": faq_count
        },

        {
            "column": col4,
            "title": "⚡ Status",
            "value": "Online"
        }

    ]



    for card in cards:

        with card["column"]:

            st.markdown(
                f"""
                <div class="dashboard-card">

                    <div class="dashboard-card-title">
                        {card["title"]}
                    </div>

                    <div class="dashboard-card-value">
                        {card["value"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )



    st.write("")



    st.markdown(
        """
        <div style="
            text-align:center;
            color:#94a3b8;
            font-size:13px;
            margin-top:10px;
        ">

        📈 Real-time chatbot activity monitoring

        </div>
        """,
        unsafe_allow_html=True
    )