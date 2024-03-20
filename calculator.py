import tkinter as tk
from tkinter import *

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except (SyntaxError, ZeroDivisionError):
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def toggle_theme():
    global dark_theme
    dark_theme = not dark_theme
    apply_theme()

def apply_theme():
    bg_color = "#000000" if dark_theme else "#FFFFFF"
    fg_color = "#FFFFFF" if dark_theme else "#000000"
    entry.config(background=bg_color, foreground=fg_color)
    button_bg_color = "#444444" if dark_theme else "#CCCCCC"
    button_fg_color = "#FFFFFF" if dark_theme else "#000000"
    for button in buttons:
        button.config(background=button_bg_color, foreground=button_fg_color)
    root.config(bg=bg_color)

# Create main window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("350x400")

# Create entry widget
entry = Entry(root, justify="right", width=20)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Define buttons
buttons = []
buttons_text = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 4, 0)  # Clear button
]
for (text, row, col) in buttons_text:
    if text == "=":
        button = Button(root, text=text, width=10, command=calculate)
    elif text == "C":
        button = Button(root, text=text, width=10, command=clear)
    else:
        button = Button(root, text=text, width=10, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    buttons.append(button)

# Toggle button for theme
dark_theme = False
theme_button = Button(root, text="Toggle Theme", command=toggle_theme)
theme_button.grid(row=5, column=0, columnspan=4, pady=(10, 0))

# Apply the initial theme
apply_theme()

# Column and row configuration
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Start the GUI
root.mainloop()
