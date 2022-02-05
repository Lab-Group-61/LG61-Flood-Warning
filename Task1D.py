import floodsystem.geo
import floodsystem.stationdata

def run():
    # part 1: 
    station_list = floodsystem.stationdata.build_station_list()
    river_list = floodsystem.geo.rivers_with_station(station_list)
    print("{} stations".format(len(river_list)))
    print("First 10 - {}".format(river_list[0:10]))

    # part 2:
    the_mapping = floodsystem.geo.stations_by_river(station_list)
    print("Stations on River Cam are {}".format(sorted(the_mapping["River Cam"])))
    print("Stations on River Aire are {}".format(sorted(the_mapping["River Aire"])))
    print("Stations on River Thames are {}".format(sorted(the_mapping["River Thames"])))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()