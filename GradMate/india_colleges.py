import pandas as pd

# Loading the excel file -------------------------
df = pd.read_excel("affiliated_colleges_india.xlsx", skiprows=2)

# Rename columns explicitly to clean up any residual header issues (optional but recommended)
df.columns = [
    "Aishe Code", "Name", "State", "District", "Website",
    "Year Of Establishment", "Location", "College Type",
    "Management", "University Name", "University Type"
]

df.to_csv("all_colleges_india.csv", index = False)

print("CSV file created successfully!")