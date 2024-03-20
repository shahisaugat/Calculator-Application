import tkinter as tk

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

root = tk.Tk()
root.title("Basic Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14),
                         command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", width=10, height=2, font=("Arial", 14),
                             command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()
