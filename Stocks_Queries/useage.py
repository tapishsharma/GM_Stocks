import pandas as pd

def query_stock_data(csv_file, conditions):
    """
    Query stock data from a CSV file based on multiple conditions.

    Args:
    - csv_file (str): The path to the CSV file containing stock data.
    - conditions (list): A list of conditions in the format (parameter, operator, value).
                         Supported operators: '==', '>', '<', '>=', '<=', '!='.
                         Example conditions: [('Market Cap', '>', 1000), ('ROCE', '>', 15)]

    Returns:
    - DataFrame: A Pandas DataFrame containing rows that match the query criteria.
    """
    try:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(csv_file)

        # Initialize a filter mask
        mask = pd.Series([True] * len(df))

        # Apply each condition to the filter mask
        for param, operator, value in conditions:
            if operator == '==':
                mask = mask & (df[param] == value)
            elif operator == '>':
                mask = mask & (df[param] > value)
            elif operator == '<':
                mask = mask & (df[param] < value)
            elif operator == '>=':
                mask = mask & (df[param] >= value)
            elif operator == '<=':
                mask = mask & (df[param] <= value)
            elif operator == '!=':
                mask = mask & (df[param] != value)

        # Apply the filter mask to the DataFrame
        queried_data = df[mask]

        return queried_data
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
# csv_file = 'stock_data.csv'  # Replace with the path to your CSV file
# conditions = [('Market Cap', '>', 1000), ('ROCE', '>', 15)]
# result = query_stock_data(csv_file, conditions)
# print(result)
