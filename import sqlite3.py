import sqlite3
import pandas as pd
import os

"""
Hourly Trip Analysis

This script reads trip data from the SQLite database and creates
an hourly summary showing ride volume, revenue, and average tip.
The results are printed and saved as a CSV file for tools like
Excel or Power BI.
"""

# Locate database relative to this script
db_name = "Metropolis_Mobility.db"
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, db_name)


def run_analysis():
    try:
        print("Connecting to database...")

        conn = sqlite3.connect(db_path)

        # Aggregate trip data by hour
        query = """
        SELECT 
            strftime('%H', tpep_pickup_datetime) AS Hour_of_Day,
            COUNT(*) AS Number_of_Rides,
            ROUND(SUM(total_amount), 2) AS Total_Revenue,
            ROUND(AVG(tip_amount), 2) AS Average_Tip
        FROM Fact_Trips
        GROUP BY Hour_of_Day
        ORDER BY Total_Revenue DESC
        """

        df_results = pd.read_sql_query(query, conn)

        print("\nTop hourly revenue periods:")
        print(df_results.head(10))

        # Save results so BI tools can load them quickly
        output_file = os.path.join(script_dir, "Hourly_Summary.csv")
        df_results.to_csv(output_file, index=False)

        print(f"\nCSV export complete: {output_file}")

        conn.close()

    except sqlite3.OperationalError:
        print(f"Error: {db_name} was not found in this folder.")
        print("Make sure the database file exists before running the analysis.")


if __name__ == "__main__":
    run_analysis()
