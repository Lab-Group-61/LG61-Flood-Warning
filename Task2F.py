import datetime

from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.flood import stations_highest_rel_level

from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.plot import plot_water_levels

from floodsystem.analysis import polyfit

def run():
    # Build list of stations
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)

    output_list = stations_highest_rel_level(station_list,1)
    # each element in the list is a (station, relative water level) tuple, 
    # hence element[0] is the station

    for element in output_list:
        # Fetch data over past 2 days & plot graph
        dt = 2
        dates, levels = fetch_measure_levels(element[0].measure_id, dt=datetime.timedelta(days=dt))
        print(polyfit(dates, levels,4))

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()