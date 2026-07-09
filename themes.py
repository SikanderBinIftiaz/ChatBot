"""
themes.py
------------------------
Theme configuration for AI FAQ Assistant
"""

import customtkinter as ctk


# ----------------------------------------------------
# Appearance
# ----------------------------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ----------------------------------------------------
# Colors
# ----------------------------------------------------

COLORS = {

    "background": "#1E1E1E",

    "sidebar": "#181818",

    "header": "#202123",

    "chat_bg": "#212121",

    "user_bubble": "#2563EB",

    "bot_bubble": "#2D2D2D",

    "text": "#FFFFFF",

    "secondary_text": "#BDBDBD",

    "success": "#16A34A",

    "warning": "#F59E0B",

    "danger": "#DC2626",

    "border": "#3B3B3B",

    "entry": "#2A2A2A"

}


# ----------------------------------------------------
# Fonts
# ----------------------------------------------------

FONTS = {

    "title": ("Segoe UI", 28, "bold"),

    "heading": ("Segoe UI", 20, "bold"),

    "normal": ("Segoe UI", 15),

    "small": ("Segoe UI", 12),

    "tiny": ("Segoe UI", 10),

    "chat": ("Segoe UI", 15)

}


# ----------------------------------------------------
# Bubble Sizes
# ----------------------------------------------------

CHAT = {

    "bubble_radius": 18,

    "wrap_length": 520,

    "padding_x": 15,

    "padding_y": 10

}


# ----------------------------------------------------
# Window
# ----------------------------------------------------

WINDOW = {

    "width": 1300,

    "height": 760,

    "min_width": 1100,

    "min_height": 650

}


# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

SIDEBAR = {

    "width": 250

}