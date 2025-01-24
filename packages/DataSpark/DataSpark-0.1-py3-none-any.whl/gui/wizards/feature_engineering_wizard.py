# gui/wizards/feature_engineering_wizard.py
import tkinter as tk
from tkinter import messagebox

class FeatureEngineeringWizard:
    def __init__(self, master, callback, data):
        self.master = master
        self.callback = callback
        self.data = data
        self.result = None
        self.top = tk.Toplevel(master)
        self.top.title("Feature Engineering Wizard")
        self.top.geometry("400x300")
        self.top.grab_set()
        
        tk.Label(self.top, text="Select Feature Engineering Options:").pack(pady=5)
        
        # Placeholder for feature engineering options
        self.options = {}
        for option in ["Normalize", "Log Transform", "Create Age Groups"]:
            var = tk.BooleanVar()
            tk.Checkbutton(self.top, text=option, variable=var).pack(anchor=tk.W)
            self.options[option] = var
        
        apply_button = tk.Button(self.top, text="Apply", command=self.apply_features)
        apply_button.pack(pady=10)

    def apply_features(self):
        from data_handling import apply_feature_engineering, example_feature_engineering
        
        selected_features = {k: v.get() for k, v in self.options.items() if v.get()}
        if not selected_features:
            messagebox.showwarning("Warning", "No features selected for engineering.")
            return

        # Apply selected features
        df = self.data.copy()
        
        if "Normalize" in selected_features:
            # Assume you have a normalize function in data_operations.py
            df = apply_feature_engineering(df, lambda d: normalize_feature(d, 'income'))
        
        if "Log Transform" in selected_features:
            # Assume you have a log transform function in data_operations.py
            df = apply_feature_engineering(df, lambda d: log_transform_feature(d, 'income'))
        
        if "Create Age Groups" in selected_features:
            df = apply_feature_engineering(df, example_feature_engineering)

        self.result = df
        self.callback(self.result)
        self.top.destroy()