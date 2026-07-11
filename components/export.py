from __future__ import annotations

import json
import os
from datetime import datetime
from io import BytesIO

try:
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

    REPORTLAB_AVAILABLE = True

except ImportError:
    REPORTLAB_AVAILABLE = False


EXPORT_FOLDER = "exports"


# ============================================================
# HELPERS
# ============================================================

def _ensure_export_folder():
    """Create exports folder if it doesn't exist."""

    os.makedirs(
        EXPORT_FOLDER,
        exist_ok=True
    )


def _timestamp():
    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


def _filename(extension: str):

    return f"chat_{_timestamp()}.{extension}"


# ============================================================
# TXT EXPORT
# ============================================================

def export_txt(messages):

    lines = []

    lines.append("=" * 60)
    lines.append("AI FAQ Chatbot")
    lines.append("Conversation Export")
    lines.append("=" * 60)
    lines.append(
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )
    lines.append("")

    for message in messages:

        role = message.get("role", "assistant")

        if role == "user":
            speaker = "You"
        else:
            speaker = "AI"

        lines.append(f"{speaker}:")
        lines.append(message.get("content", ""))
        lines.append("")

    text = "\n".join(lines)

    filename = _filename("txt")

    path = os.path.join(
        EXPORT_FOLDER,
        filename
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

    return (
        text.encode("utf-8"),
        filename,
        "text/plain"
    )


# ============================================================
# JSON EXPORT
# ============================================================

def export_json(messages):

    data = {

        "application": "AI FAQ Chatbot",

        "created_at": datetime.now().isoformat(),

        "total_messages": len(messages),

        "messages": messages

    }

    text = json.dumps(
        data,
        indent=4,
        ensure_ascii=False
    )

    filename = _filename("json")

    path = os.path.join(
        EXPORT_FOLDER,
        filename
    )

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(text)

    return (
        text.encode("utf-8"),
        filename,
        "application/json"
    )


# ============================================================
# PDF EXPORT
# ============================================================

def export_pdf(messages):

    if not REPORTLAB_AVAILABLE:

        raise RuntimeError(

            "ReportLab is not installed.\n\n"

            "Install using:\n"

            "pip install reportlab"

        )

    buffer = BytesIO()

    document = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "<b>AI FAQ Chatbot</b>",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "Conversation Export",
            styles["Heading2"]
        )
    )

    story.append(
        Paragraph(
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            styles["Normal"]
        )
    )

    story.append(
        Spacer(
            1,
            18
        )
    )

    for message in messages:

        role = message.get(
            "role",
            "assistant"
        )

        if role == "user":
            speaker = "You"
        else:
            speaker = "AI Assistant"

        story.append(

            Paragraph(

                f"<b>{speaker}</b>",

                styles["Heading3"]

            )

        )

        story.append(

            Paragraph(

                message.get(
                    "content",
                    ""
                ),

                styles["BodyText"]

            )

        )

        story.append(
            Spacer(
                1,
                12
            )
        )

    document.build(story)

    pdf_bytes = buffer.getvalue()

    filename = _filename("pdf")

    path = os.path.join(
        EXPORT_FOLDER,
        filename
    )

    with open(
        path,
        "wb"
    ) as file:

        file.write(pdf_bytes)

    return (
        pdf_bytes,
        filename,
        "application/pdf"
    )


# ============================================================
# MAIN EXPORT FUNCTION
# ============================================================

def generate_export(

    messages,

    export_format

):
    """
    Returns:

    bytes,
    filename,
    mime_type
    """

    _ensure_export_folder()

    export_format = export_format.upper()

    if export_format == "TXT":

        return export_txt(messages)

    elif export_format == "JSON":

        return export_json(messages)

    elif export_format == "PDF":

        return export_pdf(messages)

    return (
        None,
        None,
        None
    )