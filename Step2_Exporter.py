import sqlite3
import pandas as pd
import os

"""
PROJECT: NYC Taxi Hourly Summary Export
PURPOSE: Read trip data from the local SQLite database and generate
         a simple hourly summary for Excel or Power BI.
AUTHOR: Mansur Mohammed
"""

# -------------------------------
# Setup Paths
# -------------------------------
# Locate the folder where this script is running
current_folder = os.path.dirname(os.path.abspath(__file__))

# Path to the local SQLite database
db_path = os.path.join(current_folder, "Metropolis_Mobility.db")

# Path for the exported CSV file
output_path = os.path.join(current_folder, "Hourly_Summary.csv")


def export_hourly_summary():
    """Connect to the database and export a summary of trips by hour."""
    try:
        print("🗄️ Connecting to SQLite database...")

        conn = sqlite3.connect(db_path)

        # SQL query: summarize trips by hour
        query = """
        SELECT 
            strftime('%H', tpep_pickup_datetime) AS Hour,
            COUNT(*) AS Rides,
            ROUND(SUM(total_amount), 2) AS Revenue,
            ROUND(AVG(tip_amount), 2) AS Avg_Tip
        FROM Fact_Trips
        GROUP BY Hour
        ORDER BY Hour
        """

        # Execute query and load results into a DataFrame
        df = pd.read_sql_query(query, conn)

        # Save the summary to CSV for Excel / Power BI
        df.to_csv(output_path, index=False)

        conn.close()

        print("✅ Export completed successfully!")
        print(f"📂 File saved at: {output_path}")

    except Exception as e:
        print("❌ An error occurred while exporting the data.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    export_hourly_summary()
