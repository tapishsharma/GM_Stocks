import csv
import os
import pandas as pd

# Define the input and output file paths
input_file = os.path.join('..', 'stock_data.csv')
output_file = os.path.join('result.csv')

# User-defined parameters
days1 = int(input("Enter the value for days1: "))
days2 = int(input("Enter the value for days2: "))
divergence = float(input("Enter the value for divergence: "))
threshold = float(input("Enter the value for threshold: "))
above = input("Enter 'y' for above or 'n' for below: ").lower() == 'y'

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(input_file)

# Create an empty list to store symbols that meet the criteria
selected_symbols = []

# Iterate through the DataFrame to check for crossover and percentage condition
for index, row in df.iterrows():
    symbol = row['SYMBOL']
    latest_prices = row.iloc[:].values[1:].astype(float)  # Extract the latest prices
    # Calculate the moving averages
    dma1 = sum(latest_prices[-days1:]) / days1
    dma2 = sum(latest_prices[-days2:]) / days2

    # Check if the crossover and percentage conditions are met
    if (dma1 / dma2 > divergence - threshold) and (dma1 / dma2 < divergence + threshold):
        if above and dma1 > dma2:
            selected_symbols.append([symbol])  # Store each symbol in a list
        elif not above and dma1 < dma2:
            selected_symbols.append([symbol])  # Store each symbol in a list

# Write the selected symbols to the result CSV file with each symbol in a separate row
with open(output_file, 'w', newline='') as result_csv:
    writer = csv.writer(result_csv)
    writer.writerow(['SYMBOL'])
    writer.writerows(selected_symbols)

print("Results saved in result.csv")
