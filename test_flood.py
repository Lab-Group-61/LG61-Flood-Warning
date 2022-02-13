"""Unit test for the flood submodule"""
from turtle import distance
from numpy import sort
import pytest
import floodsystem.geo
import floodsystem.station
import floodsystem.stationdata
import floodsystem.flood

# The station list is here:
station_list = floodsystem.stationdata.build_station_list()

def test_stations_level_over_threshold(): # Test for Task 2B
    floodsystem.stationdata.update_water_levels(station_list)

    output = floodsystem.flood.stations_level_over_threshold(station_list,1)
    assert type(output) is list
    assert type(output[0]) is tuple 

    relative_water_levels = []
    for i in output:
        relative_water_levels.append(i[1])
    assert all(relative_water_levels[i] >= relative_water_levels[i+1] for i in range(len(relative_water_levels) - 1)) == True # Checking that the list is sorted properly