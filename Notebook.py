import tkinter as tk
from tkinter import ttk, filedialog, Text, messagebox
import os
from datetime import datetime

class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("Untitled - Notepad")
        self.file_path = None

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both')

        self.create_menu()

        self.time_date_label = tk.Label(self.master, text="", anchor="e", padx=10)
        self.time_date_label.pack(side="top", fill="x")

        self.update_time_date()
        self.master.after(1000, self.update_time_date)

    def create_menu(self):
        menu_bar = tk.Menu(self.master)
        self.master.config(menu=menu_bar)

        menu_bar.add_command(label="New", command=self.new_file)
        menu_bar.add_command(label="Open", command=self.open_file)
        menu_bar.add_command(label="Save", command=self.save_file)
        menu_bar.add_separator()
        menu_bar.add_command(label="Exit", command=self.quit_application)

    def update_time_date(self):
        now = datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        self.time_date_label.config(text=formatted_datetime)

    def new_file(self):
        # Implement logic for creating a new file
        tab = NotepadTab(self.notebook)
        self.notebook.add(tab, text="Untitled")
        self.notebook.select(tab)

    def open_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file_path:
            self.file_path = file_path
            self.master.title(os.path.basename(self.file_path) + " - Notepad")
            self.notebook.delete(1.0, tk.END)

            try:
                with open(self.file_path, "r") as file:
                    self.notebook.insert(1.0, file.read())
            except FileNotFoundError as e:
                messagebox.showerror("Error", str(e))

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file_path:
            self.file_path = file_path
            self.master.title(os.path.basename(self.file_path) + " - Notepad")

            try:
                with open(self.file_path, "w") as file:
                    file.write(self.notebook.get(1.0, tk.END))
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def quit_application(self):
        self.master.destroy()

class NotepadTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.notepad = Text(self, wrap='word')
        self.notepad.pack(expand=True, fill='both')

        self.close_button = tk.Button(self, text="Close", command=self.close)
        self.close_button.pack(side="right")

    def close(self):
        self.master.forget(self)

if __name__ == "__main__":
    root = tk.Tk()
    notepad = Notepad(root)
    root.mainloop()
