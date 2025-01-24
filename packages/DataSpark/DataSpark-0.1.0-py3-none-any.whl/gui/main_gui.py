import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from data_handling import load_data, save_data
from gui.wizards import ImportWizard, FeatureEngineeringWizard
from visualization.visualization_functions import plot_data
import pandas as pd

class DataSparkGUI:
    def __init__(self, master):
        self.master = master
        master.title("DataSpark")
        
        # Menu Bar
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)
        
        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Load Data", command=self.load_data_wizard)
        self.file_menu.add_command(label="Save Data", command=self.save_data)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        # Analysis Menu
        self.analysis_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.analysis_menu.add_command(label="Feature Engineering", command=self.feature_engineering_wizard)
        self.analysis_menu.add_command(label="Visualize Data", command=self.visualize_data)
        self.menu_bar.add_cascade(label="Analysis", menu=self.analysis_menu)
        
        # Help Menu
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Give Feedback", command=self.give_feedback)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)
        
        # Main Frame
        self.main_frame = ttk.Frame(master, padding="3 3 12 12")
        self.main_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        
        # Data Display Area
        self.data_frame = tk.Frame(self.main_frame)
        self.data_frame.grid(column=0, row=0, sticky=tk.W+tk.E, padx=5, pady=5)
        self.data_view = tk.Text(self.data_frame, height=20, width=80)
        self.data_view.grid(column=0, row=0, sticky=tk.W+tk.E)
        self.scrollbar = tk.Scrollbar(self.data_frame, command=self.data_view.yview)
        self.scrollbar.grid(column=1, row=0, sticky=tk.N+tk.S)
        self.data_view['yscrollcommand'] = self.scrollbar.set
        
        # Placeholder for Chart
        self.chart_frame = tk.Frame(self.main_frame, width=400, height=300)
        self.chart_frame.grid(column=0, row=1, padx=5, pady=5)
        self.chart_canvas = tk.Canvas(self.chart_frame, width=400, height=300)
        self.chart_canvas.pack()

        # Offline Mode Toggle
        self.offline_mode = tk.BooleanVar(value=False)
        self.offline_check = tk.Checkbutton(self.main_frame, text="Offline Mode", variable=self.offline_mode, command=self.toggle_offline_mode)
        self.offline_check.grid(column=0, row=2, sticky=tk.W)

        # Interactive Elements
        self.interactive_button = tk.Button(self.main_frame, text="Interactive Feature", command=self.interactive_feature)
        self.interactive_button.grid(column=0, row=3, pady=10)

    def load_data_wizard(self):
        ImportWizard(self.master, self.on_data_imported)

    def on_data_imported(self, data):
        self.current_data = data['data']
        self.display_data(self.current_data)
        messagebox.showinfo("Success", "Data imported successfully!")

    def save_data(self):
        if hasattr(self, 'current_data'):
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if file_path:
                save_data(self.current_data, file_path)
                messagebox.showinfo("Success", "Data saved successfully!")
        else:
            messagebox.showerror("Error", "No data to save!")

    def feature_engineering_wizard(self):
        if hasattr(self, 'current_data'):
            FeatureEngineeringWizard(self.master, self.on_feature_engineered, self.current_data)
        else:
            messagebox.showerror("Error", "Please load data first!")

    def on_feature_engineered(self, data):
        self.current_data = data
        self.display_data(data)
        messagebox.showinfo("Success", "Feature engineering applied!")

    def visualize_data(self):
        if hasattr(self, 'current_data'):
            plot_data(self.chart_canvas, self.current_data)
        else:
            messagebox.showerror("Error", "Please load data first!")

    def toggle_offline_mode(self):
        if self.offline_mode.get():
            messagebox.showinfo("Offline Mode", "Now in offline mode. Some features might be limited.")
        else:
            messagebox.showinfo("Online Mode", "Back to online mode. Full features available.")

    def interactive_feature(self):
        # Placeholder for an interactive feature, like data filtering or dynamic chart updates
        messagebox.showinfo("Interactive Feature", "This feature will be interactive!")

    def display_data(self, data):
        self.data_view.delete(1.0, tk.END)
        self.data_view.insert(tk.END, data.head().to_string())

    def give_feedback(self):
        feedback_window = tk.Toplevel(self.master)
        feedback_window.title("Give Feedback")
        feedback_window.geometry("300x200")
        
        tk.Label(feedback_window, text="Your Feedback:").pack(pady=5)
        feedback_entry = tk.Text(feedback_window, height=5, width=30)
        feedback_entry.pack(pady=5)
        
        submit_button = tk.Button(feedback_window, text="Submit", command=lambda: self.submit_feedback(feedback_entry.get("1.0", tk.END)))
        submit_button.pack(pady=10)

    def submit_feedback(self, feedback):
        # Here you would typically save feedback to a file or send it via email
        with open('feedback.txt', 'a') as f:
            f.write(feedback + '\n')
        messagebox.showinfo("Feedback", "Thank you for your feedback!")

if __name__ == "__main__":
    root = tk.Tk()
    gui = DataSparkGUI(root)
    root.mainloop()