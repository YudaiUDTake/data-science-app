import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2011-1-31', end='2021-1-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
