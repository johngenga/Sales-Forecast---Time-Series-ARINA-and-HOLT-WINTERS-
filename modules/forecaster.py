from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.arima.model import ARIMA

def forecast_sales_arima(data, order=(1, 1, 1), steps=12):
    """Forecast future sales using ARIMA."""
    if 'sales' in data.columns:
        model = ARIMA(data['sales'], order=order)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=steps)
        print("ARIMA Forecasted Sales:")
        print(forecast)  # Print the forecasted values for verification
        return forecast
    else:
        raise KeyError("Column 'sales' not found in the DataFrame")

def forecast_sales_holt_winters(data, seasonal_periods=12, steps=12):
    """Forecast future sales using Holt-Winters method."""
    if 'sales' in data.columns:
        model = ExponentialSmoothing(data['sales'], trend='add', seasonal='add', seasonal_periods=seasonal_periods)
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=steps)
        print("Holt-Winters Forecasted Sales:")
        print(forecast)  # Print the forecasted values for verification
        return forecast
    else:
        raise KeyError("Column 'sales' not found in the DataFrame")
