from dataModelUtils import *
from constants import *
from ngsildclient import Client


if __name__ == "__main__":

    realData = importDataset(realDataPath)
    lat, lon, stopsData = importStopData(stopDataPath, stopsDataPath)

    cb = Client("localhost", port=1026, tenant="openiot", overwrite=True)
    print(cb.is_connected()) #check connection

    bus = busEntityCreation(1)
    trip = tripEntityCreation(1)
    busRoute = busRouteEntityCreation(1)
    busStop = busStopEntityCreation(1)
    gpsDevice = gpsDeviceEntityCreation(1)
    apcDevice = apcDeviceEntityCreation(1)

    busStop, trip = updateBusStop(busStop, trip)
    gpsDevice, bus = updateGPS(gpsDevice, bus)
    apcDevice, bus = updateAPC(apcDevice, bus)

    mobility_entities = [bus, trip, busRoute, busStop, gpsDevice, apcDevice]

    cb.create(mobility_entities)