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
print((sorted(the_mapping["River Aire"])))
print(sorted(the_mapping["River Thames"]))

"""
I found a problem here, the number of stations with River Aire
is different from the representative result
I guess the data is prob different now

e.g. there are 21 stations in the answer
but 24 in my codes

From answer:
['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Saltaire', 'Snaygill', 'Stockbridge']

From new calculation:
['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Leeds Crown Point Flood Alleviation Scheme', 'Leeds Knostrop Weir Flood Alleviation Scheme', 'Oulton Lemonroyd', 'Saltaire', 'Snaygill', 'Stockbridge']
"""