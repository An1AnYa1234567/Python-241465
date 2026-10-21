# Write a program to demonstrate Modular Multi-Frame Graphical Dashboard Application.
import tkinter as tk
from tkinter import messagebox
import json
import os

CONFIG_FILE = "dashboard_config.json"


# Model: Stores application data
class DashboardModel:
    def __init__(self):
        self.config = {
            "username": "Guest",
            "theme": "Light"
        }

    def save_config(self):
        with open(CONFIG_FILE, "w") as file:
            json.dump(self.config, file, indent=4)

    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as file:
                self.config = json.load(file)


# View and Controller: GUI and event handling
class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Screen Dashboard")
        self.root.geometry("600x400")

        self.model = DashboardModel()
        self.model.load_config()

        # Menu bar
        menu_bar = tk.Menu(root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Save Configuration",
                              command=self.save_config)
        file_menu.add_command(label="Exit", command=self.exit_app)

        menu_bar.add_cascade(label="File", menu=file_menu)

        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_command(label="Dashboard",
                              command=self.show_dashboard)
        view_menu.add_command(label="Settings",
                              command=self.show_settings)

        menu_bar.add_cascade(label="View", menu=view_menu)
        root.config(menu=menu_bar)

        # Navigation frame
        self.nav_frame = tk.Frame(root, bg="lightgray")
        self.nav_frame.pack(side="left", fill="y")

        tk.Button(self.nav_frame, text="Dashboard",
                  command=self.show_dashboard).pack(padx=10, pady=10)

        tk.Button(self.nav_frame, text="Settings",
                  command=self.show_settings).pack(padx=10, pady=10)

        # Main content frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(side="right", expand=True, fill="both")

        self.show_dashboard()

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Dashboard",
                 font=("Arial", 20, "bold")).pack(pady=20)

        tk.Label(
            self.main_frame,
            text="Welcome, " + self.model.config["username"]
        ).pack(pady=10)

        tk.Label(
            self.main_frame,
            text="Current Theme: " + self.model.config["theme"]
        ).pack(pady=10)

    def show_settings(self):
        self.clear_frame()

        tk.Label(self.main_frame, text="Settings",
                 font=("Arial", 20, "bold")).grid(
                     row=0, column=0, columnspan=2, pady=20
                 )

        tk.Label(self.main_frame, text="Username:").grid(
            row=1, column=0, padx=10, pady=10
        )

        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=10)
        self.username_entry.insert(
            0, self.model.config["username"]
        )

        tk.Label(self.main_frame, text="Theme:").grid(
            row=2, column=0, padx=10, pady=10
        )

        self.theme_var = tk.StringVar(
            value=self.model.config["theme"]
        )

        tk.Radiobutton(
            self.main_frame, text="Light",
            variable=self.theme_var, value="Light"
        ).grid(row=2, column=1, sticky="w")

        tk.Radiobutton(
            self.main_frame, text="Dark",
            variable=self.theme_var, value="Dark"
        ).grid(row=3, column=1, sticky="w")

        tk.Button(
            self.main_frame, text="Apply Settings",
            command=self.apply_settings
        ).grid(row=4, column=0, columnspan=2, pady=20)

    def apply_settings(self):
        username = self.username_entry.get().strip()

        if not username:
            messagebox.showwarning(
                "Warning", "Username cannot be empty!"
            )
            return

        self.model.config["username"] = username
        self.model.config["theme"] = self.theme_var.get()

        self.save_config()
        messagebox.showinfo(
            "Success", "Settings updated successfully!"
        )
        self.show_dashboard()

    def save_config(self):
        try:
            self.model.save_config()
            messagebox.showinfo(
                "Saved", "Configuration saved successfully!"
            )
        except OSError as error:
            messagebox.showerror("File Error", str(error))

    def exit_app(self):
        if messagebox.askyesno(
            "Exit", "Do you want to exit the application?"
        ):
            self.root.destroy()


# Main application
root = tk.Tk()
app = DashboardApp(root)
root.mainloop()