function sendMessage() {
    var messageInput = document.getElementById("message-input");
    var messageText = messageInput.value.trim();
    if (messageText !== "") {
        addMessage("You", messageText);
        messageInput.value = "";
    }
}

function addMessage(sender, message) {
    var chatBox = document.getElementById("chat-box");
    var newMessage = document.createElement("div");
    newMessage.classList.add("message");
    newMessage.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatBox.appendChild(newMessage);
    chatBox.scrollTop = chatBox.scrollHeight;

    var teacherMsg = document.createElement("div");
    teacherMsg.classList.add("message");

    const responses = [
        "I'll be there in a minute!",
        "Just a moment, let me check.",
        "Let me see what I can do to assist you.",
        "I'm here to help, what do you need?",
        "Give me a second to respond.",
        "Thanks for reaching out, I'll get back to you shortly.",
        "Your request has been received, I'll address it promptly.",
        "I'm on it!",
        "Your inquiry is noted, I'll provide assistance shortly.",
        "Don't worry, I'm here to support you."
    ];

    const randomIndex = Math.floor(Math.random() * responses.length);
    const randomResponse = responses[randomIndex];

    teacherMsg.innerHTML = `<strong>Teacher:</strong> ${randomResponse}`;
    chatBox.appendChild(teacherMsg);
    chatBox.scrollTop = chatBox.scrollHeight;
}



function teacherMessage() {
    var chatBox = document.getElementById("chat-box");
    var newMessage = document.createElement("div");
    newMessage.classList.add("message");
    const teacherChatMessages = [
        "Good morning class! I hope everyone had a fantastic weekend. Let's dive into today's lesson on pointers.",
        "Remember, if you have any questions about the assignment, don't hesitate to reach out to me via email or during office hours.",
        "Is there a problem I could help with?",
        "Don't forget to review the study guide for our upcoming test. It covers important concepts from the last few weeks.",
        "Hello there! How are you feeling?",
        "I'll be hosting a review session after school tomorrow for anyone who wants extra help preparing for the exam. Hope to see you there!",
        "Please make sure to bring your textbooks to class tomorrow. We'll be referring to them for our discussion on chapter 5 about arrays.",
        "Congratulations to Kiara for winning the Hackaton! Your hard work and dedication really paid off.",
        "Ready to code?",
        "Hello! Ready for another day of learning?"
      ];

    const randomIndex = Math.floor(Math.random() * teacherChatMessages.length);
    const randomMessage = teacherChatMessages[randomIndex];
    
    newMessage.innerHTML = `<strong>Teacher:</strong> ${randomMessage}`;
    chatBox.appendChild(newMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}

teacherMessage();