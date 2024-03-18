import pandas as pd

# Define paths to the CSV files
data_path = 'path/to/data.csv'
test_path = 'path/to/test.csv'
stores_path = 'path/to/stores.csv'
transactions_path = 'path/to/transactions.csv'
oil_path = 'path/to/oil(India).csv'
holidays_events_path = 'path/to/holidays_events(India).csv'

# Loading the datasets
def load_csv(file_path):
    return pd.read_csv(file_path)

data = load_csv(data_path)
test = load_csv(test_path)
stores = load_csv(stores_path)
transactions = load_csv(transactions_path)
oil = load_csv(oil_path)
holidays_events = load_csv(holidays_events_path)

# Example: Display the first few rows of each dataset
print(data.head())
print(test.head())
print(stores.head())
print(transactions.head())
print(oil.head())
print(holidays_events.head())
