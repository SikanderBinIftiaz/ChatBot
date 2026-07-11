"""
ui_components.py
----------------------------------------
Reusable UI Components
"""

import customtkinter as ctk
from themes import COLORS, FONTS


# -------------------------------------------------------
# Dashboard Card
# -------------------------------------------------------

class DashboardCard(ctk.CTkFrame):

    def __init__(self, master, title, value="0"):

        super().__init__(
            master,
            fg_color=COLORS["header"],
            corner_radius=15
        )

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=FONTS["normal"],
            text_color=COLORS["secondary_text"]
        )

        self.title.pack(pady=(15,5))

        self.value = ctk.CTkLabel(
            self,
            text=value,
            font=("Segoe UI",28,"bold")
        )

        self.value.pack(pady=(0,15))

    def update_value(self,value):

        self.value.configure(text=str(value))


# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            width=260,
            fg_color=COLORS["sidebar"],
            corner_radius=0
        )

        self.pack_propagate(False)

        # -------------------------
        # Logo
        # -------------------------

        logo = ctk.CTkLabel(

            self,

            text="🤖\nAI FAQ\nAssistant",

            font=("Segoe UI",24,"bold")

        )

        logo.pack(pady=(25,20))

        # -------------------------
        # Status
        # -------------------------

        self.status = ctk.CTkLabel(

            self,

            text="🟢 Online",

            font=FONTS["normal"],

            text_color=COLORS["success"]

        )

        self.status.pack()

        # -------------------------
        # Cards
        # -------------------------

        self.question_card = DashboardCard(

            self,

            "Questions Asked",

            "0"

        )

        self.question_card.pack(

            fill="x",

            padx=15,

            pady=(25,10)

        )

        self.confidence_card = DashboardCard(

            self,

            "Average Confidence",

            "0%"

        )

        self.confidence_card.pack(

            fill="x",

            padx=15,

            pady=10

        )

        self.faq_card = DashboardCard(

            self,

            "FAQs Loaded",

            "0"

        )

        self.faq_card.pack(

            fill="x",

            padx=15,

            pady=10

        )

        # -------------------------
        # Search
        # -------------------------

        self.search = ctk.CTkEntry(

            self,

            placeholder_text="🔍 Search FAQ..."

        )

        self.search.pack(

            fill="x",

            padx=15,

            pady=(25,10)

        )

        # -------------------------
        # Theme Switch
        # -------------------------

        self.theme = ctk.CTkSwitch(

            self,

            text="Dark Mode"

        )

        self.theme.select()

        self.theme.pack(

            padx=15,

            anchor="w",

            pady=10

        )

        # -------------------------
        # Buttons
        # -------------------------

        self.export_btn = ctk.CTkButton(

            self,

            text="💾 Export Chat"

        )

        self.export_btn.pack(

            fill="x",

            padx=15,

            pady=(25,10)

        )

        self.clear_btn = ctk.CTkButton(

            self,

            text="🗑 Clear Chat",

            fg_color=COLORS["danger"]

        )

        self.clear_btn.pack(

            fill="x",

            padx=15

        )

    # ---------------------------------------

    def update_questions(self,value):

        self.question_card.update_value(value)

    # ---------------------------------------

    def update_confidence(self,value):

        self.confidence_card.update_value(f"{value:.1f}%")

    # ---------------------------------------

    def update_faqs(self,value):

        self.faq_card.update_value(value)