"""
utils.py
---------------------------------------
Utility functions for AI FAQ Assistant
"""

import os
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph


# --------------------------------------------------
# Create Export Folder
# --------------------------------------------------

EXPORT_FOLDER = "exports"

os.makedirs(EXPORT_FOLDER, exist_ok=True)


# --------------------------------------------------
# Current Time
# --------------------------------------------------

def current_time():
    """
    Returns current time
    Example: 08:45 PM
    """
    return datetime.now().strftime("%I:%M %p")


# --------------------------------------------------
# Current Date
# --------------------------------------------------

def current_date():
    """
    Returns current date
    """
    return datetime.now().strftime("%d-%m-%Y")


# --------------------------------------------------
# Session Name
# --------------------------------------------------

def session_filename(extension="txt"):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return os.path.join(
        EXPORT_FOLDER,
        f"chat_session_{timestamp}.{extension}"
    )


# --------------------------------------------------
# Export TXT
# --------------------------------------------------

def export_txt(chat_text):

    filename = session_filename("txt")

    with open(filename, "w", encoding="utf-8") as file:

        file.write(chat_text)

    return filename


# --------------------------------------------------
# Export PDF
# --------------------------------------------------

def export_pdf(chat_text):

    filename = session_filename("pdf")

    document = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    story = []

    for line in chat_text.split("\n"):

        story.append(
            Paragraph(line.replace(" ", "&nbsp;"), styles["BodyText"])
        )

    document.build(story)

    return filename


# --------------------------------------------------
# Average Confidence
# --------------------------------------------------

def average_confidence(confidence_list):

    if len(confidence_list) == 0:

        return 0

    return round(

        sum(confidence_list) / len(confidence_list),

        2

    )


# --------------------------------------------------
# Confidence Color
# --------------------------------------------------

def confidence_color(score):

    if score >= 0.80:

        return "#16A34A"

    elif score >= 0.50:

        return "#F59E0B"

    return "#DC2626"


# --------------------------------------------------
# Typing Animation
# --------------------------------------------------

def typing_frames():

    return [

        "🤖 Typing.",
        "🤖 Typing..",
        "🤖 Typing...",
        "🤖 Typing...."

    ]