import datetime

from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.flood import stations_highest_rel_level

from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.plot import plot_water_levels

def run():
    # Build list of stations
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)

    output_list = stations_highest_rel_level(station_list,5)

    for element in output_list:
        # Fetch data over past 10 days & plot graph
        dt = 10
        dates, levels = fetch_measure_levels(element[0].measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(element[0], dates, levels)

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()