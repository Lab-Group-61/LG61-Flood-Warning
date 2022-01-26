# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from .station import MonitoringStation

from haversine import haversine, Unit

def stations_by_distance(stations,p): 
    # This function sorts a list of MonitoringStations by their distance from a point p (Task 1B)
    output = []
    for i in range(len(stations)):
        st_id = (stations[i].name,stations[i].town,haversine(p,stations[i].coord))
        output.append(st_id)
    sorted_output = sorted_by_key(output,2) 
    return(sorted_output)

def stations_within_radius(stations, centre, r):
    # This function produces a sorted list of station names within a radius of r from a designated centre (Task 1C)
    output = []
    for i in range(len(stations)):
        if haversine(centre, stations[i].coord) <= r:
            output.append(stations[i].name)
    output.sort()
    return output


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