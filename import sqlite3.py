import sqlite3
import pandas as pd
import os

db_name = "Metropolis_Mobility.db"
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, db_name)

def run_analysis():
    try:
        conn = sqlite3.connect(db_path)
        
        # WHAT: Grouping 100,000+ rides by 'Hour' to find the "Gold Mines."
        query = """
        SELECT 
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
        print(df_results.head(10)) 

        # We save this to CSV so Power BI can read it instantly.
        df_results.to_csv("Hourly_Summary.csv", index=False)
        print("\n[SUCCESS] Hourly_Summary.csv has been updated for Power BI.")

        conn.close()
        
    except sqlite3.OperationalError:
        print(f"[ERROR] Could not find {db_name}. Ensure the database is in the same folder.")

if __name__ == "__main__":
    run_analysis()


