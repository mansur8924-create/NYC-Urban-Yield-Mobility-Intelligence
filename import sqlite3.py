import sqlite3
import pandas as pd

# --- ARCHITECT'S NOTE: THE CONNECTION ---
# WHAT: Pointing to the vault we built in Step 1.
db_path = r"C:\Users\mansu\OneDrive\Desktop\Data Analyst Boot Camp\Data Analyst Projects\The_Metropolis_Mobility Ledger\Metropolis_Mobility.db"
conn = sqlite3.connect(db_path)

# --- ARCHITECT'S NOTE: THE "MONEY" QUERY ---
# WHAT: Grouping 100,000 rides by 'Hour' to see when the city is most profitable.
# WHY: This is 'Time-Series' analysis. It proves you can find patterns in time.
query = """
SELECT 
    tpep_pickup_datetime AS Time_Stamp,
    strftime('%H', tpep_pickup_datetime) AS Hour_of_Day,
    COUNT(*) AS Number_of_Rides,
    ROUND(SUM(total_amount), 2) AS Total_Revenue,
    ROUND(AVG(tip_amount), 2) AS Average_Tip
FROM Fact_Trips
GROUP BY Hour_of_Day
ORDER BY Total_Revenue DESC;
"""

# Executing the search
df_results = pd.read_sql_query(query, conn)
print("--- THE HOURLY REVENUE REPORT ---")
print(df_results.head(10)) # Show the top 10 most profitable hours

conn.close()
