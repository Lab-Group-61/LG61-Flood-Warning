# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .stationdata import build_station_list #temporary for testing

from .utils import sorted_by_key  # noqa

from .station import MonitoringStation

from haversine import haversine, Unit

station_list = build_station_list() # Build a list of stations (temporary for testing)

def stations_by_distance(stations,p):
    output = []
    for i in range(len(stations)):
        st_name_and_town = "{} in {}".format(stations[i].name,stations[i].town)
        st_id = (st_name_and_town,stations[i].coord)
        output.append(st_id)
    return(output)
