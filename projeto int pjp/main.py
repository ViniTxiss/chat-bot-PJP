import google.generativeai as genai
from dotenv import load_dotenv
import os

# Carrega as variáveis do .env
load_dotenv()

def carregar_conhecimento(caminho="dados.txt"):
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()

def iniciar_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("❌ API KEY da Gemini não encontrada. Verifique seu .env.")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
    chat = model.start_chat()
    return chat

def responder_com_gemini(chat, base_conhecimento, pergunta_usuario):
    prompt = f"""
    Use o conteúdo abaixo como base para responder a pergunta de forma direta, sem inventar nada que não esteja no texto.

    === BASE DE CONHECIMENTO ===
    {base_conhecimento}

    === PERGUNTA ===
    {pergunta_usuario}

    Responda com base apenas no conteúdo da base acima.
    """
    resposta = chat.send_message(prompt)
    return resposta.text.strip()

def iniciar_chatbot():
    chat = iniciar_gemini()
    base_conhecimento = carregar_conhecimento()

    print("🤖 Chatbot PJP (LLM Gemini) iniciado! Digite 'sair' para encerrar.")
    while True:
        pergunta = input("👤 Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("🤖 Até mais!")
            break
        resposta = responder_com_gemini(chat, base_conhecimento, pergunta)
        print(f"\n🤖 {resposta}")

if __name__ == "__main__":
    iniciar_chatbot()
