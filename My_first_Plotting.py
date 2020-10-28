import bokeh as bk
import numpy as np
from 
from bk.plotting import figure
from bk.plotting import output_file
from bk.plotting import show

def run():
    output_file('graficado_simple.html')
    fig = figure()
    total_vals = int(input('Cuantos valores quieres graficar? '))
    x_vals = list(range(total_vals))
    y_vals = []

    for i in x_vals:
        val = int(input(f'Valor y para x = {i}: '))
        y_vals.append(val)
    
    fig.line(x_vals, y_vals, line_width = 2)
    show(fig)

if __name__ == '__main__':
    run()