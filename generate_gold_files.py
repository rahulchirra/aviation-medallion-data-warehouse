import pandas as pd
from extract import extract_flights_data
from transform import clean_flight_data

# 1. Live Flights API  data and  clean
raw_data = extract_flights_data()
df = clean_flight_data(raw_data)

# 2. Duplicate flights removing (Snowflake ROW_NUMBER)
df = df.drop_duplicates(subset=['icao24'], keep='last')

# 3. Speed Category column add 
def get_speed_category(v):
    if v == 0:
        return 'Stopped'
    elif v < 150:
        return 'Slow'
    else:
        return 'Fast'

df['speed_category'] = df['velocity'].apply(get_speed_category)

# 4. GOLD TABLE 1: dim_aircraft create and  save 
dim_aircraft = df[['icao24', 'callsign', 'origin_country']]
dim_aircraft.to_csv('dim_aircraft.csv', index=False)

# 5. GOLD TABLE 2: fact_flight_telemetry create  and save 
fact_telemetry = df[['icao24', 'last_contact', 'longitude', 'latitude', 'baro_altitude', 'velocity', 'speed_category', 'on_ground']]
fact_telemetry.to_csv('fact_flight_telemetry.csv', index=False)

print("Success: dim_aircraft.csv and fact_flight_telemetry.csv created for PowerBI!")