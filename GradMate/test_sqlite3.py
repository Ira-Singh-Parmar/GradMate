import sqlite3

# Connect to your SQLite DB
con = sqlite3.connect("colleges.db")
cur = con.cursor()

# Run PRAGMA to get column info
cur.execute("PRAGMA table_info(colleges);")
columns = cur.fetchall()

# Print just the column names
print("🧾 Column Names in 'colleges' table:")
for col in columns:
    print(col[1])  # column name is the 2nd item in each tuple

con.close()