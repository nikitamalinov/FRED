import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/cryptoDownloadData/BTC.csv')
    df['date'] = pd.to_datetime(df['date'])
    return df

# Identify halving dates
def get_halving_dates():
    return [
        datetime(2012, 11, 28),
        datetime(2016, 7, 9),
        datetime(2020, 5, 11),
        datetime(2024, 4, 27),  # Estimated
    ]

# Simple predictive model
def predict_price(df, days_since_halving):
    last_price = df['close'].iloc[-1]
    growth_rate = 0.001  # Adjust this value to change the prediction
    return last_price * (1 + growth_rate) ** days_since_halving

# Main app
def main():
    st.title("Bitcoin Price Prediction based on Halving")

    # Load data
    df = load_data()

    # Sidebar
    st.sidebar.header("Settings")
    days_to_predict = st.sidebar.slider("Days to predict", 1, 1000, 365)

    # Get halving dates
    halving_dates = get_halving_dates()

    # Create figure
    fig = go.Figure()

    # Plot historical data
    fig.add_trace(go.Scatter(x=df['date'], y=df['close'], mode='lines', name='Historical Price'))

    # Plot halving lines
    for date in halving_dates:
        fig.add_vline(x=date.strftime('%Y-%m-%d'), line_dash="dash", line_color="red")
        fig.add_annotation(x=date.strftime('%Y-%m-%d'), y=1, yref='paper', text="Halving", showarrow=False, yshift=10)

    # Predict future prices
    last_date = df['date'].iloc[-1]
    future_dates = pd.date_range(start=last_date, periods=days_to_predict)
    last_halving = max(date for date in halving_dates if date <= last_date)
    predicted_prices = [predict_price(df, (date - last_halving).days) for date in future_dates]

    # Plot predicted prices
    fig.add_trace(go.Scatter(x=future_dates, y=predicted_prices, mode='lines', name='Predicted Price', line=dict(dash='dot')))

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
    st.write(f"Predicted Price (in {days_to_predict} days): ${predicted_prices[-1]:,.2f}")

if __name__ == "__main__":
    main()