# gui/wizards/import_wizard.py
import tkinter as tk
from tkinter import filedialog, messagebox
from data_handling import load_data

class ImportWizard:
    def __init__(self, master, callback):
        self.master = master
        self.callback = callback
        self.result = None
        self.top = tk.Toplevel(master)
        self.top.title("Data Import Wizard")
        self.top.geometry("400x300")
        self.top.grab_set()  # Makes this window modal
        
        self.file_type_var = tk.StringVar(value="csv")
        tk.Label(self.top, text="Select File Type:").pack(pady=5)
        for text, value in [("CSV", "csv"), ("JSON", "json"), ("Excel", "excel")]:
            tk.Radiobutton(self.top, text=text, variable=self.file_type_var, value=value).pack(anchor=tk.W)

        self.preview_text = tk.Text(self.top, height=10, width=50)
        self.preview_text.pack(pady=5)
        
        load_button = tk.Button(self.top, text="Browse File", command=self.browse_file)
        load_button.pack(pady=10)
        
        import_button = tk.Button(self.top, text="Import Data", command=self.import_data)
        import_button.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[
            ("CSV files", "*.csv"), ("JSON files", "*.json"), ("Excel files", "*.xlsx")])
        if file_path:
            self.file_path = file_path
            self.preview_text.delete(1.0, tk.END)
            try:
                data = load_data(file_path, self.file_type_var.get())
                self.preview_text.insert(tk.END, data.head().to_string())
            except Exception as e:
                self.preview_text.insert(tk.END, f"Error previewing data: {str(e)}")

    def import_data(self):
        if hasattr(self, 'file_path'):
            try:
                data = load_data(self.file_path, self.file_type_var.get())
                self.result = {"data": data, "file_type": self.file_type_var.get()}
                self.callback(self.result)
                self.top.destroy()
            except Exception as e:
                messagebox.showerror("Import Error", f"Failed to import data: {str(e)}")
        else:
            messagebox.showerror("Error", "Please select a file first.")