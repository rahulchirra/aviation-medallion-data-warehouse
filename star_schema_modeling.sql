USE DATABASE cdc_db;
USE SCHEMA users_schema;

-- 1. SILVER TABLE: Removing duplicates & adding speed_category
CREATE OR REPLACE TABLE silver_flights_cleaned AS
WITH deduplicated_flights AS (
    SELECT 
        *,
        CASE 
            WHEN velocity = 0 THEN 'Stopped'
            WHEN velocity < 150 THEN 'Slow'
            ELSE 'Fast'
        END AS speed_category,
        ROW_NUMBER() OVER (PARTITION BY icao24 ORDER BY last_contact DESC) AS row_num
    FROM bronze_flight_raw
)
SELECT * EXCLUDE (row_num)
FROM deduplicated_flights
WHERE row_num = 1;

-- 2. GOLD DIMENSION TABLE: Flight Identity
CREATE OR REPLACE TABLE dim_aircraft AS
SELECT 
    icao24,
    callsign,
    origin_country
FROM silver_flights_cleaned;

-- 3. GOLD FACT TABLE: Flight Telemetry Metrics
CREATE OR REPLACE TABLE fact_flight_telemetry AS
SELECT 
    icao24,
    last_contact,
    longitude,
    latitude,
    baro_altitude,
    velocity,
    speed_category,
    on_ground
FROM silver_flights_cleaned;