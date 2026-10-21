# Write a program to demonstrate GUI Student Record Manager with File Storage.
import tkinter as tk
from tkinter import filedialog, messagebox

# Store student records
students = {}

# Create main window
root = tk.Tk()
root.title("Student Record Management")
root.geometry("500x600")

# Student details
tk.Label(root, text="Student Record Management",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Roll Number").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Gender").pack()
gender = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male", variable=gender,
               value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender,
               value="Female").pack()

tk.Label(root, text="Skills").pack()
python_var = tk.IntVar()
cpp_var = tk.IntVar()

tk.Checkbutton(root, text="Python",
               variable=python_var).pack()
tk.Checkbutton(root, text="C++",
               variable=cpp_var).pack()

tk.Label(root, text="Address").pack()
address_text = tk.Text(root, height=3, width=35)
address_text.pack(pady=5)

# Add student record
def add_student():
    roll = roll_entry.get().strip()
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    address = address_text.get("1.0", tk.END).strip()

    if not roll or not name or not age:
        messagebox.showerror("Error", "Fill all required fields!")
        return

    if roll in students:
        messagebox.showerror("Error", "Roll number already exists!")
        return

    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid age!")
        return

    skills = []
    if python_var.get():
        skills.append("Python")
    if cpp_var.get():
        skills.append("C++")

    students[roll] = {
        "Name": name,
        "Age": age,
        "Gender": gender.get(),
        "Skills": ", ".join(skills) or "None",
        "Address": address
    }

    messagebox.showinfo("Success", "Student record added!")
    clear_fields()

# View student record
def view_student():
    roll = roll_entry.get().strip()

    if roll not in students:
        messagebox.showerror("Error", "Student not found!")
        return

    record = students[roll]
    output.delete("1.0", tk.END)
    output.insert(tk.END, f"Roll Number: {roll}\n")

    for key, value in record.items():
        output.insert(tk.END, f"{key}: {value}\n")

# Delete student record
def delete_student():
    roll = roll_entry.get().strip()

    if roll in students:
        del students[roll]
        messagebox.showinfo("Success", "Record deleted!")
        output.delete("1.0", tk.END)
    else:
        messagebox.showerror("Error", "Student not found!")

# Save records to a file
def save_records():
    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for roll, record in students.items():
                    file.write(f"Roll Number: {roll}\n")
                    for key, value in record.items():
                        file.write(f"{key}: {value}\n")
                    file.write("-" * 30 + "\n")

            messagebox.showinfo("Success", "Records saved successfully!")
        except OSError as error:
            messagebox.showerror("File Error", str(error))

# Load records from a file
def load_records():
    filename = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )

    if filename:
        try:
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()

            output.delete("1.0", tk.END)
            output.insert(tk.END, content)
        except OSError as error:
            messagebox.showerror("File Error", str(error))

# Clear input fields
def clear_fields():
    roll_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    address_text.delete("1.0", tk.END)
    gender.set("Male")
    python_var.set(0)
    cpp_var.set(0)

# Buttons
tk.Button(root, text="Add Student",
          command=add_student).pack(pady=4)

tk.Button(root, text="View Student",
          command=view_student).pack(pady=4)

tk.Button(root, text="Delete Student",
          command=delete_student).pack(pady=4)

tk.Button(root, text="Save Records",
          command=save_records).pack(pady=4)

tk.Button(root, text="Load File",
          command=load_records).pack(pady=4)

tk.Label(root, text="Student Record Output",
         font=("Arial", 11, "bold")).pack(pady=5)

output = tk.Text(root, height=8, width=45)
output.pack(pady=5)

root.mainloop()