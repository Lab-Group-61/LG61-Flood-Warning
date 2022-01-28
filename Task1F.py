from floodsystem.stationdata import build_station_list

from floodsystem.station import inconsistent_typical_range_stations

station_list = build_station_list() # Build a list of stations

print(inconsistent_typical_range_stations(station_list))

print(station_list[0].typical_range_consistent)