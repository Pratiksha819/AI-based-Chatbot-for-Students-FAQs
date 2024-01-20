import random
import json
import tkinter as tk
from tkinter import ttk, messagebox

# Load the college dataset
with open('college_dataset.json') as file:
    college_data = json.load(file)

# Responses for different user inputs
greetings = ["Hello!", "Hi there!", "Greetings!", "Nice to meet you!"]
questions = ["What would you like to know about the college?", "How can I assist you with college information?"]
goodbyes = ["Goodbye!", "Have a great day!", "See you later!"]
welcome = ["You're welcome!", "My pleasure!", "Glad I  could help!"]

# Function to search for information in the dataset
def search_college_data(query):
    query = query.lower()
    response = "I'm sorry, I couldn't find the information you're looking for."

    # Search the dataset for matching keywords
    for data in college_data:
        keywords = data['keywords']
        if any(keyword in query for keyword in keywords):
            response = random.choice(data['responses'])
            break

    return response

# Function to generate a response
def generate_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return random.choice(greetings)
    elif "?" in user_input:
        return random.choice(questions)
    elif user_input in ["bye", "goodbye"]:
        return random.choice(goodbyes)
    elif user_input in ["thanks", "thank you"]:
        return random.choice(welcome)
    else:
        return search_college_data(user_input)

# Function to handle sending user input and displaying chat
def handle_send():
    user_text = user_input.get()
    if user_text.strip() == '':
        return

    response = generate_response(user_text)
    add_chat_message(user_text, '\nUser')
    add_chat_message(response, '\nChatbot')
    user_input.delete(0, tk.END)

# Function to add a chat message to the chat window
def add_chat_message(message, sender):
    chat_message = f'{sender}: \t{message}\n'
    chat_text.configure(state=tk.NORMAL)
    chat_text.insert(tk.END, chat_message)
    chat_text.configure(state=tk.DISABLED)
    chat_text.see(tk.END)

# Create the main GUI window
window = tk.Tk()
window.title("College Chatbot")

# Load college logo

# Create chat window
chat_frame = ttk.Frame(window, padding=10)
chat_frame.pack(expand=True, fill='both')
chat_text = tk.Text(chat_frame, height=15, wrap=tk.WORD, state=tk.DISABLED)
chat_text.pack(side=tk.LEFT, fill='both', expand=True)
chat_scrollbar = ttk.Scrollbar(chat_frame, command=chat_text.yview)
chat_scrollbar.pack(side=tk.RIGHT, fill='y')
chat_text.configure(yscrollcommand=chat_scrollbar.set)

# Create user input field
user_input = ttk.Entry(window, width=50)
user_input.bind("<Return>", lambda event: handle_send())
user_input.pack()
send_button = ttk.Button(window, text="Send", command=handle_send )
send_button.pack()


# Create send button

# Start the GUI event loop
window.mainloop()