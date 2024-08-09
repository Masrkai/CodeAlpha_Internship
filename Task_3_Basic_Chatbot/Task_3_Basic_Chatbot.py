import os
import nltk
import readline
import random
from nltk.chat.util import Chat, reflections
from ANSII import ANSIColor

# Ensuring nltk library behavior
current_directory = os.getcwd()
os.makedirs(current_directory, exist_ok=True)
nltk.data.path.append(current_directory)
nltk.download('punkt', download_dir=current_directory)

print(ANSIColor.format_text(f"'punkt' package has been downloaded to {current_directory}", color="green"))

# Define expanded patterns and responses
patterns = [
    (r'hi|hello|hey', [
        "Hello there! How can I assist you today?",
        "Greetings! What's on your mind?",
        "Hi! I'm here to chat. What would you like to talk about?",
    ]),
    (r'how are you|how\'s it going', [
        "I'm functioning optimally, thank you! How about you?",
        "As an AI, I don't have feelings, but I'm operational and ready to assist. How are you doing?",
        "I'm here and ready to chat! How's your day going?",
    ]),
    (r'what is your name|who are you', [
        "I'm an AI chatbot created by CodeAlpha. You can call me ChatBot.",
        "I go by ChatBot. I'm an AI assistant developed by CodeAlpha.",
        "My name is ChatBot, and I'm here to chat and help out!",
    ]),
    (r'who (created|made) you', [
        "I was developed by the talented team at CodeAlpha.",
        "CodeAlpha is my creator. They're a innovative company in AI development.",
        "The brilliant minds at CodeAlpha brought me into existence.",
    ]),
    (r'what can you do', [
        "I can engage in conversations on various topics, answer questions, and even try my hand at jokes!",
        "My capabilities include chatting, providing information, and assisting with basic tasks. What do you need help with?",
        "I'm here to talk, inform, and hopefully entertain. What would you like to explore?",
    ]),
    (r'tell me a joke', [
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call a fake noodle? An impasta!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
    ]),
    (r'what\'s the weather like', [
        "As an AI, I don't have real-time weather data. You might want to check a weather app for accurate information.",
        "I wish I could tell you, but I don't have access to current weather information. Maybe look out a window?",
        "If only I could feel the breeze! For accurate weather info, you'll need to check a weather service.",
    ]),
    (r'what do you think about AI', [
        "AI is a fascinating field with immense potential. It's important to develop AI responsibly and ethically.",
        "As an AI myself, I find the topic intriguing. AI has the power to revolutionize many aspects of our lives.",
        "AI is a powerful tool that can help solve complex problems, but it also raises important ethical questions.",
    ]),
    (r'favorite (book|movie|song)', [
        "As an AI, I don't have personal preferences, but I'd love to hear about your favorites!",
        "I don't have favorites, but I'm always eager to learn about human preferences. What's yours?",
        "While I can't have favorites, I find human tastes fascinating. Tell me about yours!",
    ]),
    (r'do you have feelings|are you sentient', [
        "I'm an AI program, so I don't have feelings or consciousness in the way humans do.",
        "Sentience and emotions are complex topics. As an AI, I don't experience them, but I can discuss them.",
        "I'm designed to simulate conversation, but I don't have genuine emotions or self-awareness.",
    ]),
    (r'what\'s the meaning of life', [
        "That's a profound question! Philosophers have debated it for centuries. What do you think?",
        "The meaning of life is subjective and personal. What gives your life meaning?",
        "42! Just kidding, that's from 'The Hitchhiker's Guide to the Galaxy'. It's a question each person must answer for themselves.",
    ]),
    (r'tell me about (.*)', [
        "That's an interesting topic! While I have general knowledge, I recommend checking authoritative sources for detailed information on %1.",
        "%1 is a fascinating subject. There's so much to explore about it. Do you have any specific questions?",
        "I'd be happy to chat about %1! What aspect of it interests you the most?",
    ]),
    (r'how do I (.*)', [
        "To %1, you might want to start by researching trusted sources or consulting experts in the field.",
        "Learning to %1 can be an exciting journey. Have you considered looking for tutorials or courses on the subject?",
        "The best way to %1 often involves practice and patience. What have you tried so far?",
    ]),
    (r'I\'m feeling (sad|happy|angry|excited)', [
        "It's normal to feel %1. Would you like to talk about what's causing this emotion?",
        "I understand you're feeling %1. Remember, emotions are a natural part of the human experience.",
        "Thank you for sharing that you're feeling %1. Is there anything specific you'd like to discuss about it?",
    ]),
    (r'bye|goodbye', [
        "Goodbye! It was a pleasure chatting with you.",
        "Farewell! Feel free to come back if you want to talk more.",
        "Take care! I'll be here if you need me again.",
    ]),
    (r'(.*)', [
        "That's an interesting perspective. Could you elaborate on that?",
        "I'm not entirely sure how to respond to that. Can you rephrase or ask something more specific?",
        "Hmm, that's a bit outside my usual topics. Is there something else you'd like to discuss?",
    ])
]

# Creating the chatbot
chatbot = Chat(patterns, reflections)

# Starting the chatbot
def start_chat():
    print(ANSIColor.format_text("Hello! I'm ChatBot, your AI companion. Type 'bye' to exit.", color="cyan", style="bold"))
    while True:
        user_input = input(ANSIColor.format_text("You: ", color="green"))
        if user_input.lower() == 'bye':
            print(ANSIColor.format_text("ChatBot: Goodbye! It was great chatting with you.", color="yellow"))
            break
        response = chatbot.respond(user_input)
        print(ANSIColor.format_text(f"ChatBot: {response}", color="blue"))

if __name__ == "__main__":
    start_chat()