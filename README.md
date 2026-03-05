# NYC-Urban-Yield-Mobility-Intelligence
a sophisticated data lifecycle project designed for Koogle's urban mobility division. It synchronizes four distinct technologies—SQL, Python, Excel/VBA, and Power BI—to transform 100,000+ raw NYC taxi transactions into a high-octane decision-support system.

⚠️ Critical Security Setup (For Reviewers)
Because this project utilizes VBA Macros to bridge Excel and SQL, Windows will "Lock" the file by default for your safety. To enable the interactive features:

Unblock the File: Right-click Metropolis_Command_Center.xlsm > Properties > Check the Unblock box at the bottom > OK.

Enable Content: Upon opening the Excel file, click 'Enable Content' on the yellow security bar at the top.

Keep Together: Ensure all files remain in the same folder to maintain the "Relative Path" connections.

⚙️ Operating Instructions (The Flight Manual)
To operate the "Metropolis Mobility" machine, follow these steps in order:

Step 1: The Ingestion Engine (Python)
Run Step1_Data_Ingestion.py.

Technical Note: Performs ETL (Extract, Transform, Load) on 100,000 records using the Parquet format for maximum efficiency.

Step 2: The Data Bridge (Python)
Run Step2_Data_Bridge.py.

Step 3: The Operational Audit (Excel/VBA)
Open Metropolis_Command_Center.xlsm.

Technical Note: Uses VBA to perform an automated "Pull" from the SQL database, updating live revenue and tip metrics instantly.

Step 4: Strategic Intelligence (Power BI)
Open the Power BI file.

📈 Final Business Insights
Peak Revenue: Identified Hour 12 (Noon) as the primary revenue peak ($216k+).

The Midnight Economy: Discovered that Hour 0 (Midnight) ranks as a top-3 profit window, outperforming the morning rush.

Yield Efficiency: Leveraged dual-axis modeling to show that while volume is highest at noon, tip-to-fare ratios peak during late-evening transitions.

🛠️ The Architect's Tech Stack
SQL (SQLite): For relational storage and high-speed querying.

Python (Pandas/OS): For automated data cleaning and portable path management.

VBA: For bridging the gap between "Raw Data" and "User Experience."

Power BI: For advanced spatial intelligence and root-cause analysis.
