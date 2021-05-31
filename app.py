from pynse import *
from logging import info, error, fatal, debug, critical
import pandas as pd
import datetime
import json
# from pymongo import MongoClient
import sqlite3

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")
nse = Nse()
conn = sqlite3.connect('Option-chain.db')

symbols = ["AARTIIND", "ACC", "ADANIENT", "ADANIPORTS", "ALKEM", "AMARAJABAT", "AMBUJACEM", "APLLTD", "APOLLOHOSP",
           "APOLLOTYRE", "ASHOKLEY", "ASIANPAINT", "AUBANK", "AUROPHARMA", "AXISBANK", "BAJAJ-AUTO", "BAJAJFINSV",
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


def get_data(symbol):
    df = nse.option_chain(symbol)
    # df.index = df.get("strikePrice")
    # df.drop(
    #     df.columns.difference(
    #         ["CE.openInterest", "PE.openInterest"]
    #     ),
    #     1,
    #     inplace=True,
    # )
    df.to_sql(name=symbol, con=conn, if_exists="append")


def read_sql(symbol):
    try:
        c = conn.cursor()
        for row in c.execute(f'SELECT * FROM {symbol} ORDER BY strikePrice'):
            print(row)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    for symbol in symbols:
        get_data(symbol)
        read_sql(symbol)
