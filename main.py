import warnings
warnings.filterwarnings("ignore")

from extract import extract_flights_data
from transform import clean_flight_data
from load_aws import load_data_s3
from load_snowflake import load_to_bronze

def run_pipeline():
    print("--- STARTING LIVE AVIATION DATA PIPELINE ---")
    
    # Step 1: Extract
    raw_data = extract_flights_data()
    print(f"Step 1 Done: Extracted {len(raw_data)} live flights from API.")
    
    # Step 2: Transform
    clean_df = clean_flight_data(raw_data)
    print(f"Step 2 Done: Cleaned data in Pandas ({len(clean_df)} valid rows).")
    
    # Step 3: Load to AWS S3
    load_data_s3(clean_df)
    print("Step 3 Done: Uploaded Parquet file to AWS S3.")
    
    # Step 4: Load to Snowflake Bronze Table
    load_to_bronze()
    print("Step 4 Done: Appended batch into Snowflake Bronze layer!")
    
    print("--- PIPELINE COMPLETED SUCCESSFULLY ---")

run_pipeline()