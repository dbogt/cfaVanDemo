# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:12:06 2024

@author: Bogdan Tudose
@email: bogdan.tudose@trainingthestreet.com

"""
#%% Python 3 - Afternoon Codes
#Coffee break until 2:15pm PST

#codes to run for streamlit to install
    # pip install streamlit
    # pip install --upgrade streamlit
    # streamlit hello
        #leave email blank
        #will open a dummy dashboard


#when you're back try these two codes:
import plotly.express as px
import streamlit as st
import pandas as pd

st.title("DEMO")
st.header("Sub header")

tickers = ['AAPL','DIS','NKE']
pick = st.sidebar.selectbox("Pick a ticker:",tickers) #dropdown box

startDate = st.sidebar.date_input("Pick a start date")
endDate = st.sidebar.date_input("Pick an end date")

df = pd.read_csv(pick + ".csv", parse_dates=['Date'])
st.write(df)
    #st.write --> like print in python

dayStart = '{:%Y-%m-%d}'.format(startDate)
dayEnd = '{:%Y-%m-%d}'.format(endDate)
filterDF = df[df['Date'].between(dayStart, dayEnd)]

fig = px.line(filterDF, x='Date', y='Close')
st.plotly_chart(fig)















