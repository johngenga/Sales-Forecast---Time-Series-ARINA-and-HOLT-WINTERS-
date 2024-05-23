import pandas as pd

def load_data(file_path):
    """Load sales data from a CSV file."""
    data = pd.read_csv(file_path)
    print("Loaded Data:")
    print(data.head())  # Print the first few rows of the DataFrame for verification
    return data
