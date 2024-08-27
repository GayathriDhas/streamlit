import streamlit as st
import yfinance as yf
import datetime

ticker_symbol = st.text_input("Enter the stock name","AAPL")
start_date = st.date_input("START_DATE", value = datetime.date("2018/06/05"))
end_date = st.date_input("END_DATE", value = datetime.date("2023/01/07"))
data = yf.download(ticker_symbol,start=start_date,end=end_date)
st.write(data)

st.line_chart(data["close"])