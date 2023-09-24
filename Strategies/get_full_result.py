import csv
import os
import pandas as pd

# Define the input and output file paths
input_file1 = os.path.join('..','stock_data.csv')
input_file2 = os.path.join('result.csv')
output_file = os.path.join('full_result.csv')

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv(input_file1)
df2 = pd.read_csv(input_file2)

# Merge the DataFrames based on the "SYMBOL" column
merged_df = pd.merge(df1, df2, on='SYMBOL', how='inner')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv(output_file, index=False)

print(f"Merged data saved to {output_file}")
