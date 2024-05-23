from modules.data_loader import load_data
from modules.data_preprocessor import preprocess_data, aggregate_data
from modules.visualizer import plot_sales, plot_forecast
from modules.forecaster import forecast_sales_arima, forecast_sales_holt_winters


def main():
    # Load the data
    data = load_data('C:/Users/User/PycharmProjects/supply_chain_project/data/sales_data.csv')

    # Preprocess the data
    data = preprocess_data(data)

    # Aggregate the data
    monthly_sales = aggregate_data(data)

    # Plot the sales data
    plot_sales(monthly_sales)

    # Forecast sales using ARIMA
    arima_forecast = forecast_sales_arima(monthly_sales, order=(1, 1, 1), steps=12)

    # Forecast sales using Holt-Winters
    hw_forecast = forecast_sales_holt_winters(monthly_sales, seasonal_periods=12, steps=12)

    # Plot the forecasts
    plot_forecast(monthly_sales, arima_forecast, hw_forecast)


if __name__ == '__main__':
    main()
