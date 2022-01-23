from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance

station_list = build_station_list() # Build a list of stations

Cambridge_CC = (52.2053, 0.1218)

sorted_station_list = stations_by_distance(station_list,Cambridge_CC)

print("The closest 10 stations from Cambridge City Centre are:")
print(sorted_station_list[:10])

print("The furthest 10 stations from Cambridge City Centre are:")
print(sorted_station_list[-10:])