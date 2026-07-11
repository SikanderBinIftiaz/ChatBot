import customtkinter as ctk
from datetime import datetime
import pyperclip

from theme import *


class ChatBubble(ctk.CTkFrame):

    def __init__(self, parent, message, sender="ai", copy_callback=None):

        super().__init__(
            parent,
            fg_color="transparent"
        )

        self.message = message
        self.sender = sender
        self.copy_callback = copy_callback

        if sender == "user":
            self.create_user()
        else:
            self.create_ai()

    # =====================================================
    # USER MESSAGE
    # =====================================================

    def create_user(self):

        wrapper = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        wrapper.pack(
            fill="x",
            padx=10,
            pady=8
        )

        bubble = ctk.CTkFrame(
            wrapper,
            fg_color=PRIMARY,
            corner_radius=18
        )

        bubble.pack(
            anchor="e",
            padx=(180, 0)
        )

        ctk.CTkLabel(
            bubble,
            text=self.message,
            wraplength=520,
            justify="left",
            text_color="white",
            font=(FONT, 15)
        ).pack(
            padx=18,
            pady=(14, 6)
        )

        ctk.CTkLabel(
            bubble,
            text=datetime.now().strftime("%H:%M"),
            text_color="#E5E7EB",
            font=(FONT, 11)
        ).pack(
            anchor="e",
            padx=14,
            pady=(0, 10)
        )

    # =====================================================
    # AI MESSAGE
    # =====================================================

    def create_ai(self):

        wrapper = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        wrapper.pack(
            fill="x",
            padx=10,
            pady=8
        )

        row = ctk.CTkFrame(
            wrapper,
            fg_color="transparent"
        )

        row.pack(
            anchor="w"
        )

        avatar = ctk.CTkLabel(
            row,
            text="🤖",
            font=(FONT, 22)
        )

        avatar.pack(
            side="left",
            padx=(0, 10),
            anchor="n"
        )

        bubble = ctk.CTkFrame(
            row,
            fg_color=CARD,
            corner_radius=18
        )

        bubble.pack(
            side="left"
        )

        ctk.CTkLabel(
            bubble,
            text=self.message,
            wraplength=650,
            justify="left",
            text_color=TEXT,
            font=(FONT, 15)
        ).pack(
            padx=18,
            pady=(14, 8)
        )

        footer = ctk.CTkFrame(
            bubble,
            fg_color="transparent"
        )

        footer.pack(
            fill="x",
            padx=12,
            pady=(0, 10)
        )

        ctk.CTkLabel(
            footer,
            text=datetime.now().strftime("%H:%M"),
            text_color=TEXT_SECONDARY,
            font=(FONT, 11)
        ).pack(
            side="left"
        )

        copy_btn = ctk.CTkButton(
            footer,
            text="📋 Copy",
            width=70,
            height=28,
            corner_radius=8,
            fg_color=BUTTON,
            hover_color=BUTTON_HOVER,
            font=(FONT, 11),
            command=self.copy_message
        )

        copy_btn.pack(
            side="right"
        )

    # =====================================================
    # COPY MESSAGE
    # =====================================================

    def copy_message(self):

        pyperclip.copy(self.message)

        if self.copy_callback:
            self.copy_callback()