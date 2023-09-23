import pandas as pd

def get_prices_from_user_input( symbol, num_days):
    try:
        df = pd.read_csv('stock_data.csv')
        symbol = symbol.upper()
        symbol_data = df[df['SYMBOL'] == symbol]
        if symbol_data.empty:
            return None
        prices = symbol_data.iloc[:, -num_days:].values.tolist()[0]
        prices = [price for price in prices if not pd.isna(price)]
        return prices
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
