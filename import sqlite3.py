import sqlite3
import pandas as pd
import os

"""
PROJECT: NYC Taxi Hourly Revenue Analysis
PURPOSE: Read trip data from the SQLite database, summarize rides by hour,
         and export results for Excel or Power BI.
AUTHOR: Mansur Mohammed
"""

# -------------------------------
# Setup: Locate the database
# -------------------------------
db_name = "Metropolis_Mobility.db"
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, db_name)


def run_hourly_analysis():
    """
    Connects to the database, aggregates trip data by hour,
    and saves a CSV for quick visualization.
    """
    try:
        print("🗄️ Connecting to SQLite database...")

        conn = sqlite3.connect(db_path)

        # SQL query: aggregate trips by hour, calculate total rides, revenue, and average tip
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

        # Execute the query and load results into a DataFrame
        df_results = pd.read_sql_query(query, conn)

        print("\n🚦 Top hourly revenue periods:")
        print(df_results.head(10))

        # Save the summary to a CSV file for BI tools
        output_file = os.path.join(script_dir, "Hourly_Summary.csv")
        df_results.to_csv(output_file, index=False)

        print(f"\n✅ CSV export complete! File ready at: {output_file}")

        conn.close()

    except sqlite3.OperationalError:
        print(f"❌ Error: {db_name} was not found in this folder.")
        print("Please make sure the database exists before running the analysis.")


if __name__ == "__main__":
    run_hourly_analysis()
