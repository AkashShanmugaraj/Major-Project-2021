from cmd_spin import spin
def plottable(data, columns, tablehead = None):
    import plotly.graph_objects as go
    import numpy as np
    import time
    transpose_data = np.array(data).T.tolist()
    fig = go.Figure(data=[go.Table(header=dict(values=columns, fill_color = '#ff5754', line_color = 'darkslategrey'),cells=dict(values=transpose_data, fill_color = '#ff9896', line_color = 'darkslategrey'))])
    spin('Fetching and Tabulating Data...')
    fig.update_layout(title_text = tablehead)
    fig.show()

