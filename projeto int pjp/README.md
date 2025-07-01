# Chatbot Jovem Programador com Gemini

## 📝 Descrição

Este projeto é um assistente de chat (chatbot) desenvolvido para responder perguntas sobre o programa "Jovem Programador". Ele utiliza a API do Google Gemini para gerar respostas com base em uma base de conhecimento pré-definida, garantindo que as informações sejam precisas e contextuais.

A aplicação possui duas interfaces:
1.  Uma interface web amigável construída com Flask.
2.  Uma interface de linha de comando para testes e interações diretas.

## ✨ Funcionalidades

-   **Interface Web**: Um chat limpo e responsivo para interagir com o bot.
-   **Base de Conhecimento**: Utiliza um arquivo `dados.txt` como única fonte de verdade, evitando que o modelo de linguagem "invente" respostas.
-   **Integração com Gemini**: Conecta-se à API do Google Gemini (modelo `gemini-1.5-flash`) para processamento de linguagem natural.
-   **Fácil Configuração**: Utiliza variáveis de ambiente para gerenciar a chave da API de forma segura.

## 📂 Estrutura do Projeto

```
projeto int pjp/
├── .env                # Arquivo para armazenar a chave da API (não versionado)
├── dados.txt           # Base de conhecimento do chatbot
├── main.py             # Lógica principal do chatbot e interface de linha de comando
├── scraping.py         # (Script auxiliar para obter dados, se aplicável)
├── README.md           # Este arquivo
├── requirements.txt    # Dependências do Python
└── interface/
    ├── app.py          # Servidor web Flask que serve a interface
    ├── static/         # Arquivos estáticos (CSS, JavaScript)
    │   ├── script.js
    │   └── style.css
    └── templates/      # Templates HTML do Flask
        └── chat.html
```

## 🚀 Instalação e Configuração

Siga os passos abaixo para executar o projeto em sua máquina local.

### 1. Pré-requisitos

-   Python 3.8 ou superior
-   Uma chave de API do Google Gemini (disponível no Google AI Studio)

### 2. Instalação

1.  **Clone o repositório** (ou use a sua pasta local do projeto).

2.  **Crie um ambiente virtual** (recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências**:
    Com o ambiente virtual ativado, execute o seguinte comando na pasta raiz do projeto para instalar todas as bibliotecas necessárias a partir do arquivo `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a Chave da API**:
    -   Crie um arquivo chamado `.env` na raiz do projeto (`projeto int pjp/.env`).
    -   Adicione sua chave da API do Gemini a este arquivo:
        ```
        GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
        ```
    -   Substitua `"SUA_CHAVE_API_AQUI"` pela sua chave real.

## 🏃 Como Executar

Você pode executar a aplicação de duas maneiras:

### Interface Web (Recomendado)

1.  Navegue até a pasta `interface`: `cd interface`
2.  Inicie o servidor Flask: `python app.py`
3.  Abra seu navegador e acesse `http://127.0.0.1:5000`.

### Interface de Linha de Comando

1.  Certifique-se de estar na pasta raiz do projeto (`projeto int pjp/`).
2.  Execute o script `main.py`: `python main.py`
3.  Interaja com o chatbot diretamente no seu terminal. Digite `sair` para encerrar.

## ⚙️ Como Funciona

-   **`dados.txt`**: Contém pares de perguntas e respostas que servem como contexto para o modelo de linguagem.
-   **`main.py`**: A função `responder_com_gemini` cria um *prompt* que instrui o Gemini a usar exclusivamente a `base_conhecimento` (o conteúdo de `dados.txt`) para formular a resposta à `pergunta_usuario`. Isso limita o escopo do modelo e aumenta a precisão.
-   **`interface/app.py`**: Este servidor Flask tem uma rota principal (`/`) que renderiza a página do chat e uma rota `/chat` (via POST) que recebe a mensagem do usuário em formato JSON. Ele chama a função `responder_com_gemini` e retorna a resposta do bot, também em JSON.
-   **`interface/static/script.js`**: O JavaScript captura o envio do formulário, envia a mensagem do usuário para o endpoint `/chat` usando `fetch()`, aguarda a resposta e, em seguida, adiciona dinamicamente tanto a mensagem do usuário quanto a resposta do bot à janela de chat.