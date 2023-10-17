import random

dataset = {
    "greetings": ["Hello!", "Hi!", "Hey there!", "Greetings!"],
    "farewell": ["Goodbye!", "Bye!", "See you later!", "Take care!"],
    "thanks": ["Thank you!", "Thanks a lot!", "Thanks! I appreciate it!"],
    "unknown": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure I follow."],
}


def chatbot():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input or "hey" in user_input:
            print("Chatbot: " + random.choice(dataset["greetings"]))
        elif "goodbye" in user_input or "bye" in user_input:
            print("Chatbot: " + random.choice(dataset["farewell"]))
            break
        elif "thank you" in user_input or "thanks" in user_input:
            print("Chatbot: " + random.choice(dataset["thanks"]))
            break
        elif "How are you" in user_input or "are you ok" in user_input:
            print("Chatbot: I am fine,what about you?")
            break
        elif "fine" in user_input or "good" in user_input:
            print("Chatbot: " + "Good to hear")
            break
        else:
            print("Chatbot: " + random.choice(dataset["unknown"]))

# Run the chatbot
chatbot()

