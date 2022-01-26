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



def rivers_with_station(stations):
    # input (stations)：a list containing the names of stations
    # ouput (river_involved): The set containing names of rivers related to 
    # any of the station in the input list
    river_involved = []
    for station in stations:
        river_involved.append(station.river)
    return set(river_involved)

def stations_by_river(stations):
    # input: a list of stations
    # output (rivers_mapping) : a dictionary that maps the names of the rivers 
    # in the inputs to a list containing the related station names

    # initialize the dictionary with keywords
    # the river_with_station function is called to find the names of rivers
    river_mapping = {}
    the_rivers_involved = rivers_with_station(stations)
    for river in the_rivers_involved:
        river_mapping[river] = []
    
    # iterate over the stations to append them to the rivers 
    for station in stations:
        # append the stations to rivers
        river_mapping[station.river].append(station.name)
        
    return river_mapping