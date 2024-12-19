import pandas as pd

# Load the CSV file
input_csv = "NEXGO SERIALS - 10pcs N5.csv"  # Input CSV file path
output_excel = "Book4.xlsx"  # Output Excel file path

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv)

# Specify the columns you want to extract (by column names)
columns_to_extract = [
    "KRA SERIAL",
    "COMPANY",
    "PHONE",
    "CONTACT NAME",
]  # Replace with actual column names

# Extract the desired columns
df_extracted = df[columns_to_extract]

# Save the extracted columns to a new Excel file
df_extracted.to_excel(output_excel, index=False)

print(f"Columns extracted and saved to {output_excel}")
