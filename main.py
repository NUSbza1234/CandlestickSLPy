import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime, timedelta

def plot_candlestick(ticker, period):
    df = yf.download(ticker, period=period, interval="1d")
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    fig.update_layout(title=f'Candlestick chart for {ticker}',
                      yaxis_title='Stock Price (USD)',
                      xaxis_title='Date')
    st.plotly_chart(fig)

st.title('Candlestick Chart Viewer')

ticker = st.text_input('Enter Stock Ticker:', 'AAPL')

timeframes = {
    "10 years ago": "10y",
    "5 years ago": "5y",
    "3 years ago": "3y",
    "1 year ago": "1y",
    "6 months ago": "6mo",
    "3 months ago": "3mo",
    "1 month ago": "1mo",
    "Year to date (YTD)": "ytd"
}

timeframe = st.selectbox("Select Timeframe:", list(timeframes.keys()))

# Plot the default ticker 'AAPL' when the app runs
if ticker:
    plot_candlestick(ticker, timeframes[timeframe])

