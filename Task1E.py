import floodsystem.geo
import floodsystem.stationdata

def run():

    station_list = floodsystem.stationdata.build_station_list()

    the_result = floodsystem.geo.rivers_by_station_number(station_list,9)

    print("The first 9th stations are {}".format(the_result))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()