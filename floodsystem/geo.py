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
    for station in stations:
        st_id = (station.name,station.town,haversine(p,station.coord))
        output.append(st_id)
    sorted_output = sorted_by_key(output,2) 
    return(sorted_output)

def stations_within_radius(stations, centre, r):
    # This function produces a sorted list of station names within a radius of r from a designated centre (Task 1C)
    output = []
    for station in stations:
        if haversine(centre, station.coord) <= r:
            output.append(station.name)
    output.sort()
    return output


def rivers_with_station(stations):
    # input (stations)：a list containing the names of stations
    # ouput (river_involved): The list containing names of rivers related to 
    # any of the station in the input list
    river_involved = []
    for station in stations:
        river_involved.append(station.river)
    return sorted(list(set(river_involved)))

def stations_by_river(stations):
    # Input: a list of stations
    # Output (rivers_mapping) : a dictionary that maps the names of the rivers in the inputs 
    # to a list containing the related station names(sorted)

    # initialize the dictionary with keywords (rivers)
    # the river_with_station function is called to find the names of rivers
    river_mapping = {}
    the_rivers_involved = rivers_with_station(stations)
    for river in the_rivers_involved:
        river_mapping[river] = []
    
    # iterate over the stations to append them to the rivers 
    for station in stations:
        # append the stations to rivers
        river_mapping[station.river].append(station.name)

    # sort the stations on each river in alphabetical order
    for key in river_mapping:
        river_mapping[key] = sorted(river_mapping[key])
        
    return river_mapping

def rivers_by_station_number(stations, N):
    # input: a list of stations and an integer N
    # output: a list containing first Nth stations with largest number of stations

    # calling station_by_river(in task 1D, part 2) to find the river->station dictionary
    input_rivers = stations_by_river(stations)
    
    # if N is out of range:
    if N not in range(0,len(input_rivers)+1):
        raise ValueError("the N is not in the correct range")
    
    # temp is a list, each element is a (river,station number) tuple
    temp = []
    for key in input_rivers:
        temp.append((key,len(input_rivers[key])))

    # sorted temp by station number
    sorted_river = sorted_by_key(temp,1, reverse= True)
    
    # include the rivers with repeated number of stations into the output
    repeated_index = True # to record if there is any repitition
    i = N # i is the actually size of output list. i = N + repeated number of river at position N
    while repeated_index == True:
        if i < len(sorted_river) and sorted_river[i][1] == sorted_river[i-1][1]:
            i += 1
        else:
            repeated_index = False
    
    # return the first ith tuples
    return sorted_river[0:i]