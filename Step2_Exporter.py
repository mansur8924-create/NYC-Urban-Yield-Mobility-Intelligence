import sqlite3
import pandas as pd
import os

"""
Trip Data Export Script

Reads trip data from the local SQLite database and generates
a simple hourly summary that can be opened in Excel or used
in Power BI.
"""

# Locate the folder where this script is stored
current_folder = os.path.dirname(os.path.abspath(__file__))

# Paths for the database and exported CSV
db_path = os.path.join(current_folder, "Metropolis_Mobility.db")
output_path = os.path.join(current_folder, "Hourly_Summary.csv")


def export_hourly_summary():
    try:
        print("Connecting to database...")

        conn = sqlite3.connect(db_path)

        # SQL query to summarize rides by hour
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

        # Run query and load results into a dataframe
        df = pd.read_sql_query(query, conn)

        # Save results as a CSV file
        df.to_csv(output_path, index=False)

        conn.close()

        print("Export completed successfully.")
        print(f"File saved to: {output_path}")

    except Exception as e:
        print("An error occurred while exporting the data.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    export_hourly_summary()
