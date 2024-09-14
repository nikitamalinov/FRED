import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime, timedelta
from sklearn.metrics import mean_squared_error
from math import sqrt

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/cryptoDownloadData/BTC.csv')
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    return df

# Train ARIMA model and make predictions
def train_and_predict(data, days_to_predict):
    model = ARIMA(data['close'], order=(1, 1, 1))
    results = model.fit()
    
    forecast = results.forecast(steps=days_to_predict)
    forecast_dates = pd.date_range(start=data.index[-1] + timedelta(days=1), periods=days_to_predict)
    forecast_series = pd.Series(forecast, index=forecast_dates)
    
    return forecast_series

# Calculate RMSE
def calculate_rmse(actual, predicted):
    return sqrt(mean_squared_error(actual, predicted))

# Main app
def main():
    st.title("Bitcoin Price Prediction using ARIMA")

    # Load data
    df = load_data()

    # Sidebar
    st.sidebar.header("Settings")
    days_to_predict = st.sidebar.slider("Days to predict", 1, 365, 30)

    # Train model and make predictions
    forecast = train_and_predict(df, days_to_predict)

    # Create figure
    fig = go.Figure()

    # Plot historical data
    fig.add_trace(go.Scatter(x=df.index, y=df['close'], mode='lines', name='Historical Price'))

    # Plot predicted prices
    fig.add_trace(go.Scatter(x=forecast.index, y=forecast.values, mode='lines', name='Predicted Price', line=dict(dash='dot')))

    # Update layout
    fig.update_layout(title='Bitcoin Price - Historical and Predicted',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      hovermode='x unified')

    # Display the chart
    st.plotly_chart(fig)

    # Display some statistics
    st.subheader("Statistics")
    st.write(f"Current Price: ${df['close'].iloc[-1]:,.2f}")
    st.write(f"Predicted Price (in {days_to_predict} days): ${forecast.iloc[-1]:,.2f}")

    # Calculate and display RMSE
    if len(df) >= 30:  # Ensure we have enough data for a meaningful RMSE
        historical_prediction = train_and_predict(df.iloc[:-30], 30)
        actual_values = df['close'].iloc[-30:]
        rmse = calculate_rmse(actual_values, historical_prediction)
        st.write(f"Model RMSE (based on last 30 days): ${rmse:,.2f}")

if __name__ == "__main__":
    main()