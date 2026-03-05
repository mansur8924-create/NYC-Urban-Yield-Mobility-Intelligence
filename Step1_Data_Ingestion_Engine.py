import pandas as pd
import sqlite3
import requests
import os

# --- ARCHITECT'S NOTE: PATH MANAGEMENT ---
# WHAT: Defining a raw string (r"") for your specific Windows directory.
# WHY: Windows uses backslashes which Python can mistake for "escape characters." 
# Using a raw string ensures the code finds your "Data Analyst Projects" folder perfectly.
base_path = r"C:\Users\mansu\OneDrive\Desktop\Data Analyst Boot Camp\Data Analyst Projects\The_Metropolis_Mobility Ledger"
db_path = os.path.join(base_path, "Metropolis_Mobility.db")
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-01.parquet"

# --- ARCHITECT'S NOTE: DIRECTORY VALIDATION ---
# WHAT: Checking if the folder exists, and creating it if not.
# WHY: A robust script shouldn't crash just because a folder is missing; it should be "self-healing."
if not os.path.exists(base_path):
    os.makedirs(base_path)

print(f"--- Project: The Metropolis Mobility Ledger ---")
print("Status: Downloading Real-World NYC Data...")

# --- ARCHITECT'S NOTE: DATA ACQUISITION ---
# WHAT: Pulling the Parquet file from the NYC Government Cloud.
# WHY: Parquet is the industry standard for "Big Data." It is 10x smaller than a CSV, 
# making this download much faster for your machine.
data = pd.read_parquet(url)

print("Status: Initializing SQL 'Vault'...")

# --- ARCHITECT'S NOTE: RELATIONAL STORAGE ---
# WHAT: Connecting to SQLite and injecting the first 100,000 rows.
# WHY: We use a 'Subset' (head) to ensure your Excel and Power BI tools remain 
# lightning-fast while we build the logic. 100,000 rows is plenty for a high-level "Proof of Concept."
conn = sqlite3.connect(db_path)
data.head(100000).to_sql('Fact_Trips', conn, if_exists='replace', index=False)
conn.close()

print(f"\nSuccess! Database created at: {db_path}")


