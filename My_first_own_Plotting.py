#-*- coding: utf-8 -*-
#sources : https://docs.bokeh.org/en/2.2.3/docs/user_guide/annotations.html
#          https://docs.bokeh.org/en/latest/docs/user_guide/plotting.html#specialized-curves
# This piece of code was made by Meluiscruz @ Oct 28th, 2020.

import bokeh
import numpy

from numpy import arange
from bokeh.plotting import figure, output_file, show

def run():
    x = arange(-3, 3, 0.01)
    y = 3*pow(x,5) - 25*pow(x,3) + 60*x +3 # <-- Your polynomial eq. here.

    output_file("Polynomial plot.html")
    p = figure(x_range = (-3.5, 3.5), y_range = (-50, 50))

    p.title.text = "Strain - Stress Plot"
    p.xaxis.axis_label = 'x value [mm]'
    p.yaxis.axis_label = 'y value [kPa]'
    p.line(x, y, color = 'green', line_width = 1.5)

    show(p)

if __name__ == '__main__':
    run()