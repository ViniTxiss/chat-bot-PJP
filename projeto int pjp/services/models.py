import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def teste_gerar():
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    chat = model.start_chat()
    response = chat.send_message("Olá, teste de modelo com quota gratuita.")
    print(response.text)

if __name__ == "__main__":
    teste_gerar()
