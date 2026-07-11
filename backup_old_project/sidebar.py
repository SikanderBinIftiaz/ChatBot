import customtkinter as ctk

from theme import *


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            width=SIDEBAR_WIDTH,
            fg_color=SIDEBAR,
            corner_radius=0
        )

        self.parent = parent

        self.grid_propagate(False)

        # =======================================
        # Logo
        # =======================================

        logo = ctk.CTkLabel(
            self,
            text="🤖",
            font=(FONT, 42)
        )

        logo.pack(
            pady=(30, 5)
        )

        title = ctk.CTkLabel(
            self,
            text="AI Assistant",
            font=(FONT, 24, "bold"),
            text_color=TEXT
        )

        title.pack()

        subtitle = ctk.CTkLabel(
            self,
            text="Gemini 2.5 Flash",
            font=(FONT, 12),
            text_color=TEXT_SECONDARY
        )

        subtitle.pack(
            pady=(0, 30)
        )

        # =======================================
        # Buttons
        # =======================================

        self.create_button(
            "➕  New Chat",
            self.parent.new_chat
        )

        self.create_button(
            "🕘  History",
            self.parent.show_history
        )

        self.create_button(
            "📊  Statistics",
            self.parent.show_statistics
        )

        self.create_button(
            "📄  Export Chat",
            self.parent.export_chat
        )

        self.create_button(
            "⚙  Settings",
            self.parent.open_settings
        )

        # Spacer

        ctk.CTkLabel(
            self,
            text=""
        ).pack(
            expand=True
        )

        # =======================================
        # Footer
        # =======================================

        line = ctk.CTkFrame(
            self,
            height=2,
            fg_color=DIVIDER
        )

        line.pack(
            fill="x",
            padx=20,
            pady=10
        )

        status = ctk.CTkLabel(
            self,
            text="🟢 Online",
            font=(FONT, 13),
            text_color=SUCCESS
        )

        status.pack()

        version = ctk.CTkLabel(
            self,
            text="Version 3.0",
            font=(FONT, 11),
            text_color=TEXT_SECONDARY
        )

        version.pack(
            pady=(5,20)
        )

    # =======================================
    # Button Builder
    # =======================================

    def create_button(self, text, command):

        btn = ctk.CTkButton(

            self,

            text=text,

            command=command,

            height=46,

            corner_radius=12,

            fg_color=BUTTON,

            hover_color=BUTTON_HOVER,

            font=(FONT,15),

            anchor="w"

        )

        btn.pack(

            fill="x",

            padx=18,

            pady=6

        )