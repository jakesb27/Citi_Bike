import pandas as pd


citi_bike_data = pd.read_csv('resources/2023-Q1_CitiBike.csv',
                             dtype={'start_station_id': 'str', 'end_station_id': 'str'})

station_id_details = pd.read_csv('resources/station_details.csv', dtype={'start_station_id': 'str'})
station_id_details.head()

new_df = citi_bike_data.merge(station_id_details, how='left', on='start_station_id')

new_df.to_csv('resources/2023-Q1_CitiBike_Final.csv', index=False)
