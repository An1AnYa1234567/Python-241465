# Write a program to demonstrate Dynamic Interactive Image/File Viewer with Dialog Prompts.
import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox

# Create main window
root = tk.Tk()
root.title("File and Image Viewer")
root.geometry("600x500")

# Heading
title = tk.Label(root, text="File and Image Viewer",
                 font=("Arial", 18, "bold"))
title.pack(pady=10)

# Display label
info = tk.Label(root, text="Select a file to view",
                font=("Arial", 12))
info.pack(pady=5)

# Text area
text_area = tk.Text(root, height=12, width=60)
text_area.pack(pady=10)

# Canvas for image display
canvas = tk.Canvas(root, width=300, height=150, bg="white")
canvas.pack(pady=5)

# Open text or image file
def open_file(event=None):
    filename = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[
            ("Text Files", "*.txt"),
            ("Image Files", "*.png *.gif"),
            ("All Files", "*.*")
        ]
    )

    if not filename:
        return

    if filename.lower().endswith((".txt", ".py", ".csv")):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, content)
            info.config(text="Text File: " + filename.split("/")[-1])
            canvas.delete("all")

        except (OSError, UnicodeError) as error:
            messagebox.showerror("File Error", str(error))

    elif filename.lower().endswith((".png", ".gif")):
        try:
            image = tk.PhotoImage(file=filename)
            canvas.delete("all")
            canvas.image = image
            canvas.create_image(150, 75, image=image)
            info.config(text="Image: " + filename.split("/")[-1])
            text_area.delete("1.0", tk.END)

        except tk.TclError:
            messagebox.showerror(
                "Image Error",
                "Unable to open this image format."
            )
    else:
        messagebox.showwarning(
            "Unsupported File",
            "Please select a text or PNG/GIF image file."
        )

# Choose background color
def choose_color():
    color = colorchooser.askcolor(title="Choose Background Color")

    if color[1]:
        root.configure(bg=color[1])
        title.configure(bg=color[1])
        info.configure(bg=color[1])
        messagebox.showinfo("Color Selected", "Background color updated!")

# Mouse click event
def mouse_click(event):
    info.config(text="Mouse clicked at X={}, Y={}".format(
        event.x, event.y
    ))

# Buttons
tk.Button(root, text="Open File", command=open_file).pack(pady=5)
tk.Button(root, text="Choose Color", command=choose_color).pack(pady=5)

# Bind Enter key
root.bind("<Return>", open_file)

# Bind mouse click on canvas
canvas.bind("<Button-1>", mouse_click)

# Start application
root.mainloop()