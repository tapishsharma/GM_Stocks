import pandas as pd
import os

# Create an empty dictionary to store data frames
data_frames = {}

# Directory containing the CSV files
directory = 'csv_files'

# Iterate through files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        
        # Extract the 'SYMBOL' and 'CLOSE' columns and rename 'CLOSE' to the filename
        df = df[['SYMBOL', 'CLOSE']]
        df.rename(columns={'CLOSE': filename}, inplace=True)
        
        # Store the DataFrame in the dictionary with the filename as the key
        data_frames[filename] = df

# Merge all DataFrames on the 'SYMBOL' column
merged_df = None
for key, df in data_frames.items():
    if merged_df is None:
        merged_df = df
    else:
        merged_df = pd.merge(merged_df, df, on='SYMBOL', how='outer')

# Replace NaN values with an empty string
merged_df.fillna('', inplace=True)

# Save the merged DataFrame to a CSV file
merged_df.to_csv('merged_output.csv', index=False)
