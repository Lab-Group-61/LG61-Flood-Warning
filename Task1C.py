from floodsystem.stationdata import build_station_list

from floodsystem.geo import stations_within_radius

def run():
    station_list = build_station_list() # Build a list of stations

    Cambridge_CC = (52.2053, 0.1218)

    radius = 10 # Define radius in km

    output_list = stations_within_radius(station_list,Cambridge_CC,radius)

    print("The stations within {}km of Cambridge City Centre are:".format(radius))
    print(output_list)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()