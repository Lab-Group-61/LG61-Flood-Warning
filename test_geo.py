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

def test_stations_by_river():

    the_map = floodsystem.geo.stations_by_river(station_list)

    # Check when the river name does not exist
    with pytest.raises(KeyError):
        the_map["A not-existed River"]
    # Check if the specific mapping for River Cam is correct
    assert the_map["River Cam"] == ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Great Chesterford', 'Weston Bampfylde']
    # Check ifthe total number of river in River Thames is correct
    assert len(the_map["River Thames"]) == 55
    # Check no repotition in the stations on River Aire
    assert len(the_map["River Aire"]) == len(set(the_map["River Aire"]))
    return


def test_river_by_station_number():

    # check the case when N is not in range
    with pytest.raises(ValueError):
        floodsystem.geo.rivers_by_station_number(station_list,-1)
    with pytest.raises(ValueError):
        floodsystem.geo.rivers_by_station_number(station_list,951)

    # check the specific output when N = 9
    assert floodsystem.geo.rivers_by_station_number(station_list,9) == [('River Thames', 55),
    ('River Avon', 31), ('River Great Ouse', 30), ('River Derwent', 25), ('River Aire', 24),
    ('River Calder', 23), ('River Severn', 21), ('River Stour', 21), ('River Colne', 18),
    ('River Ouse', 18)]
    return

test_stations_by_river()