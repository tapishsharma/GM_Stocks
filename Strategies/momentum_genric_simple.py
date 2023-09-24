import pandas as pd
import os

def momentum_genric_simple(input_csv_file, output_csv_file, num_days):
    try:
        # Read the input CSV file into a DataFrame
        df = pd.read_csv(input_csv_file)
        
        # Calculate the new column values for all rows by dividing last column by num_days columns back
        df['New_Column'] = df.iloc[:, -1] / df.iloc[:, -1 - num_days]
        
        # Round the new column values to three decimal places
        df['New_Column'] = df['New_Column'].round(3)
        
        # Create a new DataFrame with only the first symbol column and the new column
        df_result = df[['SYMBOL', 'New_Column']]
        
        # Sort the DataFrame in descending order based on the new column
        df_result_sorted = df_result.sort_values(by='New_Column', ascending=False)
        
        # Save the resulting DataFrame to the specified output CSV file
        df_result_sorted.to_csv(output_csv_file, index=False, header=False)
        
        return True
    except Exception as e:
        return False

# Define the fixed input CSV file path
input_csv_file = os.path.join('..', 'stock_data.csv')

# Ask the user to input the number of days
num_days = int(input("Enter the number of days: "))

# Specify the desired output CSV file name
output_csv_file = "result.csv"

if momentum_genric_simple(input_csv_file, output_csv_file, num_days):
    print(f"Sorted data saved to {output_csv_file}.")
else:
    print("Error processing the CSV file.")
