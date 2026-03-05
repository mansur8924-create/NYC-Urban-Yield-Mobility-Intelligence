import sqlite3
import pandas as pd
import os

base_path = r"C:\Users\mansu\OneDrive\Desktop\Data Analyst Boot Camp\Data Analyst Projects\The_Metropolis_Mobility Ledger"
db_path = os.path.join(base_path, "Metropolis_Mobility.db")

conn = sqlite3.connect(db_path)

# Extract the hourly summary we just saw
query = "SELECT strftime('%H', tpep_pickup_datetime) as Hour, COUNT(*) as Rides, SUM(total_amount) as Revenue, AVG(tip_amount) as Tip FROM Fact_Trips GROUP BY Hour"
df = pd.read_sql_query(query, conn)

# Save it as a small CSV for Excel to read
df.to_csv(os.path.join(base_path, "Hourly_Summary.csv"), index=False)
conn.close()
print("Export Complete! Excel can now read the data.")