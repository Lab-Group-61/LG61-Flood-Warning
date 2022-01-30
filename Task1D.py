import floodsystem.geo
import floodsystem.stationdata


station_list = floodsystem.stationdata.build_station_list()

# part 1: 
river_list = floodsystem.geo.rivers_with_station(station_list)

print("{} stations".format(len(river_list)))

print("First 10 - {}".format(river_list[0:10]))

# part 2:
the_mapping = floodsystem.geo.stations_by_river(station_list)
print(sorted(the_mapping["River Cam"]))
print(sorted(the_mapping["River Aire"]))
print(sorted(the_mapping["River Thames"]))