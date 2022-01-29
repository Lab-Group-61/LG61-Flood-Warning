from floodsystem.stationdata import build_station_list

from floodsystem.station import inconsistent_typical_range_stations

from floodsystem.station import MonitoringStation

station_list = build_station_list() # Build a list of stations

print("The stations with inconsitent range data:")
print(inconsistent_typical_range_stations(station_list))