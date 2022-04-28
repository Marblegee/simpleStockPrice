from tracemalloc import start
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
         ## Simple Stock Price App
         
         Shown are the stock **closing price** and ***volume*** of Google!
         
         """)

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

# historical price data 
tickerDf = tickerData.history(period='id', start='2010-10-16', end='2022-4-26')

st.write("""
         ### Closing Price
         """)

st.line_chart(tickerDf.Close)

st.write("""
         ### Volume
         """)

st.line_chart(tickerDf.Volume)

