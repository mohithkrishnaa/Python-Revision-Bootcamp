# Tkinter
# Tkinter is the standard GUI (Graphical User Interface) library for Python.
# It provides a simple way to create windows, dialogs, buttons, and other GUI elements in your Python applications.

import tkinter as tk
from tkinter import messagebox

# Function to be called when the button is clicked
def some_function():
    messagebox.showinfo("Message", "You clicked the button")

# Create a new Tkinter window
root = tk.Tk()

# Set the window title
root.title("My First GUI Application")

#Tkinter widgets
#Label: Display static text or images.
#Button: Create clickable buttons to trigger actions.
#Entry: Allow user input for single-line text.
#Frame: Organize widgets within a container.

# Create and pack a label
label = tk.Label(root, text="Welcome to my first GUI application")
label.pack()

# Create and pack a button
button = tk.Button(root, text="Click me", command=some_function)
button.pack()

# Create and pack an entry (single-line text input)
entry = tk.Entry(root)
entry.pack()

# Create and pack a text (multiline text input)
text = tk.Text(root)
text.pack()

# Create and pack a frame to organize widgets within a container
frame = tk.Frame(root)
frame.pack()

# Start the Tkinter event loop
root.mainloop()
