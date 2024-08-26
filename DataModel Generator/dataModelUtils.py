import pandas as pd





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

