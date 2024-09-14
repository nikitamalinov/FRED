import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st

def show():
    st.title("VIX (Volatility Index) Chart")

    # Create a dictionary for periods
    period_options = {
        "1 Year": "1y",
        "2 Years": "2y",
        "5 Years": "5y",
        "10 Years": "10y",
        "20 Years": "20y",
        "30 Years": "30y",
        "Max": "max"
    }

    # Add a selectbox to choose the period
    selected_period = st.selectbox("Select Time Period:", list(period_options.keys()))

    # Download VIX data from Yahoo Finance based on selected period
    vix_data = yf.download("^VIX", period=period_options[selected_period])

    # Plot the data using matplotlib
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(vix_data.index, vix_data['Close'], label="VIX Closing Price")
    ax.set_xlabel("Date")
    ax.set_ylabel("VIX")
    ax.set_title(f"VIX Chart ({selected_period})")
    ax.legend()
    
    # Show the chart in Streamlit
    st.pyplot(fig)
