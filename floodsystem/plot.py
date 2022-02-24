from turtle import color
import matplotlib.dates
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
from floodsystem import analysis

def plot_water_levels(station, dates, levels):
    typical_range = station.typical_range
    # Plot
    plt.plot(dates, levels)
    plt.axhline(y=typical_range[0], color='g', linestyle ='--')
    plt.axhline(y=typical_range[1], color='r', linestyle ='--')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('dates')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water levels of {}".format(station.name))

    high_legend = mpatches.Patch(color='red', label='Typical High')
    low_legend = mpatches.Patch(color='green', label='Typical Low')
    level_legend = mpatches.Patch(color='blue', label='Current Water Level')

    plt.legend(handles=[high_legend,low_legend,level_legend])
    plt.tight_layout()
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    # plot the waterlevel data and the best-fit polynomial on the same diagram
    poly, time_shift = analysis.polyfit(dates,levels,p)
    predicted_levels = []
    for date in dates:
        predicted_levels.append(poly(matplotlib.dates.date2num(date)-time_shift))

    typical_range = station.typical_range
    # Plot
    #plt.plot(dates, levels)
    plt.plot(dates,predicted_levels,color='y')
    plt.plot(dates,levels,color='b')
    plt.axhline(y=typical_range[0], color='g', linestyle ='--')
    plt.axhline(y=typical_range[1], color='r', linestyle ='--')

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('dates')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water levels of {}".format(station.name))

    high_legend = mpatches.Patch(color='red', label='Typical High')
    low_legend = mpatches.Patch(color='green', label='Typical Low')
    level_legend = mpatches.Patch(color='blue', label='Current Water Level')
    poly_fit_legend = mpatches.Patch(color = 'yellow', label='Best-fit Water Level')

    plt.legend(handles=[high_legend,low_legend,level_legend,poly_fit_legend])
    plt.tight_layout()
    plt.show()
    return