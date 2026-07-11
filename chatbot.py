import os
import json

import streamlit as st
from dotenv import load_dotenv
from google import genai

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================================
# LOAD API KEY
# ==========================================================

load_dotenv()


def get_api_key():
    """
    Get Gemini API Key from:
    1. Streamlit Secrets (Cloud)
    2. .env file (Local)
    """

    try:
        if "GEMINI_API_KEY" in st.secrets:
            return st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

    return os.getenv("GEMINI_API_KEY")


API_KEY = get_api_key()

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found.\n\n"
        "Local: Add it to your .env file.\n"
        "Streamlit Cloud: Add it under Settings → Secrets."
    )


client = genai.Client(api_key=API_KEY)


# ==========================================================
# FAQ CHATBOT
# ==========================================================

class FAQChatbot:

    def __init__(self):

        with open("faq_data.json", "r", encoding="utf-8") as file:
            self.data = json.load(file)

        self.questions = [
            item["question"]
            for item in self.data
        ]

        self.answers = [
            item["answer"]
            for item in self.data
        ]

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        self.question_vectors = self.vectorizer.fit_transform(
            self.questions
        )

        self.greetings = {

            "hi":
                "Hello! 👋 How can I help you today?",

            "hello":
                "Hello! 👋 How can I help you today?",

            "hey":
                "Hi! 😊",

            "good morning":
                "Good Morning! ☀️",

            "good afternoon":
                "Good Afternoon! 😊",

            "good evening":
                "Good Evening! 🌙",

            "how are you":
                "I'm doing great! 😊",

            "who are you":
                "I'm your AI FAQ Assistant powered by Google Gemini.",

            "what is your name":
                "I'm AI FAQ Assistant.",

            "thanks":
                "You're welcome! 😊",

            "thank you":
                "You're welcome! 😊",

            "bye":
                "Goodbye! 👋 Have a wonderful day.",

            "goodbye":
                "See you again soon! 👋"

        }

        print("✅ FAQ Loaded Successfully")
        print(f"✅ Total FAQs: {len(self.questions)}")


    # ==========================================================
    # GEMINI
    # ==========================================================

    def ask_gemini(self, question):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=question
            )

            if hasattr(response, "text") and response.text:
                return response.text.strip()

            return "Sorry, I couldn't generate a response."

        except Exception as e:

            print("\n========== GEMINI ERROR ==========")
            print(type(e))
            print(e)
            print("==================================")

            return (
                "Sorry, the AI service is temporarily unavailable.\n\n"
                f"Error: {str(e)}"
            )


    # ==========================================================
    # FAQ SEARCH
    # ==========================================================

    def search_faq(self, question):

        user_vector = self.vectorizer.transform([question])

        similarity = cosine_similarity(
            user_vector,
            self.question_vectors
        )[0]

        best_index = similarity.argmax()

        confidence = float(similarity[best_index])

        if confidence >= 0.35:

            return (
                self.answers[best_index],
                confidence,
                True
            )

        return (
            None,
            confidence,
            False
        )


    # ==========================================================
    # GET ANSWER
    # ==========================================================

    def get_answer(self, user_question):

        question = user_question.strip()

        if not question:

            return (
                "Please enter a question.",
                0.0
            )

        lower = question.lower()

        if lower in self.greetings:

            return (
                self.greetings[lower],
                1.0
            )

        answer, confidence, found = self.search_faq(question)

        if found:

            return (
                answer,
                confidence
            )

        answer = self.ask_gemini(question)

        return (
            answer,
            0.99
        )


# ==========================================================
# TERMINAL TEST
# ==========================================================

if __name__ == "__main__":

    bot = FAQChatbot()

    print("=" * 60)
    print("🤖 AI FAQ Chatbot")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        answer, confidence = bot.get_answer(question)

        print("\nBot:")
        print(answer)
        print(f"\nConfidence: {confidence:.2%}")