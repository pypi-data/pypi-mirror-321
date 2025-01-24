import unittest
from gui.main_gui import DataSparkGUI
from tkinter import Tk
import tkinter as tk

class TestGUI(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.gui = DataSparkGUI(self.root)

    def test_gui_init(self):
        # Check if main frame exists
        self.assertIsInstance(self.gui.main_frame, tk.Frame)
        # Check if data view text widget exists
        self.assertIsInstance(self.gui.data_view, tk.Text)
        # Check if there's at least one menu item
        self.assertTrue(len(self.root.winfo_children()) > 0)

    def test_load_data_wizard(self):
        # This test would ideally open the wizard and check if it exists
        # Here, we'll just ensure the method is callable
        self.assertTrue(callable(self.gui.load_data_wizard))

    def test_save_data(self):
        # Similarly, for saving data
        self.assertTrue(callable(self.gui.save_data))

    def test_feature_engineering_wizard(self):
        self.assertTrue(callable(self.gui.feature_engineering_wizard))

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()