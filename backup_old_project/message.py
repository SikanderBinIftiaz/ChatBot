import customtkinter as ctk
from theme import *


class MessageBubble(ctk.CTkFrame):

    def __init__(self, master, text, sender="bot"):

        super().__init__(
            master,
            fg_color="transparent"
        )

        if sender == "user":

            bubble_color = PRIMARY
            text_color = "white"
            emoji = "👤"

            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=0)

            bubble = ctk.CTkFrame(
                self,
                fg_color=bubble_color,
                corner_radius=18
            )

            bubble.grid(
                row=0,
                column=1,
                padx=15,
                pady=8,
                sticky="e"
            )

            avatar = ctk.CTkLabel(
                self,
                text=emoji,
                font=(FONT, 24)
            )

            avatar.grid(
                row=0,
                column=2,
                padx=(5, 15),
                sticky="n"
            )

        else:

            bubble_color = CARD
            text_color = TEXT
            emoji = "🤖"

            self.grid_columnconfigure(1, weight=1)

            avatar = ctk.CTkLabel(
                self,
                text=emoji,
                font=(FONT, 24)
            )

            avatar.grid(
                row=0,
                column=0,
                padx=(15, 5),
                sticky="n"
            )

            bubble = ctk.CTkFrame(
                self,
                fg_color=bubble_color,
                corner_radius=18
            )

            bubble.grid(
                row=0,
                column=1,
                padx=10,
                pady=8,
                sticky="w"
            )

        message = ctk.CTkLabel(

            bubble,

            text=text,

            wraplength=700,

            justify="left",

            text_color=text_color,

            font=(FONT, 15)

        )

        message.pack(
            padx=18,
            pady=14
        )