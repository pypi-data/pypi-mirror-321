import unittest
import tkinter as tk
from visualization.visualization_functions import plot_data
import pandas as pd

class TestVisualization(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()
        self.sample_data = pd.DataFrame({
            'x': [1, 2, 3],
            'y': [2, 4, 5]
        })

    def test_plot_data(self):
        plot_data(self.canvas, self.sample_data, 'x', 'y')
        # Since we're in a test environment, we can't visually check the plot. 
        # Instead, we'll check if the canvas has children (indicating a plot was added).
        self.assertTrue(len(self.canvas.winfo_children()) > 0)

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()