import floodsystem.geo
import floodsystem.stationdata


station_list = floodsystem.stationdata.build_station_list()

the_result = floodsystem.geo.rivers_by_station_number(station_list,9)

print(the_result)
