"""Uni-test for flood module"""
import datetime

import pytest

from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.flood import stations_highest_rel_level

from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.plot import plot_water_levels,plot_water_level_with_fit

from floodsystem.analysis import polyfit

def plot_water_level_with_fit(station, dates, levels, p):
    # Test for the second function in Task 2F
    # Test by check the error raised when there is one missing input


    # Build list of stations
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)

    output_list = stations_highest_rel_level(station_list,2)
    # each element in the list is a (station, relative water level) tuple, 
    # hence element[0] is the station

    for element in output_list:
        # Fetch data over past 2 days & plot graph
        dt = 2
        dates, levels = fetch_measure_levels(element[0].measure_id, dt=datetime.timedelta(days=dt))
        with pytest.raises(TypeError):
            # I deliberately missed the input paramenter "p"
            plot_water_level_with_fit(element[0],dates,levels)
    return