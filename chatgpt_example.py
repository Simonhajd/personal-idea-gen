import time
from openai import OpenAI
import tkinter
from tkinter import messagebox
import os
from dotenv import load_dotenv  # Import load_dotenv from dotenv

# Load environment variables from .env file
load_dotenv()
client = OpenAI(
    api_key=os.getenv("API_KEY"),
    organization=os.getenv("ORGANIZATION"),
    project=os.getenv("PROJECT"),
)

messages = [
    
]

while True:

    user_input = input("You: ")
    


    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )

    ai_response = response.choices[0].message.content
    print("AI: ", ai_response, "\n")

    messages.append({"role": "assistant", "content": ai_response})