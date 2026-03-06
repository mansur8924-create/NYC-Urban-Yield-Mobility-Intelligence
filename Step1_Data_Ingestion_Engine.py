import pandas as pd
import sqlite3
import os

"""
NYC Taxi Data Loader

This script downloads NYC yellow taxi trip data (Parquet format),
stores a subset of the data in a local SQLite database, and prepares
it for analysis.
"""

# Find the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Database will be created in the same folder as the script
db_path = os.path.join(current_dir, "Metropolis_Mobility.db")

# Source dataset (NYC Taxi & Limousine Commission)
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"


def initialize_database():
    print("Loading NYC taxi dataset...")

    try:
        # Read the parquet file directly from the URL
        data = pd.read_parquet(url)

        print("Dataset loaded successfully.")
        print("Creating SQLite database...")

        # Connect to SQLite
        conn = sqlite3.connect(db_path)

        # Use only the first 100k rows so the database stays lightweight
        subset = data.head(100000)

        # Store the data in a table called Fact_Trips
        subset.to_sql("Fact_Trips", conn, if_exists="replace", index=False)

        conn.close()

        print("Database created successfully.")
        print(f"Database location: {db_path}")

    except Exception as e:
        print("An error occurred while loading the dataset.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    initialize_database()
