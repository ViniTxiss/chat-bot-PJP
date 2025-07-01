from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os
import sys

# Adiciona o diretório raiz ao path para encontrar o main.py e outros módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa as funções do seu arquivo main.py
from main import carregar_conhecimento, iniciar_gemini, responder_com_gemini

app = Flask(__name__)

# --- INICIALIZAÇÃO DO CHATBOT ---
# Carrega as variáveis de ambiente do arquivo .env na raiz do projeto
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

try:
    # Define o caminho para o arquivo de dados
    caminho_dados = os.path.join(os.path.dirname(__file__), '..', 'dados.txt')
    
    # Carrega a base de conhecimento e inicia o modelo Gemini
    base_conhecimento = carregar_conhecimento(caminho_dados)
    chat_session = iniciar_gemini()
    print("✅ Chatbot Gemini inicializado com sucesso!")

except Exception as e:
    print(f"❌ Erro ao inicializar o chatbot: {e}")
    base_conhecimento = None
    chat_session = None
# ------------------------------------

@app.route('/')
def home():
    return render_template('chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    if not chat_session:
        return jsonify({'response': 'Desculpe, o chatbot não está disponível no momento.'}), 500

    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'Mensagem não pode ser vazia.'}), 400

    bot_response = responder_com_gemini(chat_session, base_conhecimento, user_message)
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run(debug=True)
