# Urban Mobility Digital Twin

This repository contains a small-scale implementation of a Digital Twin (DT) architecture for urban mobility, using FIWARE GEs as core components. The system simulates a real-world bus transportation network in a major Italian city, leveraging Automatic Passenger Counting (APC) systems and GPS data to monitor and predict bus occupancy and movements.

## System Architecture 
![image](https://github.com/user-attachments/assets/a22195de-af41-45f3-8d13-1a9d15ee5e4d)

## Repository Structure
The repository is organized as follows:
- **FIWARE Components** contains the docker-compose.yml file to deploy these containers: 
  1) **Orion-LD** is FIWARE Context Broker. This will receive/send requests in NGSI-LD format.
  2) **IoT Agent** for JSON, the bridge that allows devices communication using a simple JSON protocol.  
  3) **MongoDB** is used by *i)* the Orion Context Broker to hold context data information, subscriptions and registrations; *ii)* the IoT Agent to hold device information (device URLs and API keys)
  4) **Timescale** timeseries database for persisting historic context. 
  5) **Mintaka** add-on which services the temporal interface and is responsible for persisting the context. 
  6) **Grafana** service used for display the persisted time-series data stored in Timescale.


