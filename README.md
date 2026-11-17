# Aviation Medallion Data Warehouse & Power BI Radar

An end-to-end Data Engineering & Business Intelligence project that extracts live global flight radar data, processes it through a Medallion Architecture (Bronze -> Silver -> Gold) in Snowflake, and visualizes live telemetry in Power BI.

### Architecture Flow
`OpenSky Live REST API` -> `Python (Pandas & Parquet)` -> `AWS S3` -> `Snowflake (Bronze, Silver, Gold Star Schema)` -> `Power BI Dashboard`

### Tech Stack
* **Language:** Python (`requests`, `pandas`, `boto3`, `snowflake-connector-python`)
* **Cloud Storage:** AWS S3
* **Data Warehouse:** Snowflake SQL (CTEs, `ROW_NUMBER`, `CASE WHEN`, Star Schema)
* **BI Tool:** Microsoft Power BI (Star Schema Modeling, DAX)

### Project Files
* `extract.py` - Pulls live flight telemetry (5,600+ flights) from OpenSky Network API.
* `transform.py` - Maps 2D JSON arrays into structured columns and cleans string whitespaces.
* `load_aws.py` - Converts DataFrame to in-memory Parquet (`BytesIO`) and uploads to AWS S3.
* `load_snowflake.py` - Appends S3 Parquet files into the Snowflake Bronze table (`bronze_flight_raw`).
* `star_schema_modeling.sql` - SQL scripts for Silver layer deduplication and Gold layer Star Schema (`dim_aircraft` & `fact_flight_telemetry`).
* `aviation_radar_dashboard.pbix` - Interactive Power BI dashboard with GPS Map, KPI Cards, and Slicers.
