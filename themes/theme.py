"""
============================================================
AI FAQ Chatbot - Theme Manager

Handles Light/Dark Theme Styling
CodeAlpha Internship Project
============================================================
"""

from __future__ import annotations

import streamlit as st


# ============================================================
# THEME DEFINITIONS
# ============================================================

THEMES = {

    "🌙 Dark": {

        "background": "#0f172a",

        "secondary": "#1e293b",

        "card": "#1e293b",

        "border": "#334155",

        "text": "#f8fafc",

        "muted": "#94a3b8",

        "accent": "#6366f1",

        "success": "#22c55e",

        "user_chat": "#312e81",

        "bot_chat": "#1e293b",

    },

    "☀️ Light": {

        "background": "#ffffff",

        "secondary": "#f8fafc",

        "card": "#ffffff",

        "border": "#cbd5e1",

        "text": "#0f172a",

        "muted": "#64748b",

        "accent": "#4f46e5",

        "success": "#16a34a",

        "user_chat": "#dbeafe",

        "bot_chat": "#f1f5f9",

    }

}


DEFAULT_THEME = "🌙 Dark"


# ============================================================
# CURRENT THEME
# ============================================================

def current_theme():

    theme = st.session_state.get(
        "theme",
        DEFAULT_THEME
    )

    return THEMES.get(
        theme,
        THEMES[DEFAULT_THEME]
    )


# ============================================================
# APPLY THEME
# ============================================================

def apply_theme():

    colors = current_theme()

    st.markdown(

        f"""
<style>

/* ==========================================================
   APP
========================================================== */

.stApp {{

    background:{colors["background"]};
    color:{colors["text"]};

}}

/* ==========================================================
   SIDEBAR
========================================================== */

section[data-testid="stSidebar"] {{

    background:{colors["secondary"]};

    border-right:1px solid {colors["border"]};

}}

section[data-testid="stSidebar"] * {{

    color:{colors["text"]};

}}

/* ==========================================================
   CHAT
========================================================== */

div[data-testid="stChatMessage"] {{

    border-radius:16px;

    border:1px solid {colors["border"]};

    padding:10px;

    margin-bottom:10px;

}}

div[data-testid="stChatMessage"]:hover {{

    border-color:{colors["accent"]};

}}

/* ==========================================================
   BUTTONS
========================================================== */

.stButton>button {{

    width:100%;

    border-radius:10px;

    border:none;

    background:{colors["accent"]};

    color:white;

    font-weight:600;

}}

.stButton>button:hover {{

    opacity:0.92;

}}

/* ==========================================================
   INPUT
========================================================== */

.stTextInput input {{

    border-radius:12px;

}}

.stTextArea textarea {{

    border-radius:12px;

}}

textarea {{

    border-radius:12px;

}}

/* ==========================================================
   SELECTBOX
========================================================== */

div[data-baseweb="select"] > div {{

    border-radius:10px;

}}

/* ==========================================================
   CARDS
========================================================== */

.dashboard-card {{

    background:{colors["card"]};

    border:1px solid {colors["border"]};

    border-radius:16px;

    padding:18px;

    margin-bottom:12px;

}}

.dashboard-card-title {{

    color:{colors["muted"]};

    font-size:14px;

}}

.dashboard-card-value {{

    color:{colors["text"]};

    font-size:28px;

    font-weight:bold;

}}

/* ==========================================================
   METRIC
========================================================== */

div[data-testid="metric-container"] {{

    background:{colors["card"]};

    border-radius:14px;

    border:1px solid {colors["border"]};

    padding:12px;

}}

/* ==========================================================
   SCROLLBAR
========================================================== */

::-webkit-scrollbar {{

    width:8px;

}}

::-webkit-scrollbar-thumb {{

    background:{colors["accent"]};

    border-radius:20px;

}}

::-webkit-scrollbar-track {{

    background:transparent;

}}

</style>

""",

        unsafe_allow_html=True

    )