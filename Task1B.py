from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_by_distance

def run():
    station_list = build_station_list() # Build a list of stations

    Cambridge_CC = (52.2053, 0.1218)

    sorted_station_list = stations_by_distance(station_list,Cambridge_CC)

    print("The closest 10 stations from Cambridge City Centre (in km) are:")
    print(sorted_station_list[:10])

    print( "\n The furthest 10 stations from Cambridge City Centre (in km) are:")
    print(sorted_station_list[-10:])

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()