import pytest
import yfinance as yf
import plotly.graph_objs as go
from main import plot_candlestick

# Test data retrieval
def test_data_retrieval():
    ticker = "AAPL"
    period = "1mo"
    df = yf.download(ticker, period=period, interval="1d")
    assert not df.empty, "DataFrame should not be empty for valid ticker and period"
    assert set(['Open', 'High', 'Low', 'Close']).issubset(df.columns), "DataFrame should contain OHLC data"

# Test plot generation
def test_plot_generation():
    ticker = "AAPL"
    period = "1mo"
    df = yf.download(ticker, period=period, interval="1d")
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                                         open=df['Open'],
                                         high=df['High'],
                                         low=df['Low'],
                                         close=df['Close'])])
    assert isinstance(fig, go.Figure), "The plot should be a Plotly Figure instance"

# Optional: Test plot_candlestick function directly
def test_plot_candlestick(mocker):
    ticker = "AAPL"
    period = "1mo"
    mocker.patch('yfinance.download', return_value=yf.download(ticker, period=period, interval="1d"))
    plot_candlestick(ticker, period)  # Simply checking if it runs without error

