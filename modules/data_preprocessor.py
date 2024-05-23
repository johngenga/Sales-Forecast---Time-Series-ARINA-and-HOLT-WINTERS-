import pandas as pd


def preprocess_data(data):
    """Preprocess the sales data."""
    # Handle missing values
    data = data.fillna(0)

    # Convert date column to datetime type
    if 'date' in data.columns:
        data['date'] = pd.to_datetime(data['date'])
    else:
        raise KeyError("Column 'date' not found in the DataFrame")

    print("Preprocessed Data:")
    print(data.head())  # Print the first few rows after preprocessing for verification
    return data


def aggregate_data(data):
    """Aggregate the sales data by month."""
    if 'date' in data.columns and 'sales' in data.columns:
        data['month'] = data['date'].dt.to_period('M')
        monthly_sales = data.groupby('month')['sales'].sum().reset_index()
        print("Aggregated Monthly Sales Data:")
        print(monthly_sales.head())  # Print the first few rows of the aggregated data for verification
        return monthly_sales
    else:
        raise KeyError("Required columns 'date' and/or 'sales' not found in the DataFrame")
