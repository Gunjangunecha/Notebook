import tkinter as tk
from tkinter import ttk

class NotePad:
    def __init__(self, root):
        self.root = root
        self.root.title("Python NotePad")
        self.root.geometry("800x600")

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        self.create_header()
        self.create_text_area()

        self.current_file = None
        self.is_locked = False

    def create_header(self):
        self.header_frame = ttk.Frame(self.root)
        self.header_frame.pack(side="top", fill="x", padx=5, pady=2)

        ttk.Button(self.header_frame, text="New", command=self.new_file).pack(side="left", padx=5)
        ttk.Button(self.header_frame, text="Open", command=self.open_file).pack(side="left", padx=5)
        ttk.Button(self.header_frame, text="Save", command=self.save_file).pack(side="left", padx=5)
        ttk.Button(self.header_frame, text="Lock", command=self.lock_file).pack(side="left", padx=5)
        ttk.Button(self.header_frame, text="Insert Picture", command=self.insert_picture).pack(side="left", padx=5)
        ttk.Button(self.header_frame, text="Calculator", command=self.open_calculator).pack(side="left", padx=5)
        ttk.Button(self.header_frame, text="Close Tab", command=self.close_current_tab).pack(side="left", padx=5)

    def create_text_area(self):
        self.text_area = tk.Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

    def new_file(self):
        new_frame = ttk.Frame(self.notebook)
        new_frame.pack(fill='both', expand=True)

        new_text = tk.Text(new_frame, wrap='word')
        new_text.pack(expand=True, fill='both')

        self.notebook.add(new_frame, text="New File")

    def open_file(self):
        pass

    def save_file(self):
        pass

    def lock_file(self):
        pass

    def insert_picture(self):
        pass

    def open_calculator(self):
        calculator_frame = ttk.Frame(self.notebook)
        calculator_frame.pack(fill='both', expand=True)

        calculator_label = ttk.Label(calculator_frame, text="Calculator")
        calculator_label.pack()

        self.calculator_entry = ttk.Entry(calculator_frame)
        self.calculator_entry.pack()

        button_frame = ttk.Frame(calculator_frame)
        button_frame.pack()

        operations = ['+', '-', '*', '/', '%']

        for operation in operations:
            ttk.Button(button_frame, text=operation, command=lambda op=operation: self.append_operation(op)).pack(side='left', padx=5)

        ttk.Button(button_frame, text="=", command=self.calculate_result).pack(side='left', padx=5)
        ttk.Button(button_frame, text="Clear", command=self.clear_entry).pack(side='left', padx=5)

        self.notebook.add(calculator_frame, text="Calculator")

    def append_operation(self, operation):
        self.calculator_entry.insert(tk.END, operation)

    def calculate_result(self):
        try:
            expression = self.calculator_entry.get()
            result = eval(expression)
            self.calculator_entry.delete(0, tk.END)
            self.calculator_entry.insert(0, str(result))
        except Exception as e:
            self.calculator_entry.delete(0, tk.END)
            self.calculator_entry.insert(0, "Error")

    def clear_entry(self):
        self.calculator_entry.delete(0, tk.END)

    def close_current_tab(self):
        selected_tab = self.notebook.select()
        if selected_tab:
            self.notebook.forget(selected_tab)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotePad(root)
    root.mainloop()
