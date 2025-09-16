import os
import streamlit as st
from streamlit_chat import message
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests

# -----------------------------
# Gemini API Setup
# -----------------------------
from dotenv import load_dotenv
load_dotenv()  # loads GEMINI_API_KEY from .env file
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# -----------------------------
# Lottie animation loader
# -----------------------------
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_header = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_tutvdkg0.json")

# -----------------------------
# Streamlit Page Config
# -----------------------------
st.set_page_config(page_title="AI Company Agent", page_icon="🤖", layout="wide")
st_lottie(lottie_header, height=150, key="header")
st.title("🤖 AI Agent for Companies")
st.write("Choose a service below and let AI assist you!")

# -----------------------------
# Sidebar Menu
# -----------------------------
option = st.sidebar.selectbox(
    "Select Service",
    ("Email Writer", "Report Summarizer", "Customer Support")
)

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# -----------------------------
# AI Functions
# -----------------------------
def generate_response(prompt):
    response = model.generate_content(prompt)
    return response.text

def email_writer(subject, points):
    prompt = f"Write a professional email on: {subject}\nPoints: {points}"
    return generate_response(prompt)

def summarize_text(text):
    prompt = f"Summarize this text in 5 bullet points:\n{text}"
    return generate_response(prompt)

def customer_support(query):
    prompt = f"You are a customer support AI. Answer politely:\n{query}"
    return generate_response(prompt)

# -----------------------------
# User Interaction
# -----------------------------
user_input = ""
if option == "Email Writer":
    subject = st.text_input("Email Subject")
    points = st.text_area("Key Points")
    if st.button("Generate Email"):
        user_input = f"Email: {subject} | {points}"
        output = email_writer(subject, points)
        st.session_state.history.append(("User", user_input))
        st.session_state.history.append(("Agent", output))

elif option == "Report Summarizer":
    text = st.text_area("Paste Text to Summarize")
    if st.button("Summarize"):
        user_input = text
        output = summarize_text(text)
        st.session_state.history.append(("User", user_input))
        st.session_state.history.append(("Agent", output))

elif option == "Customer Support":
    query = st.text_input("Enter Customer Query")
    if st.button("Get Response"):
        user_input = query
        output = customer_support(query)
        st.session_state.history.append(("User", user_input))
        st.session_state.history.append(("Agent", output))

# -----------------------------
# Display Chat
# -----------------------------
for i, (sender, msg) in enumerate(st.session_state.history):
    if sender == "User":
        message(msg, is_user=True, key=f"{i}_user")
    else:
        message(msg, is_user=False, key=f"{i}_agent")

