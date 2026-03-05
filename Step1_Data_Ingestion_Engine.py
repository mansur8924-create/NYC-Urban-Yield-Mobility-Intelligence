import pandas as pd
import sqlite3
import os

# WHAT: Using a relative path strategy.
# WHY: On GitHub, we want this script to be "Plug and Play." 
# This command finds the folder where this specific script is saved on ANY computer.
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, "Metropolis_Mobility.db")
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

def initialize_database():
    print(f"--- Project Zenith: The Metropolis Mobility Ledger ---")
    print("Status: Downloading Real-World NYC Data (Parquet)...")

    try:
        # WHAT: Pulling the Parquet file from the NYC Government Cloud.
        # WHY: Parquet is the industry standard—it's small, fast, and professional.
        data = pd.read_parquet(url)

        print("Status: Initializing SQL 'Vault'...")

        # WHAT: Connecting to SQLite and injecting the first 100,000 rows.
        # WHY: We use a 'Subset' to keep the "Command Center" lightning-fast.
        conn = sqlite3.connect(db_path)
        data.head(100000).to_sql('Fact_Trips', conn, if_exists='replace', index=False)
        conn.close()

        print(f"\n[SUCCESS] Database created at: {db_path}")
        
    except Exception as e:
        print(f"\n[ERROR] An issue occurred during ingestion: {e}")

if __name__ == "__main__":
    initialize_database()

