// script.js

const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');

sendButton.addEventListener('click', () => {
    const userMessage = userInput.value;
    userInput.value = '';
    appendMessage('user', userMessage);

    fetch('./chatbot', {
        method: 'POST',
        body: new URLSearchParams({ user_message: userMessage }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.text())
    .then(botReply => {
        appendMessage('bot', botReply);
    });
});

function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.classList.add(sender);
    messageElement.innerText = message;
    chatBox.appendChild(messageElement);
}
