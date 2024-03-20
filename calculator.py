import tkinter as tk
from tkinter import ttk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Modern Calculator")
root.geometry("400x400")

style = ttk.Style()
style.configure("TButton", font=("Arial", 14), padding=10)
style.configure("TEntry", font=("Arial", 14), padding=10)

entry = ttk.Entry(root, width=20, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 4, 0) 
]

for (text, row, col) in buttons:
    if text == "=":
        button = ttk.Button(root, text=text, command=calculate)
    elif text == "C":
        button = ttk.Button(root, text=text, command=clear)
    else:
        button = ttk.Button(root, text=text, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
