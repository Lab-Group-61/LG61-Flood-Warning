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
    # This function sorts a list of MonitoringStations by their distance from a point p
    output = []
    for i in range(len(stations)):
        st_name_and_town = "{} in {}".format(stations[i].name,stations[i].town)
        st_id = (st_name_and_town,haversine(p,stations[i].coord))
        output.append(st_id)
    sorted_output = sorted_by_key(output,1) 
    return(sorted_output)

def stations_within_radius(stations, centre, r):
    # This function produces a sorted list of station names within a radius of r from a designated centre
    output = []
    for i in range(len(stations)):
        if haversine(centre, stations[i].coord) <= r:
            output.append(stations[i].name)
    output.sort()
    return output


def rivers_with_station(stations):
    # input (stations)：a list containing the names of stations
    # ouput (river_involved): The set containing names of rivers related to any of the station
    river_involved = []
    for station in stations:
        river_involved.append(station.river)
    return set(river_involved)