import os
import snowflake.connector
from dotenv import load_dotenv

load_dotenv()

def load_to_bronze():
    # 1. Snowflake database login
    conn = snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        warehouse='COMPUTE_WH',
        database='CDC_DB',
        schema='USERS_SCHEMA'
    )
    cursor = conn.cursor()

    # 2. S3  flights.parquet to  Snowflake Bronze table  appending
    cursor.execute("""
        COPY INTO bronze_flight_raw
        FROM @cdc_s3_stage/aviation_data/flights.parquet
        FILE_FORMAT = (TYPE = PARQUET)
        MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
        FORCE = TRUE;
    """)

    print("Success: Live flight batch appended into Snowflake Bronze Table!")

    # 3. Save  connection close 
    conn.commit()
    cursor.close()
    conn.close()
    return True
