import sqlite3
import pandas as pd
import os

# WHAT: Automatically finding the folder where this script is saved.
# WHY: This makes your project "Plug and Play" for GitHub users.
current_folder = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_folder, "Metropolis_Mobility.db")
output_path = os.path.join(current_folder, "Hourly_Summary.csv")

def export_to_excel_bridge():
    try:
        # Connecting to the Vault
        conn = sqlite3.connect(db_path)

        # WHAT: Creating a small, readable "Snapshot" of the 100,000+ rides.
        query = """
        SELECT 
            strftime('%H', tpep_pickup_datetime) as Hour, 
            COUNT(*) as Rides, 
            ROUND(SUM(total_amount), 2) as Revenue, 
            ROUND(AVG(tip_amount), 2) as Tip 
        FROM Fact_Trips 
        GROUP BY Hour
        """
        
        df = pd.read_sql_query(query, conn)

        # WHAT: Saving as a CSV so Excel and Power BI can see the data.
        df.to_csv(output_path, index=False)
        
        conn.close()
        print(f"--- [SUCCESS] ---")
        print(f"Export Complete! {output_path} is ready for Excel.")
        
    except Exception as e:
        print(f"--- [ERROR] ---")
        print(f"Could not complete the bridge. Error: {e}")

if __name__ == "__main__":
    export_to_excel_bridge()

