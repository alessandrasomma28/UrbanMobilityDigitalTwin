# A guide for creating and running a urban mobility simulator through EclipseSUMO
This guide describe how to create and run a urban mobility simulator, leveraing the EclipseSUMO simulator. 

## Creating the simulator

### Prerequisites
Ensure you have SUMO installed. You can download it from [SUMO Download Page](https://sumo.dlr.de/docs/Downloads.php).

### Input 
In order to run the simulator, the following inputs must be provided:
- **Urban Network** describes the network of the investigated urban scenario. It can be easily downloaded from [OpenStreetMap](https://www.openstreetmap.org).
- **Zoning files** describe the zoning of the investigated city, as commonly used in mobility studies or surveys.
- **GTFS file** describes the organization and the scheduling of publica transport services.
- **Origin-Destination (OD) Matrix** contains information on journeys made by pedestrians, private vehicles, and public transport vehicles between different zones.

### Importing the urban network ###
SUMO expects the network as a *.net.xml*. To this purpose, the **OSMWebWizard** tool can be employed, taking as input the network donwload from OpenStreetMap

### Zoning ###
Zoning information is typically provided as a shapefile in the ESRI format. Importing a shapefile is a two-step process. First, the file is converted into a simulator-compatible format (*.polygons.xml*), and then grid elements are assigned to their respective traffic assignment zones (*.taz.xml*). The conversion to polygons is accomplished with the **polyconvert** tool, which requires the *.net.xml* map file. The resulting *polygons.xml* file includes region identifiers and the positions of the connecting segments.
Subsequently, the **edgesInDistricts.py** script is used to process the map and polygons, generating a *.taz.xml* file that identifies network elements and their associated zone characteristics.

### Modeling Public Transport Services ###
The **gtfs2pt.py** is used to import public transport in the simulation. As input, it taks the urban network and the gtfs files. The outputs are:
- *pt_vtypes.xml* defines the types of transport vehicles imported into the simulation
- *gtfs_publictransport.rou.xml* assigns an ID to each vehicle, specifying its departure time and the route it follows.
- *gtfs_publictransport.add.xml* contains details about the stops, including their positions, names, and IDs, as well as information about the roads traversed by the vehicles on each line.

### Transport Demand Generation ###
The transport demand described in the OD matrix must be converted in specific single trips. To this purpose, the **OD2Trips** is employed, leveraging the previously created *.taz.xml* file and the OD matrix in O-format. The output is a *.xml* file describing the list of trips.

### Routing ###
Once the trips are generated, the **duarouter** tool can be employed to generate the route of each trip. It takes as input the network file, the list of trips, and the gfts files, and generates the *trips.xml*: for each user (id) it containes the specific route, as a sequence of edges, stops or lines. 


## Running the simulation ##
In order to run the simulation, a *.sumocfg* file must be realized, specififying the path of the previously generated files, needed by the simulation. Hence, it is possible to run the simulation from command line, as follows:

```
$ sumo.exe -c conf.sumocfg
```
In this way, the simulation is executed in background, and its behavior is described in the output files (that can be configured in the *.sumocfg* (see https://sumo.dlr.de/docs/sumo.html)

Alternatively, it is possible to run the simulation with the GUI, allowing the real-time interaction with the simulator environment (it is worth noting that in this case the simulation will take longer). To this purpose, the following command can be used:
```
$ sumo-gui.exe -c conf.sumocfg
```

