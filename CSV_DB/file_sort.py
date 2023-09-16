import pandas as pd

# Load the merged CSV file
df = pd.read_csv('merged_output.csv')

# Sort the columns (dates) in ascending order
date_columns = sorted(df.columns[1:], key=lambda x: pd.to_datetime(x))
sorted_columns = ['SYMBOL'] + date_columns
df = df[sorted_columns]

# Save the sorted DataFrame to a new CSV file
df.to_csv('sorted_merged_output.csv', index=False)
