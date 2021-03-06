"""Unit test for the geo submodule"""
from turtle import distance
from numpy import sort
import pytest
import floodsystem.geo
import floodsystem.station
import floodsystem.stationdata

# The station list is here:
station_list = floodsystem.stationdata.build_station_list()

def test_stations_by_distance(): # Test for Task 1B
    x = (0.0 , 0.0)
    sorted_list = floodsystem.geo.stations_by_distance(station_list,x)
    assert type(sorted_list) is list
    assert type(sorted_list[0]) is tuple 

    distances = []
    for i in sorted_list:
        distances.append(i[2])
    assert all(distances[i] <= distances[i+1] for i in range(len(distances) - 1)) == True # Checking that the list is sorted properly

def test_stations_within_radius(): # Test for Task 1C
    y = (51.0 , 0.0)
    radius_list = floodsystem.geo.stations_within_radius(station_list,y,20)
    assert type(radius_list) is list
    assert all(radius_list[i] <= radius_list[i+1] for i in range(len(radius_list) - 1)) == True # Checking that the list is sorted properly

def test_rivers_with_station(): # Test for Task 1D, part 1

    output  = floodsystem.geo.rivers_with_station(station_list)

    # check the case when input is not a list:
    with pytest.raises(AttributeError):
        floodsystem.geo.rivers_with_station("This is not a right input")
    with pytest.raises(AttributeError):
        floodsystem.geo.rivers_with_station(["This", "is", "also", "not", "correct", "input"])

    # check the output type:
    assert type(output) is list
    # check if there is repeated river in the output:
    assert len(output) == len(set(output))

    return

def test_stations_by_river(): # Test for task 1D, part 2

    the_map = floodsystem.geo.stations_by_river(station_list)

    # Check when the river name does not exist
    with pytest.raises(KeyError):
        the_map["A not-existed River"]
    # Check no repotition in the stations on River Aire
    assert len(the_map["River Aire"]) == len(set(the_map["River Aire"]))
    return


def test_river_by_station_number(): # Test for Task 1E

    # check the case when N is not in range
    with pytest.raises(ValueError):
        floodsystem.geo.rivers_by_station_number(station_list,-1)
    with pytest.raises(ValueError):
        floodsystem.geo.rivers_by_station_number(station_list,1000)
    return