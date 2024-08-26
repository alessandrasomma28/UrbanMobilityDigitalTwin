import pandas as pd
from ngsildclient import Entity, Rel
from constants import *


# function for reading dataset with real occupancy and gps data of bus systems
def importDataset(filepath: str) -> pd.DataFrame:
    try:
        realData = pd.read_csv(filepath)
        names = ['Trip', 'Route', 'Stop', 'Time stamp', 'Scheduled arrival time', 'Actual arrival time', 'Occupancy']
        if len(realData.columns) == len(names):
            realData.columns = names
        else:
            print(
                "Warning: The number of columns in the dataset does not match the expected names. Using default column names.")
        return realData
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {filepath} is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# function for importing stop data of GTFS of Italian city
def importStopData(filepath: str, savepath: str) -> tuple:
    try:
        stopsData = pd.read_csv(filepath)
        stopsData.to_csv(savepath, index=False)
        lat = stopsData['stop_lat'].to_numpy()
        lon = stopsData['stop_lon'].to_numpy()
        return lat, lon, stopsData

    except FileNotFoundError:
        print(f"Error: '{filepath}' file not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: '{filepath}' file is empty.")
    except KeyError as e:
        print(f"Error: Missing expected column {e}.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def busEntityCreation(busNaturalNumber:int) -> Entity:
    busProgressiveID = 'B{}'.format(busNaturalNumber)
    bus = Entity("Vehicle", busProgressiveID, ctx=TransportationCTX)
    bus.prop("category", "public").prop("vehicleType", "bus").prop("currentTripCount", 0)
    bus.pprint() # print the entity in a JSON-LD nicely format
    return bus

def tripEntityCreation(tripNaturalNumber:int, ctx : str) -> Entity:
    tripProgressiveID = 'T{}'.format(tripNaturalNumber)
    trip = Entity("TransitManagement", tripProgressiveID, ctx=UrbanMobilityCTX)
    trip.prop("trip_id", "0")
    trip.pprint()
    return trip

def busRouteEntityCreation(busRouteNumber: int, ctx: str) -> Entity:
    busRouteProgressiveID= 'BR{}'.format(busRouteNumber)
    busRoute = Entity("PublicTransportRoute", busRouteProgressiveID, ctx=UrbanMobilityCTX)
    busRoute.prop("transportationType", 3).prop("routeCode", "0")  # GTFS type = 3 (bus)
    return busRoute

def updateBusRoute(busRoute: Entity, bus:Entity, trip: Entity) -> tuple:
    busRoute.rel("isPerformedby", bus.id)
    bus.rel("performs", busRoute.id)
    # associazione tra bus route e trip
    busRoute.rel("follows", trip.id)  # lato bus route
    trip.rel(Rel.IS_CONTAINED_IN, busRoute.id)  # lato trip
    return bus, busRoute, trip

def busStopEntityCreation(busstopnumber: int) -> Entity :
    busStopProgressiveID = 'BS{}'.format(busstopnumber)
    busStop = Entity("PublicTransportStop", busStopProgressiveID, ctx=UrbanMobilityCTX)
    busStop.prop("transportationType", 3)  # GTFS type = 3 (bus)
    return busStop

def updateBusStop(busStop:Entity, trip: Entity) -> tuple:
    busStop.rel(Rel.IS_CONTAINED_IN, trip.id).anchor()
    busStop.prop("name", "0").prop("stop_id", 0).prop("stop_sequence", 0)
    #busStop.tprop("arrival_time", arrivaltime)
    #busStop.tprop("scheduled_arrival_time", scheduledtime).unanchor()
    trip.rel("hasStoppedAt", busStop.id)
    return busStop, trip

def apcDeviceEntityCreation(apcnumber: int) -> Entity :
    apcDeviceProgressiveID = 'APC{}'.format(apcnumber)
    apcDevice = Entity("Device", apcDeviceProgressiveID, ctx=DeviceCTX)
    apcDevice.prop("controlledProperty", "occupancy").prop("occup", 0)
    apcDevice.prop("deviceCategory", "sensor")
    return apcDevice

def gpsDeviceEntityCreation(gpsnumber: int) -> Entity:
    gpsDeviceProgressiveID = 'GPS{}'.format(gpsnumber)
    gpsDevice = Entity("Device", gpsDeviceProgressiveID, ctx=DeviceCTX)
    gpsDevice.prop("controlledProperty", "location").gprop("loc", coord)
    gpsDevice.prop("deviceCategory", "sensor")
    return gpsDevice

def updateGPS(gpsDevice: Entity, bus: Entity) -> tuple:
    gpsDevice.rel(Rel.IS_CONTAINED_IN, bus.id)
    bus.gprop("location", coord).rel(Rel.OBSERVED_BY,gpsDevice.id, nested=True)
    return gpsDevice, bus

def updateAPC(apcDevice: Entity, bus: Entity) -> tuple:
    apcDevice.rel(Rel.IS_CONTAINED_IN, bus.id)
    bus.prop("occupancy", 0).rel(Rel.OBSERVED_BY, apcDevice.id, nested=True)
    return apcDevice, bus





