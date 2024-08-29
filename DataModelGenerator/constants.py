from ngsildclient import CORE_CONTEXT

ORIONLD_PORT=1026
ORIONLD_PORT_TEMPORAL = 8086

# File datapath constants
realDataPath = "./dataset.csv"
stopDataPath = "./stops.txt"
stopsDataPath = "./stops.csv"

# Smart Data Models Context
UrbanMobilityCTX = ["https://raw.githubusercontent.com/smart-data-models/dataModel.UrbanMobility/5422d689ddca0fe995c7d46cc95d7e205c5cb30c/context.jsonld", CORE_CONTEXT]
TransportationCTX = ["https://raw.githubusercontent.com/smart-data-models/dataModel.Transportation/4df15072b13da6c7bd7e86915df91fb28921aa7f/context.jsonld", CORE_CONTEXT]
DeviceCTX = ["https://raw.githubusercontent.com/smart-data-models/dataModel.Device/master/context.jsonld", CORE_CONTEXT]
