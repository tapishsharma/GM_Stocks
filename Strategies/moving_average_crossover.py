# days1 = int(input("Enter the value for days1: "))
# days2 = int(input("Enter the value for days2: "))
# percentage_threshold = float(input("Enter the percentage threshold: "))

import csv
import os
import pandas as pd

# Define the input and output file paths
input_file = os.path.join('..', 'stock_data.csv')
output_file = os.path.join('result.csv')

# User-defined parameters
days1 = 10
days2 = 20
percentage_threshold_1 = 0.01
percentage_threshold_2 = 0.015

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(input_file)

# Create an empty list to store symbols that meet the criteria
selected_symbols = []

# Iterate through the DataFrame to check for crossover and percentage condition
for index, row in df.iterrows():
    symbol = row['SYMBOL']
    dma1 = row.iloc[-days1]
    dma2 = row.iloc[-days2]
    value = dma1/dma2
    print(dma1,dma2)

    if (dma1 / dma2 < 1 + percentage_threshold_2) and (dma1 / dma2 > 1 + percentage_threshold_1):
        selected_symbols.append([symbol])  # Store each symbol in a list

# Write the selected symbols to the result CSV file with each symbol in a separate row
with open(output_file, 'w', newline='') as result_csv:
    writer = csv.writer(result_csv)
    writer.writerow(['SYMBOL'])
    writer.writerows(selected_symbols)

print("Results saved in result.csv")
