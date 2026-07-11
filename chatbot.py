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

API_KEY = (
    st.secrets.get("GEMINI_API_KEY", None)
    or os.getenv("GEMINI_API_KEY")
)

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. "
        "Please add it to Streamlit Secrets or your local .env file."
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
                "I'm your AI Assistant powered by Google Gemini.",

            "what is your name":
                "I'm AI FAQ Assistant.",

            "thanks":
                "You're welcome! 😊",

            "thank you":
                "You're welcome! 😊",

            "bye":
                "Goodbye! 👋",

            "goodbye":
                "See you again! 👋"

        }

        print(f"✅ Loaded {len(self.questions)} FAQs")


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

            print(e)

            return (
                "Sorry, Gemini AI is currently unavailable.\n\n"
                f"Error: {e}"
            )


    # ==========================================================
    # SEARCH FAQ
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
    # MAIN ANSWER FUNCTION
    # ==========================================================

    def get_answer(self, user_question):

        question = user_question.strip()

        if question == "":
            return (
                "Please enter a question.",
                0.0
            )

        lower_question = question.lower()

        if lower_question in self.greetings:

            return (
                self.greetings[lower_question],
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

    chatbot = FAQChatbot()

    print("=" * 60)
    print("🤖 AI FAQ Chatbot")
    print("=" * 60)

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            break

        answer, confidence = chatbot.get_answer(question)

        print("\nBot:")
        print(answer)
        print(f"\nConfidence: {confidence:.2%}")