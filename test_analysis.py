"""Uni-test for analysis.py (Task 2F)"""
import datetime

from numpy import poly1d

from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.flood import stations_highest_rel_level

from floodsystem.datafetcher import fetch_measure_levels

from floodsystem.plot import plot_water_levels,plot_water_level_with_fit

from floodsystem.analysis import polyfit

import numpy as np

def test_polyfit():
    # Build list of stations
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)

    output_list = stations_highest_rel_level(station_list,5)
    # each element in the list is a (station, relative water level) tuple, 
    # hence element[0] is the station

    for element in output_list:
        # Fetch data over past 2 days & plot graph
        dt = 2
        dates, levels = fetch_measure_levels(element[0].measure_id, dt=datetime.timedelta(days=dt))
        temp = polyfit(dates,levels,4)
        assert len(temp) == 2
        assert type(temp[0]) is np.poly1d
        assert temp[1] >= 19000
        assert np.size(temp[0]) == 5
    return
