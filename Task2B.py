from floodsystem.stationdata import build_station_list, update_water_levels

from floodsystem.flood import stations_level_over_threshold

def run():
    # Build list of stations
    station_list = build_station_list()

    # Update latest level data for all stations
    update_water_levels(station_list)

    output_list = stations_level_over_threshold(station_list,0.8)

    for element in output_list:
        print(element[0].name, element[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
