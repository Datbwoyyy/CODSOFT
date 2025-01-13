import re
import tkinter as tk
from datetime import datetime

# Function to handle Chatbot Responses
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How may I be of assistance today?"
    elif "who are you" in user_input or "What are you" in user_input:
        return "I am a simple rule-based Chatbot. How can I help you?"
    elif "help" in user_input:
        return "Sure, I can help with general inquiries. Just ask a question or a myth."
    elif "bye" in user_input or "Goodbye" in user_input or "nice talking to you" in user_input:
        return "Goodbye! Have a great day!"
    elif re.search(r"weather in \w+", user_input):
        city = re.search(r"weather in (\w+)", user_input).group(1)
        return f"I can't provide real-time weather updates yet, but you can check online for the latest weather update in {city}."
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"

# Function to Send a Message
def send_message():
    user_input = entry.get()
    chat_log.insert(tk.END, f"You: {user_input}\n")
    response = chatbot_response(user_input)
    chat_log.insert(tk.END, f"Chatbot: {response}\n\n")
    entry.delete(0, tk.END)

# Creating the App
root = tk.Tk()
root.title("Simple Chatbot")

# Create a Chat log
chat_log = tk.Text(root, bg="lightgray", height=20, width=50)
chat_log.pack(pady=10)

# Creating an entry box for user input
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create a send Button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Run the application
root.mainloop()
