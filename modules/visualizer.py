import pandas as pd
import matplotlib.pyplot as plt


def plot_sales(data):
    """Plot the sales data."""
    plt.figure(figsize=(10, 5))
    plt.plot(data['month'].astype(str), data['sales'], label='Actual Sales')
    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Monthly Sales')
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()


def plot_forecast(data, arima_forecast, hw_forecast):
    """Plot the sales data and the forecasts."""
    plt.figure(figsize=(10, 5))
    plt.plot(data['month'].astype(str), data['sales'], label='Actual Sales')

    last_month = data['month'].max().to_timestamp()
    future_months = pd.date_range(start=last_month + pd.offsets.MonthEnd(1), periods=len(arima_forecast), freq='ME')
    future_months_str = future_months.strftime('%Y-%m')

    plt.plot(future_months_str, arima_forecast, label='ARIMA Forecasted Sales')
    plt.plot(future_months_str, hw_forecast, label='Holt-Winters Forecasted Sales')

    plt.xlabel('Month')
    plt.ylabel('Sales')
    plt.title('Sales Forecast')
    plt.legend()
    plt.xticks(rotation=45)
    plt.show()
