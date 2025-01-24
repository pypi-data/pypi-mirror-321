import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def plot_data(canvas, df, x_column='index', y_column='value'):
    """
    Plot data on the provided canvas.
    
    :param canvas: Tkinter Canvas widget
    :param df: pandas DataFrame to plot
    :param x_column: Column name for x-axis
    :param y_column: Column name for y-axis
    """
    fig, ax = plt.subplots(figsize=(4, 3), dpi=100)
    ax.plot(df[x_column], df[y_column])
    ax.set_title(f"{y_column} vs {x_column}")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    
    # Clear previous plots from the canvas
    if hasattr(canvas, 'chart'):
        canvas.chart.get_tk_widget().destroy()
    
    # Embed the figure in the canvas
    chart = FigureCanvasTkAgg(fig, master=canvas)
    chart.draw()
    chart.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Store reference to the chart for later use
    canvas.chart = chart