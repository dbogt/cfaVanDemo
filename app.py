import pandas as pd
import streamlit as st

st.title("DEMO")
tickers = ['AAPL','NFLX']
pick = st.selectbox("Pick ticker",tickers)
st.write("You picked " + pick)
