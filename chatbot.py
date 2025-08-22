import os
import openai

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("python-dotenv is not installed. You can install it with 'pip install python-dotenv'.")

# Securely load API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not found. Please set your API key.")

openai.api_key = api_key


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat_with_gpt(user_input)
        print("ChatBot: ", response)