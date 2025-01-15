# Chatbot with Rule-Based Responses (Tkinter GUI)

##  **README and Reference Document**
This document provides a detailed guide on how to build, run, and deploy a simple **rule-based chatbot** using **Python's Tkinter** library. The code provided here is **original** and serves as a template for educational purposes, ensuring no copyright concerns arise.

---

##  **Project Overview**
This project is a **simple chatbot application** with a **Graphical User Interface (GUI)** built using **Tkinter**. The chatbot responds to user queries based on predefined rules using **if-else conditions** and **pattern matching**. The GUI includes:
- A text area to display chat logs.
- An entry field for user input.
- A send button to submit queries.

---

## 📂 **Project Structure**
```
├── chatbot_gui.py      # Main Python file containing the chatbot logic and GUI code
└── README.md          # Documentation file (this file)
```

---

##  **Requirements**
- Python 3.6+

### **Built-in Libraries Used:**
- `tkinter` for the GUI.
- `re` for pattern matching.
- `datetime` for time-related responses.

No external libraries are required for this project.

---

##  **How to Run the Chatbot**

### **Step 1: Download the Project Files**
1. Download or copy the `chatbot.py` file.
2. Save it in your desired folder.

### **Step 2: Run the Chatbot**
1. Open **Command Prompt (CMD)** or **Terminal**.
2. Navigate to the folder where your `chatbot.py` file is saved:
   ```
   cd path/to/your/folder
   ```
3. Run the following command to launch the GUI:
   ```
   python chatbot.py
   ```
4. The chatbot window will appear, allowing you to chat with the bot.

---

##  **Code Explanation**
Here’s a breakdown of the key sections of the code:

### **1. Importing Libraries**
```python
import re
import tkinter as tk
from datetime import datetime
```
These libraries are used to handle regular expressions, create the GUI, and work with date/time data.

### **2. Chatbot Logic (Rule-Based Responses)**
```python
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "who are you" in user_input or "what are you" in user_input:
        return "I am a simple rule-based chatbot. How can I help you?"
    elif "help" in user_input:
        return "Sure! I can help you with general queries. Just ask me anything."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif re.search(r"weather in \w+", user_input):
        city = re.search(r"weather in (\w+)", user_input).group(1)
        return f"I can't provide real-time weather updates yet, but you can check online for the latest weather in {city}."
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase?"
```
This function handles user input and returns responses based on matching conditions.

### **3. GUI Design (Tkinter)**
```python
# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create a chat log
chat_log = tk.Text(root, bg="lightgray", height=20, width=50)
chat_log.pack(pady=10)

# Create an entry box for user input
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=5)

# Run the application
root.mainloop()
```
This code creates a simple GUI with a text log, entry box, and send button.

---

##  **Deploying the Chatbot as an Executable**
You can convert the Python script into a standalone executable using **PyInstaller**.

### **Step 1: Install PyInstaller**
```bash
pip install pyinstaller
```

### **Step 2: Create the Executable**
Run this command in your terminal:
```bash
pyinstaller --onefile --windowed chatbot_gui.py
```
The **`.exe` file** will be generated in the `dist/` folder.

---

##  **References**
- Official Python Documentation: https://docs.python.org/3/
- Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
- Regular Expressions (re) Module: https://docs.python.org/3/library/re.html

---

## 🔐 **Legal Disclaimer**
This project is an **original creation** for educational purposes. You are free to modify, distribute, and use it as long as proper credit is given. The author is not responsible for any misuse of this code.

