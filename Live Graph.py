import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


plt.style.use("fivethirtyeight")

xvals = []
yvals = []

# counts up one number at a time
index = count()


def animate(i):
    # add values to x counting up by one
    xvals.append(next(index))
    # add random values to y
    yvals.append(random.randint(0, 5))

    # clear axis so graph has one line instead of multiple
    plt.cla()
    # plot data onto graph
    plt.plot(xvals, yvals)
    # plt.tight_layout()


# run animate function on specific interval

# parameters (plot figures in graph, pass function to run, interval for how often function should run (millisecond))
anim = FuncAnimation(plt.gcf(), animate, interval=1000)

# add padding to graph
plt.tight_layout()

# show graph
plt.show()
