import customtkinter as ctk

from theme import *


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            width=260,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.pack_propagate(False)

        # ==========================
        # Logo
        # ==========================

        self.logo = ctk.CTkLabel(

            self,

            text="🤖",

            font=(FONT, 52)

        )

        self.logo.pack(
            pady=(35, 5)
        )

        self.title = ctk.CTkLabel(

            self,

            text="AI Assistant",

            font=(FONT, 24, "bold"),

            text_color=TEXT

        )

        self.title.pack()

        self.subtitle = ctk.CTkLabel(

            self,

            text="Powered by Gemini",

            font=(FONT, 13),

            text_color=TEXT_SECONDARY

        )

        self.subtitle.pack(
            pady=(0, 25)
        )

        # ==========================
        # Buttons
        # ==========================

        self.new_chat = self.create_button(
            "➕  New Chat"
        )

        self.history = self.create_button(
            "🕘  History"
        )

        self.stats = self.create_button(
            "📊  Statistics"
        )

        self.settings = self.create_button(
            "⚙  Settings"
        )

        self.export = self.create_button(
            "📄  Export Chat"
        )

        # ==========================
        # Bottom Info
        # ==========================

        ctk.CTkLabel(

            self,

            text="Gemini 2.5 Flash",

            text_color=SUCCESS,

            font=(FONT, 12)

        ).pack(side="bottom", pady=5)

        ctk.CTkLabel(

            self,

            text="Version 2.0",

            text_color=TEXT_SECONDARY,

            font=(FONT, 11)

        ).pack(side="bottom")



    def create_button(self, text):

        btn = ctk.CTkButton(

            self,

            text=text,

            height=45,

            corner_radius=12,

            fg_color=CARD,

            hover_color=PRIMARY,

            anchor="w",

            font=(FONT, 15)

        )

        btn.pack(
            fill="x",
            padx=18,
            pady=7
        )

        return btn