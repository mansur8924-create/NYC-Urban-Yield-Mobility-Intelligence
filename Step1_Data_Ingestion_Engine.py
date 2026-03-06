import pandas as pd
import sqlite3
import os

"""
PROJECT: NYC Taxi Data Loader
PURPOSE: Download NYC yellow taxi trip data (Parquet), store a subset in a local SQLite database,
         and prepare it for analysis.
AUTHOR: Mansur Mohammed
"""

# -------------------------------
# Setup Paths
# -------------------------------
# Locate the folder where this script is running
current_dir = os.path.dirname(os.path.abspath(__file__))

# SQLite database path (stored in the same folder)
db_path = os.path.join(current_dir, "Metropolis_Mobility.db")

# Source dataset from NYC Taxi & Limousine Commission (Parquet format)
dataset_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"


def initialize_database():
    """Load the NYC taxi dataset and create a local SQLite database."""
    print("🚖 Downloading NYC taxi dataset...")

    try:
        # Read the Parquet file directly from the URL
        data = pd.read_parquet(dataset_url)
        print("✅ Dataset loaded successfully.")

        # Connect to SQLite
        print("💾 Creating local SQLite database...")
        conn = sqlite3.connect(db_path)

        # Keep only the first 100,000 rows for faster queries
        subset = data.head(100_000)

        # Store the data in a table called 'Fact_Trips'
        subset.to_sql("Fact_Trips", conn, if_exists="replace", index=False)

        # Close the connection
        conn.close()

        print("✅ Database created successfully!")
        print(f"📂 Database location: {db_path}")

    except Exception as e:
        print("❌ An error occurred while processing the dataset.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    initialize_database()
