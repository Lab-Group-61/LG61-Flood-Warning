import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime, timedelta

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels
    p_coeff = np.polyfit(x, y, p)
    return p_coeff