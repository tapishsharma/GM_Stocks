import pandas as pd
import os

# Directory containing the CSV files
directory = 'csv_files'

# Initialize a flag to check if we have processed any files
processed_first_file = False

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Filter rows where 'series' is 'EQ'
        df = df[df['SERIES'] == 'EQ']
        
        # Extract the 'SYMBOL' and 'CLOSE' columns and rename 'CLOSE' to the filename
        df = df[['SYMBOL', 'CLOSE']]
        df.rename(columns={'CLOSE': filename}, inplace=True)
        
        if not processed_first_file:
            merged_df = df
            processed_first_file = True
        else:
            # Merge the current DataFrame with the merged DataFrame on the 'SYMBOL' column
            merged_df = pd.merge(merged_df, df, on='SYMBOL', how='outer')

# Replace NaN values with an empty string
merged_df.fillna('', inplace=True)

# Save the merged DataFrame to a CSV file
merged_df.to_csv('merged_output.csv', index=False)
