# NYC-Urban-Yield-Mobility-Intelligence
a full-stack data engineering and analytics ecosystem designed to audit and optimize NYC transit operations. By synchronizing a local SQL database with Python automation, Excel/VBA operational tools, and Power BI strategic visuals, this project transforms 100,000+ raw trip records into actionable executive intelligence.

🛠️ The Technical Stack
Database (SQL): Metropolis_Mobility.db – A relational SQLite database for high-speed transactional storage.

Automation (Python): Step1_Data_Ingestion_Engine.py – Handles ETL (Extract, Transform, Load) processes, cleaning raw data for database insertion.

Operational UI (Excel/VBA): Metropolis_Command_Center.xlsm – A "no-code" audit interface using VBA to query the SQL database directly via a button-click.

Strategic Vision (Power BI): NYC Urban Yield & Mobility Intelligence.pbix – An interactive dashboard utilizing AI-driven Decomposition Trees for root-cause revenue analysis.

📈 Key Business Insights
Peak Liquidity: Identified 12:00 PM (Noon) as the primary revenue driver, generating over $216,000 in a single hour.

The Midnight Economy: Discovered that Hour 0 (Midnight) represents a top-3 profit tier ($183k+), significantly outperforming the morning commute.

Yield Efficiency: While Noon has the highest volume, the 4:00 PM shift shows a higher tip-to-fare ratio, suggesting a shift toward high-margin passengers.

🚀 How to Run the Machine
Run Step1_Data_Ingestion_Engine.py to initialize the database.

Open Metropolis_Command_Center.xlsm, enter an hour (0-23), and click the "Update Dashboard" button to audit specific windows.

Open the Power BI file to explore the interactive "Magic Tree" and spatial heatmaps.
