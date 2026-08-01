const form = document.getElementById('chat-form');
const chatBox = document.getElementById('chat-box');
const input = document.getElementById('message-input');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userMessage = input.value.trim();
    if (!userMessage) return;

    // Append user message
    appendMessage(userMessage, 'user-message');

    // Clear input
    input.value = '';
    input.focus();

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message: userMessage})
        });

        const data = await response.json();
        appendMessage(data.reply, 'bot-message', true);

        // Scroll chat to bottom
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        appendMessage("Sorry, something went wrong.", 'bot-message');
    }
});

function appendMessage(text, className, isHtml = false) {
    const messageElem = document.createElement('div');
    messageElem.classList.add('message', className);
    if (isHtml) {
        messageElem.innerHTML = text;
    } else {
        messageElem.textContent = text;
    }
    chatBox.appendChild(messageElem);
    chatBox.scrollTop = chatBox.scrollHeight;
}
