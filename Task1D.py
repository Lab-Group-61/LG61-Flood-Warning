import floodsystem.geo

# Generate a bunch of station and put them into the list "test_stations"
station_list = (floodsystem.geo.station_list)
testing_stations = []

for item in range(0,len(station_list),100):
    testing_stations.append(station_list[item])


#Call the function to print all the rivers in "test_stations"
print(floodsystem.geo.rivers_with_station(testing_stations))