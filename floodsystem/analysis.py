import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime, timedelta

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    time_shift = x[0]
    # Using shifted x values, find coefficient of best-fit
    p_coeff = np.polyfit(x-time_shift, y, p)
    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    return poly,time_shift

def grad(poly,time_shift, now):
    der = np.polyder(poly)
    return der(now - time_shift)