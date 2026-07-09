"""
chat_bubble.py
-----------------------------------
Modern Chat Bubble Widget
"""

import customtkinter as ctk
from themes import COLORS, FONTS, CHAT


class ChatBubble(ctk.CTkFrame):

    def __init__(
        self,
        master,
        message,
        sender="bot",
        timestamp=""
    ):
        super().__init__(
            master,
            fg_color="transparent"
        )

        self.sender = sender

        # -------------------------
        # Alignment
        # -------------------------

        if sender == "user":

            bubble_color = COLORS["user_bubble"]
            anchor = "e"
            emoji = "👤"

        else:

            bubble_color = COLORS["bot_bubble"]
            anchor = "w"
            emoji = "🤖"

        # -------------------------
        # Bubble
        # -------------------------

        bubble = ctk.CTkFrame(
            self,
            fg_color=bubble_color,
            corner_radius=CHAT["bubble_radius"]
        )

        bubble.pack(
            anchor=anchor,
            padx=20,
            pady=8
        )

        # -------------------------
        # Message
        # -------------------------

        message_label = ctk.CTkLabel(
            bubble,
            text=f"{emoji}  {message}",
            justify="left",
            wraplength=CHAT["wrap_length"],
            font=FONTS["chat"],
            text_color=COLORS["text"]
        )

        message_label.pack(
            padx=18,
            pady=(12, 6)
        )

        # -------------------------
        # Timestamp
        # -------------------------

        time_label = ctk.CTkLabel(
            bubble,
            text=timestamp,
            font=FONTS["tiny"],
            text_color=COLORS["secondary_text"]
        )

        time_label.pack(
            anchor="e",
            padx=15,
            pady=(0, 8)
        )

    # ---------------------------------

    def update_message(self, message):
        """
        Future support for typing animation.
        """
        for widget in self.winfo_children():

            if isinstance(widget, ctk.CTkFrame):

                for child in widget.winfo_children():

                    if isinstance(child, ctk.CTkLabel):

                        child.configure(text=message)

                        return