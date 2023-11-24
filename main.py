import yfinance as yf
import streamlit as st
from PIL import Image

from urllib.request import urlopen


# titles and subtitles
st.title("Cryptocurrency Daily Prices | ₿")
st.header("Main Dashboard")
st.subheader("you can add more crypto in code")


# defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'
Ripple = "XRP-USD"
BitcoinCash = "BCH-USD"


# access data from yahoo finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)
XRP_Data = yf.Ticker(Ripple)
BCH_Data = yf.Ticker(BitcoinCash)


# fetch price history from yahoo finance
BTCHis = BTC_Data.history(period="max")
ETHHis = ETH_Data.history(period="max")
XRPHis = XRP_Data.history(period="max")
BCHHis = BCH_Data.history(period="max")



# fetch crypto data for the dataframe
BTC = yf.download(Bitcoin, start="2023-11-20", end="2023-11-24")
ETH = yf.download(Ethereum, start="2023-11-20", end="2023-11-24")
XRP = yf.download(Ripple, start="2023-11-20", end="2023-11-24")
BCH = yf.download(BitcoinCash, start="2023-11-20", end="2023-11-24")


# Bitcoin
st.write("BITCOIN ($)")
imageBTC = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1.png'))
# display image
st.image(imageBTC)
# display dataframe
st.table(BTC)
# display chart
st.bar_chart(BTCHis.Close)


# Ethereum
st.write("Ethereum ($)")
imageETH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png'))
# display image
st.image(imageETH)
# display dataframe
st.table(ETH)
# display chart
st.bar_chart(ETHHis.Close)


# Ripple
st.write("Ripple ($)")
imageXRP = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/52.png'))
# display image
st.image(imageXRP)
# display dataframe
st.table(XRP)
# display chart
st.bar_chart(XRPHis.Close)


# BitcoinCash
st.write("BitcoinCash ($)")
imageBCH = Image.open(urlopen('https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png'))
# display image
st.image(imageBCH)
# display dataframe
st.table(BCH)
# display chart
st.bar_chart(BCHHis.Close)


