#!/bin/python
# From:
#  https://stackoverflow.com/questions/6697259/interactive-matplotlib-plot-with-two-sliders
from numpy import pi, sin
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
import math

# Draw the plot
def do_plot(sigstr):
    def signal(t):
        return eval(sigstr)

    axis_color = 'lightgoldenrodyellow'

    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Adjust the subplots region to leave some space for the sliders and buttons
    fig.subplots_adjust(left=0.25, bottom=0.25)

    x_axis = 2*pi
    #t = np.arange(0.0, x_axis, x_axis/1000)
    t = np.linspace(0, x_axis, num=1000)

    # Draw the initial plot
    # The 'line' variable is used for modifying the line later
    [line] = ax.plot(t, signal(t), linewidth=2, color='red')
    ax.set_xlim([0, x_axis])
    ax.set_ylim([-10, 10])

    # Add two sliders for tweaking the parameters

    # Define an axes area and draw a slider in it
    xax_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], axisbg=axis_color)
    xax_slider = Slider(xax_slider_ax, 'X-Axis', pi/64, 64*pi, valinit=x_axis)

    # Draw another slider
    #freq_slider_ax = fig.add_axes([0.25, 0.1, 0.65, 0.03], axisbg=axis_color)
    #freq_slider = Slider(freq_slider_ax, 'Freq', 0.1, 30.0, valinit=freq_0)

    # Define an action for modifying the line when any slider's value changes
    def sliders_on_changed(val):
        x_axis = val
        #t = np.arange(0.0, x_axis, x_axis/1000)
        t = np.linspace(0, x_axis, num=1000)
        [line] = ax.plot(t, signal(t), linewidth=2, color='red')
        print (x_axis)
        ax.set_xlim([0, x_axis])
        line.set_ydata(signal(t))
        fig.canvas.draw_idle()
    xax_slider.on_changed(sliders_on_changed)
    #freq_slider.on_changed(sliders_on_changed)

    # Add a button for resetting the parameters
    reset_button_ax = fig.add_axes([0.8, 0.025, 0.1, 0.04])
    reset_button = Button(reset_button_ax, 'Reset', color=axis_color, hovercolor='0.975')
    def reset_button_on_clicked(mouse_event):
        #freq_slider.reset()
        xax_slider.reset()
    reset_button.on_clicked(reset_button_on_clicked)

    # Add a set of radio buttons for changing color
    color_radios_ax = fig.add_axes([0.025, 0.5, 0.15, 0.15], axisbg=axis_color)
    color_radios = RadioButtons(color_radios_ax, ('red', 'blue', 'green'), active=0)
    def color_radios_on_clicked(label):
        line.set_color(label)
        fig.canvas.draw_idle()
    color_radios.on_clicked(color_radios_on_clicked)

    plt.show()

### MAIN
if __name__ == '__main__':
    while (True):
        sigstr = input("---> ")
        do_plot(sigstr)
