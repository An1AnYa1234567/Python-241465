# Write a program to demonstrate Multi-Functional Graphical Desktop Calculator.
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Display field
entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Function to handle button clicks
def click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif value == "C":
        entry.delete(0, tk.END)

    else:
        entry.insert(tk.END, value)

# Calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons using grid
for (text, row, col) in buttons:
    button = tk.Button(
        root,
        text=text,
        font=("Arial", 16),
        width=5,
        height=2,
        command=lambda value=text: click(value)
    )
    button.grid(row=row, column=col, padx=3, pady=3)

# Run the application
root.mainloop()