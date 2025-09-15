import os
import google.generativeai as genai

# 🔹 Step 1: Gemini API key set karo
os.environ["GEMINI_API_KEY"] = "AIzaSyB2X9dMJODm57MXXqCdnAxspmHbzsNT9Sk"

# 🔹 Step 2: Gemini configure karo
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 🔹 Step 3: Model load karo
model = genai.GenerativeModel("gemini-1.5-flash")

# 🔹 Step 4: Test query bhejna
response = model.generate_content(
    "Hello! You are my personal AI agent. Introduce yourself in 3 short lines."
)

# 🔹 Step 5: Output print karna
print("\n🤖 Agent Response:\n")
print(response.text)

def email_writer(subject, points):
    prompt = f"Write a professional email on: {subject}\nPoints to cover: {points}"
    response = model.generate_content(prompt)
    return response.text

def summarize_text(text):
    prompt = f"Summarize this text in 5 bullet points:\n{text}"
    response = model.generate_content(prompt)
    return response.text

def customer_support(query):
    prompt = f"You are a customer support AI. Answer this query politely:\n{query}"
    response = model.generate_content(prompt)
    return response.text

# ---- Testing ----
print("\n📧 Email Example:\n")
print(email_writer("Meeting Reminder", "Project update, tomorrow 11 AM, Zoom link attached"))

print("\n📑 Summary Example:\n")
print(summarize_text("Artificial Intelligence is changing industries. It helps in automation, decision making, and innovation across multiple sectors."))

print("\n🤝 Customer Support Example:\n")
print(customer_support("My internet is not working since morning, please help."))