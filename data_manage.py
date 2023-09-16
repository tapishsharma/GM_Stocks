import pandas as pd
import glob
from datetime import datetime

# Define a function to convert the date strings to datetime objects
def convert_to_datetime(date_str):
    return datetime.strptime(date_str, '%d%b%Y')

# Create an empty DataFrame to store the merged data
merged_df = pd.DataFrame()

# Use the glob module to get a list of all the CSV files in the csv_files folder
file_list = glob.glob('csv_files/cm*.csv')

# Loop through each file, read it into a DataFrame, and merge it with the merged_df
for file in file_list:
    df = pd.read_csv(file)
    df['close'] = df['close'].apply(convert_to_datetime)  # Convert close column to datetime
    merged_df = pd.merge(merged_df, df, on='symbol', how='outer')

# Save the merged data to a new CSV file
merged_df.to_csv('merged_data.csv', index=False)
