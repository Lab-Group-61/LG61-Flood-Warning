from . import utils

from .station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    # This function returns a list of tuples, where each tuple holds a station at which the latest relative water level is over tol and the relative water level at the station
    # (Task 2B)
    output = []
    for station in stations:
        st_id = (station,station.relative_water_level())
        if station.relative_water_level() != None:
            if station.relative_water_level() > tol:
                output.append(st_id)
    sorted_output = utils.sorted_by_key(output,1,reverse=True) 
    return sorted_output