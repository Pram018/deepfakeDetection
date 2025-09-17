async function sendFile() {
    const fileInput = document.getElementById("file_input");
    const type = document.getElementById("type_select").value;
    const chatBox = document.getElementById("chat-box");

    if (!fileInput.files[0]) return alert("Select a file!");

    const file = fileInput.files[0];

    const userMsg = document.createElement("div");
    userMsg.className = "message user";
    userMsg.textContent = `Uploading ${file.name}...`;
    chatBox.appendChild(userMsg);
    chatBox.scrollTop = chatBox.scrollHeight;

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`/analyze_${type}`, { method: "POST", body: formData });
    const data = await response.json();

    const botMsg = document.createElement("div");
    botMsg.className = "message bot";
    botMsg.textContent = `Prediction: ${data.prediction}`;
    chatBox.appendChild(botMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
}
