#Task 2G Classify each town into a level of flood danger
# Low: current water level within typical range (relative level <= 1)
# Moderate :  1 < Relative level <= 2 AND gradient from best-fit line < threshold value
# High: 2 <Relative level < 5 OR gradient >= threshold value
# Severe: Relative level >= 5
from lib2to3.pgen2 import grammar
import numpy as np
import datetime
import matplotlib
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit, grad

def find_grad(station,now):
    # Find the gradient of best-fit polynomial at this moment
    # Fetch data over past 2 days & plot graph
    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    poly, time_shift = polyfit(dates,levels,4)
    return grad(poly,time_shift,now)

def run():
    # find the current time, this time is used to find the gradient of curve at this instant
    now = matplotlib.dates.date2num(datetime.datetime.utcnow())
    # The threshold gradient
    threshold_gradient = 0.5

    # Build list of stations
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)

    #set up the different classes
    low = []
    moderate = []
    high = []
    severe = []
    # unclear data either has no value for latest level or its gradient cannot be found
    unclear_data = []

    # iterate through all stations
    for station in station_list:
        
        # throw away data with no or absurb value of water level
        if station.relative_water_level() == None or station.relative_water_level() >= 30:
            unclear_data.append(station)
            continue
        
        # filter stations into low-danger level
        elif station.relative_water_level() <= 1:
            low.append(station)

        # continue filter stations into other levels
        else:
            # gradient is needed to filter stations into other levels
            gradient = None
            
            # find the gradient of the water-level against time diagram at this instant
            try:
                gradient = find_grad(station,now)

            except:
            # for some stations, it may not be able to calculate the gradient,
            # hence they are filtered into unclear data
                unclear_data.append(station)
                continue
            
            # filter stations into modereate-danger level
            if station.relative_water_level() <= 2 and gradient <= threshold_gradient:
                moderate.append(station)

            # filter stations into high-danger level
            elif station.relative_water_level() <= 5 or gradient >= threshold_gradient:
                high.append(station)
            
            # filter stations into severe-danger level
            else:
                # add this station into severe
                severe.append(station)

    # print out the results
    print("The stations under severe danger are:")
    for station in severe:
        print(station.name)
    print("The stations under high danger are:")
    for station in high:
        print(station.name)
    print("The stations under modereate danger are:")
    for station in moderate:
        print(station.name)
    print("The stations with unclear data are:")
    for station in unclear_data:
        print(station.name)
    return




if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()