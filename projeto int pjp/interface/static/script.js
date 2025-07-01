document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const userInput = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const userMessage = userInput.value.trim();

        if (userMessage === '') {
            return;
        }

        // Adiciona a mensagem do usuário ao chat
        addMessage(userMessage, 'user-message');
        userInput.value = '';

        try {
            // Envia a mensagem para o backend
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            const botMessage = data.response;

            // Adiciona a resposta do bot ao chat
            addMessage(botMessage, 'bot-message');

        } catch (error) {
            console.error('Erro ao comunicar com o chatbot:', error);
            addMessage('Desculpe, ocorreu um erro. Tente novamente mais tarde.', 'bot-message');
        }
    });

    function addMessage(text, className) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message', className);

        const p = document.createElement('p');
        p.textContent = text;
        
        messageElement.appendChild(p);
        chatBox.appendChild(messageElement);

        // Rola para a mensagem mais recente
        scrollToBottom();
    }

    function scrollToBottom() {
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Foco no input ao carregar a página
    userInput.focus();
});