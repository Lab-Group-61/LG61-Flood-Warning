from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance

stations = build_station_list()

Cambridge_CC = (52.2053, 0.1218)

station_lists = stations_by_distance(stations,Cambridge_CC)

print("The closest 10 stations from Cambridge City Centre are:")
print(station_lists[:10])

print("The furthest 10 stations from Cambridge City Centre are:")
print(station_lists[-10:])