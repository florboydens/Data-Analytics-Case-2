import pandas as pd

# Define paths to the CSV files
data_path = 'data/data.csv'
test_path = 'data/test.csv'
stores_path = 'data/stores.csv'
transactions_path = 'data/transactions.csv'
oil_path = 'data/oil(India).csv'
holidays_events_path = 'data/holidays_events(India).csv'
items_path = 'data/items.csv'

# Loading the datasets
def load_csv(file_path):
    return pd.read_csv(file_path)

data = load_csv(data_path)
test = load_csv(test_path)
stores = load_csv(stores_path)
transactions = load_csv(transactions_path)
oil = load_csv(oil_path)
holidays_events = load_csv(holidays_events_path)
items = load_csv(items_path)

# Example: Display the first few rows of each dataset
print(data.head())
print(test.head())
print(stores.head())
print(transactions.head())
print(oil.head())
print(holidays_events.head())
print(items.head())
