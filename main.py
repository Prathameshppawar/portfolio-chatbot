from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
client = Groq()
app = FastAPI()

class ChatInput(BaseModel):
    question: str

def load_data():
    with open("data.txt", "r", encoding='utf-8') as f:
        return f.read()

@app.post("/chat")
def chat(chat: ChatInput):
    context = load_data()
    prompt = f"Answer the question based on the following user bio:\n\n{context}\n\nQ: {chat.question}\nA:"

    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}]
        )
        return {"answer": response.choices[0].message.content.strip()}
    except Exception as e:
        return {"error": str(e)}
