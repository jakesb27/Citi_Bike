import requests
import pandas as pd
from config import geoapify_key


params = {
    "type": "postcode",
    "apiKey": geoapify_key
}

base_url = f"https://api.geoapify.com/v1/geocode/reverse?"

citi_bike_data = pd.read_csv('resources/202303-citibike-tripdata.csv',
                             dtype={'start_station_id': 'str', 'end_station_id': 'str'})

station_id_group = citi_bike_data.groupby('start_station_id')[['start_lat', 'start_lng']].mean()

station_id_group = station_id_group.reset_index()

for index, row in station_id_group.iterrows():
    start_lat = citi_bike_data.loc[index, "start_lat"]
    start_lng = citi_bike_data.loc[index, "start_lng"]
    params["lat"] = start_lat
    params["lon"] = start_lng

    results = requests.get(base_url, params=params)
    results = results.json()

    station_id_group.loc[index, "city"] = results["features"][0]["properties"]["city"]
    station_id_group.loc[index, "state"] = results["features"][0]["properties"]["state"]
    station_id_group.loc[index, "postcode"] = results["features"][0]["properties"]["postcode"]

station_id_group.to_csv("resources/station_details.csv", index=False)
