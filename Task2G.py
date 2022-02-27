#Task 2G Classify each town into a level of flood danger
# Low: current water level within typical range (relative level <= 1)
# Moderate :  1 < Relative level <= 2 AND gradient from best-fit line < threshold value
# High: 2 <Relative level < 5 OR gradient >= threshold value
# Severe: Relative level >= 5
from pickle import FALSE, NONE
import numpy as np
import datetime
import matplotlib
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit, grad


def run():
    # find the current time
    now = matplotlib.dates.date2num(datetime.datetime.utcnow())
    threshold_gradient = 0.5

    # Build list of stations
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)

    low = []
    moderate = []
    high = []
    severe = []
    unclear_data = []
    # unclear data has inconsistent value of latest level or its gradient cannot be found

    for station in station_list:
        gradient = None
        
        if station.relative_water_level() == None or station.relative_water_level() >= 30:
            # throw away data with inconsistent value of water level
            unclear_data.append(station)
            continue
        
        elif station.relative_water_level() <= 1:
            low.append(station)

        else:
            # there may be error in fetching the data so a "try,except" format is used
            try:
                gradient = find_grad(station,now)

            except:
                unclear_data.append(station)
                continue

            if station.relative_water_level() <= 2 and gradient <= threshold_gradient:
                moderate.append(station)

            elif station.relative_water_level() <= 5 or gradient >= threshold_gradient:
                high.append(station)
            else:
                severe.append(station)
    print(len(low),len(moderate),len(high),len(severe),len(unclear_data))
    return

def find_grad(station,now):
    # Find the gradient of the change water level of the station now
    # Fetch data over past 2 days & plot graph
    dt = 2
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    poly, time_shift = polyfit(dates,levels,4)
    return grad(poly,time_shift,now)



if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()