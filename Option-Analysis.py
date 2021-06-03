from live import NSELive
import streamlit as st
from pynse import *
import streamlit as st
import logging
import pandas as pd
import datetime
import json

n = NSELive()
option_chain = n.index_option_chain("NIFTY")

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")

symbols = ["NIFTY", "BANKNIFTY", "AARTIIND", "ACC", "ADANIENT", "ADANIPORTS", "ALKEM", "AMARAJABAT", "AMBUJACEM",
           "APLLTD", "APOLLOHOSP", "APOLLOTYRE", "ASHOKLEY", "ASIANPAINT", "AUBANK", "AUROPHARMA", "AXISBANK",
           "BAJAJ-AUTO", "BAJAJFINSV",
           "BAJFINANCE", "BALKRISIND", "BANDHANBNK", "BANKBARODA", "BATAINDIA", "BEL", "BERGEPAINT", "BHARATFORG",
           "BHARTIARTL", "BHEL", "BIOCON", "BOSCHLTD", "BPCL", "BRITANNIA", "CADILAHC", "CANBK", "CHOLAFIN", "CIPLA",
           "COALINDIA", "COFORGE", "COLPAL", "CONCOR", "CUB", "CUMMINSIND", "DABUR", "DEEPAKNTR", "DIVISLAB", "DLF",
           "DRREDDY", "EICHERMOT", "ESCORTS", "EXIDEIND", "FEDERALBNK", "GAIL", "GLENMARK", "GMRINFRA", "GODREJCP",
           "GODREJPROP", "GRANULES", "GRASIM", "GUJGASLTD", "HAVELLS", "HCLTECH", "HDFC", "HDFCAMC", "HDFCBANK",
           "HDFCLIFE", "HEROMOTOCO", "HINDALCO", "HINDPETRO", "HINDUNILVR", "IBULHSGFIN", "ICICIBANK", "ICICIGI",
           "ICICIPRULI", "IDEA", "IDFCFIRSTB", "IGL", "INDIGO", "INDUSINDBK", "INDUSTOWER", "INFY", "IOC", "IRCTC",
           "ITC", "JINDALSTEL", "JSWSTEEL", "JUBLFOOD", "KOTAKBANK", "L&TFH", "LALPATHLAB", "LICHSGFIN", "LT", "LTI",
           "LTTS", "LUPIN", "M&M", "M&MFIN", "MANAPPURAM", "MARICO", "MARUTI", "MCDOWELL-N", "MFSL", "MGL", "MINDTREE",
           "MOTHERSUMI", "MPHASIS", "MRF", "MUTHOOTFIN", "NAM-INDIA", "NATIONALUM", "NAUKRI", "NAVINFLUOR", "NESTLEIND",
           "NMDC", "NTPC", "ONGC", "PAGEIND", "PEL", "PETRONET", "PFC", "PFIZER", "PIDILITIND", "PIIND", "PNB",
           "POWERGRID", "PVR", "RAMCOCEM", "RBLBANK", "RECLTD", "RELIANCE", "SAIL", "SBILIFE", "SBIN", "SHREECEM",
           "SIEMENS", "SRF", "SRTRANSFIN", "SUNPHARMA", "SUNTV", "TATACHEM", "TATACONSUM", "TATAMOTORS", "TATAPOWER",
           "TATASTEEL", "TCS", "TECHM", "TITAN", "TORNTPHARM", "TORNTPOWER", "TRENT", "TVSMOTOR", "UBL", "ULTRACEMCO",
           "UPL", "VEDL", "VOLTAS", "WIPRO", "ZEEL"]

st.title("Open Interest")
try:
    selected_symbol = st.sidebar.selectbox("Select Tiker", symbols)
    logger.info(f'Will fetch the data for {selected_symbol}')
    data = None
    if selected_symbol in ["NIFTY", "BANKNIFTY"]:
        data = n.index_option_chain(selected_symbol)
    else:
        data = n.equity_option_chain(selected_symbol)
    data = pd.json_normalize(data['filtered']['data'])
    # logger.info(data)
    data_for_chart = data
    data_for_chart.index = data_for_chart.get("strikePrice")
    data_for_chart.drop(
        data_for_chart.columns.difference(
            ["CE.openInterest", "PE.openInterest"]
        ),
        1,
        inplace=True,
    )
    st.write("Open Interest")
    st.bar_chart(data_for_chart)

    data_for_changeinOpenInterest = None
    if selected_symbol in ["NIFTY", "BANKNIFTY"]:
        data_for_changeinOpenInterest = n.index_option_chain(selected_symbol)
    else:
        data_for_changeinOpenInterest = n.equity_option_chain(selected_symbol)
    # data_for_changeinOpenInterest = n.equity_option_chain(selected_symbol)
    data_for_changeinOpenInterest = pd.json_normalize(data_for_changeinOpenInterest['filtered']['data'])
    # logger.info(data_for_changeinOpenInterest)
    data_for_changeinOpenInterest.index = data_for_changeinOpenInterest.get("strikePrice")
    data_for_changeinOpenInterest.drop(
        data_for_changeinOpenInterest.columns.difference(
            ["CE.changeinOpenInterest", "PE.changeinOpenInterest"]
        ),
        1,
        inplace=True,
    )
    st.write("Changed Open Interest")
    st.bar_chart(data_for_changeinOpenInterest)
except Exception as e:
    st.error(e)
    print(e)
