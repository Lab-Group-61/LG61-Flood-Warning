"""Unit test for the geo module"""
import pytest
import floodsystem.geo
import floodsystem.station
import floodsystem.stationdata

# The station list is here:
station_list = floodsystem.stationdata.build_station_list()


def test_rivers_with_station():

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

    # check the first 10 stations:
    #My result from the different from the representative output tho
    assert output[0:10] == ['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 
    'Aldingbourne Rife', 'Aller Brook', 'Allison Dyke', 'Alverthorpe Beck', 'Ampney Brook', 
    'Amwell Loop', 'Arkle Beck']

    return

    

test_rivers_with_station()




