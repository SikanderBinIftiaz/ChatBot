import threading

from datetime import datetime

import customtkinter as ctk

from chatbot import FAQChatbot
from sidebar import Sidebar
from chatbubble import ChatBubble

from theme import *


class App(ctk.CTk):

    def __init__(self):

        super().__init__()

        # =====================================================
        # Window
        # =====================================================

        self.title("AI FAQ Chatbot")

        self.geometry("1450x850")

        self.minsize(1200, 700)

        self.configure(
            fg_color=BACKGROUND
        )

        # =====================================================
        # Data
        # =====================================================

        self.bot = FAQChatbot()

        self.question_count = 0

        self.messages = []

        # =====================================================
        # Root Layout
        # =====================================================

        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)

        # =====================================================
        # Sidebar
        # =====================================================

        self.sidebar = Sidebar(self)

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="ns"
        )

        # =====================================================
        # Main Frame
        # =====================================================

        self.main = ctk.CTkFrame(
            self,
            fg_color=BACKGROUND,
            corner_radius=0
        )

        self.main.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=18,
            pady=18
        )

        self.main.grid_columnconfigure(
            0,
            weight=1
        )

        self.main.grid_rowconfigure(
            1,
            weight=1
        )

        # =====================================================
        # Header
        # =====================================================

        self.header = ctk.CTkFrame(
            self.main,
            fg_color=CARD,
            corner_radius=18,
            height=72
        )

        self.header.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 15)
        )

        self.header.grid_columnconfigure(
            1,
            weight=1
        )

        # AI Logo

        self.logo = ctk.CTkLabel(
            self.header,
            text="🤖",
            font=(FONT, 34)
        )

        self.logo.grid(
            row=0,
            column=0,
            padx=22
        )

        # Title

        self.title_label = ctk.CTkLabel(
            self.header,
            text="AI FAQ Assistant",
            font=TITLE_FONT,
            text_color=TEXT
        )

        self.title_label.grid(
            row=0,
            column=1,
            sticky="w"
        )

        # Status

        self.status = ctk.CTkLabel(
            self.header,
            text="🟢 Gemini Online",
            font=TEXT_FONT,
            text_color=SUCCESS
        )

        self.status.grid(
            row=0,
            column=2,
            padx=22
        )
                # =====================================================
        # Chat Container
        # =====================================================

        self.chat_container = ctk.CTkFrame(
            self.main,
            fg_color=CARD,
            corner_radius=18
        )

        self.chat_container.grid(
            row=1,
            column=0,
            sticky="nsew",
            pady=(0, 15)
        )

        self.chat_container.grid_rowconfigure(0, weight=1)
        self.chat_container.grid_columnconfigure(0, weight=1)

        # =====================================================
        # Scrollable Chat Area
        # =====================================================

        self.chat_area = ctk.CTkScrollableFrame(
            self.chat_container,
            fg_color=CARD,
            corner_radius=18
        )

        self.chat_area.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        self.chat_area.grid_columnconfigure(0, weight=1)

        # =====================================================
        # Welcome Message
        # =====================================================

        self.add_ai_message(
            "👋 Welcome to AI FAQ Assistant!\n\n"
            "Powered by Google Gemini 2.5 Flash.\n\n"
            "You can ask:\n\n"
            "• What is Artificial Intelligence?\n"
            "• Explain Machine Learning\n"
            "• Write Python code\n"
            "• Explain SQL Joins\n"
            "• Solve a programming problem"
        )

        # =====================================================
        # Bottom Input Area
        # =====================================================

        self.bottom = ctk.CTkFrame(
            self.main,
            fg_color=CARD,
            corner_radius=18,
            height=90
        )

        self.bottom.grid(
            row=2,
            column=0,
            sticky="ew"
        )

        self.bottom.grid_columnconfigure(0, weight=1)

        # =====================================================
        # Entry
        # =====================================================

        self.entry = ctk.CTkEntry(
            self.bottom,
            height=52,
            corner_radius=26,
            fg_color=INPUT,
            border_color=BORDER,
            text_color=TEXT,
            placeholder_text="Message AI Assistant...",
            font=TEXT_FONT
        )

        self.entry.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=(20, 10),
            pady=20
        )

        self.entry.bind(
            "<Return>",
            self.send_message
        )

                # =====================================================
        # Send Button
        # =====================================================

        self.send_btn = ctk.CTkButton(
            self.bottom,
            text="➜",
            width=55,
            height=52,
            corner_radius=26,
            fg_color=PRIMARY,
            hover_color=PRIMARY_HOVER,
            font=(FONT, 22, "bold"),
            command=self.send_message
        )

        self.send_btn.grid(
            row=0,
            column=1,
            padx=(0, 20),
            pady=20
        )

        # Focus cursor on startup
        self.entry.focus()

        # Close button handler
        self.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

    # =====================================================
    # Scroll to Bottom
    # =====================================================

    def scroll_to_bottom(self):

        self.update_idletasks()

        try:
            self.chat_area._parent_canvas.yview_moveto(1.0)
        except Exception:
            pass


    # =====================================================
    # Copy Callback
    # =====================================================

    def copied(self):

        self.status.configure(
            text="✅ Response copied to clipboard."
        )

        self.after(
            2000,
            lambda: self.status.configure(
                text="🟢 Gemini Online"
            )
        )

    # =====================================================
    # Add User Bubble
    # =====================================================

    def add_user_message(self, message):

        bubble = ChatBubble(
            self.chat_area,
            message=message,
            sender="user"
        )

        bubble.pack(
            fill="x",
            padx=15,
            pady=5
        )

        self.messages.append(bubble)

        self.scroll_to_bottom()


    # =====================================================
    # Add AI Bubble
    # =====================================================

    def add_ai_message(self, message):

        bubble = ChatBubble(
            self.chat_area,
            message=message,
            sender="ai",
            copy_callback=self.copied
        )

        bubble.pack(
            fill="x",
            padx=15,
            pady=5
        )

        self.messages.append(bubble)

        self.scroll_to_bottom()
            # =====================================================
    # Send Message
    # =====================================================

    def send_message(self, event=None):

        question = self.entry.get().strip()

        if not question:
            return

        self.entry.delete(0, "end")

        self.question_count += 1

        self.add_user_message(question)

        self.status.configure(
            text="🟡 AI is thinking..."
        )

        self.entry.configure(state="disabled")
        self.send_btn.configure(state="disabled")

        threading.Thread(
            target=self.get_bot_response,
            args=(question,),
            daemon=True
        ).start()


    # =====================================================
    # Get Bot Response (Background Thread)
    # =====================================================

    def get_bot_response(self, question):

        try:

            answer, confidence = self.bot.get_answer(question)

        except Exception as e:

            answer = f"❌ Error:\n\n{e}"

            confidence = 0

        self.after(
            0,
            lambda: self.show_response(
                answer,
                confidence
            )
        )


    # =====================================================
    # Show Response
    # =====================================================

    def show_response(self, answer, confidence):

        self.add_ai_message(answer)

        self.status.configure(
            text=f"🟢 Gemini Online | Confidence: {confidence*100:.1f}%"
        )

        self.entry.configure(
            state="normal"
        )

        self.send_btn.configure(
            state="normal"
        )

        self.entry.focus()
            # =====================================================
    # New Chat
    # =====================================================

    def new_chat(self):

        # Remove all existing chat bubbles
        for bubble in self.messages:
            bubble.destroy()

        self.messages.clear()

        self.question_count = 0

        self.status.configure(
            text="🟢 Gemini Online"
        )

        self.add_ai_message(
            "👋 New chat started.\n\n"
            "How can I help you today?"
        )


    # =====================================================
    # Chat History
    # =====================================================

    def show_history(self):

        self.add_ai_message(
            "📜 Chat History\n\n"
            "History Manager will be added in Version 3.1.\n\n"
            "All conversations will be automatically saved."
        )


    # =====================================================
    # Statistics
    # =====================================================

    def show_statistics(self):

        self.add_ai_message(

            f"""📊 AI Assistant Statistics

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Questions Asked : {self.question_count}

Model :
Gemini 2.5 Flash

Status :
Online

Theme :
Dark

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        )


    # =====================================================
    # Export Chat
    # =====================================================

    def export_chat(self):

        self.add_ai_message(

            "📄 Export Chat\n\n"

            "TXT Export\n"

            "PDF Export\n"

            "Markdown Export\n\n"

            "These features will be available in Version 3.1."
        )


    # =====================================================
    # Settings
    # =====================================================

    def open_settings(self):

        self.add_ai_message(

            "⚙ Settings\n\n"

            "• Light Mode\n"

            "• Dark Mode\n"

            "• Font Size\n"

            "• AI Model\n"

            "• Save History\n"

            "• Auto Export\n\n"

            "Coming soon..."
        )
            # =====================================================
    # Theme Toggle (Placeholder)
    # =====================================================

    def toggle_theme(self):

        mode = ctk.get_appearance_mode()

        if mode == "Dark":

            ctk.set_appearance_mode("Light")

            self.status.configure(
                text="🌞 Light Mode Enabled"
            )

        else:

            ctk.set_appearance_mode("Dark")

            self.status.configure(
                text="🌙 Dark Mode Enabled"
            )


    # =====================================================
    # Typing Animation
    # =====================================================

    def show_typing(self):

        self.status.configure(
            text="🟡 AI is typing..."
        )


    def hide_typing(self):

        self.status.configure(
            text="🟢 Gemini Online"
        )


    # =====================================================
    # Clear Messages
    # =====================================================

    def clear_messages(self):

        for widget in self.messages:
            widget.destroy()

        self.messages.clear()


    # =====================================================
    # Application Exit
    # =====================================================

    def on_close(self):

        self.destroy()