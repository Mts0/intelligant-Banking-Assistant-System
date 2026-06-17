const API_URL = "http://localhost:8000/chat";

async function sendMessage() {

    const input = document.getElementById("message");
    const chatBox = document.getElementById("chat-box");

    const text = input.value.trim();

    if (!text) return;

    chatBox.innerHTML += `
        <div class="user">
            ${text}
        </div>
    `;

    input.value = "";

    try {

        const response = await fetch(API_URL + "/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "accept": "application/json"
            },
            body: JSON.stringify({
                message: text
            })
        });

        const data = await response.json();

        chatBox.innerHTML += `
            <div class="bot" dir="ltr">
                ${JSON.stringify(data.answer)}
            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {

        chatBox.innerHTML += `
            <div class="bot">
                خطأ في الاتصال بالخادم
            </div>
        `;
    }
}