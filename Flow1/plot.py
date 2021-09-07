# plot.py

# Importing required Modules
from cmd_spin import spin
import plotly.graph_objects as go
import numpy as np

# Function to display (plot) table
def plottable(data, columns, tablehead = None):
    transpose_data = np.array(data).T.tolist()
    fig = go.Figure(data=[go.Table(header=dict(values=columns, fill_color = '#ff5754', line_color = 'darkslategrey'),cells=dict(values=transpose_data, fill_color = '#ff9896', line_color = 'darkslategrey'))])
    spin('Fetching and Tabulating Data...')
    fig.update_layout(title_text = tablehead)
    fig.show()

