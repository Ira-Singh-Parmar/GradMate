import pandas as pd
import sqlite3

# Load the cleaned CSV
df = pd.read_csv("all_colleges_india.csv")

# Connect to SQLite DB
conn = sqlite3.connect("colleges.db")

# Insert DataFrame into SQL table
df.to_sql("colleges", conn, if_exists="replace", index=False)

print("✅ Data inserted into SQLite successfully!")
conn.close()
