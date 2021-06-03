from jugaad_data.nse import NSELive
import streamlit as st

n = NSELive()
option_chain = n.index_option_chain("NIFTY")

for option in option_chain['filtered']['data']:
    st.write("CE_LastPrice:{}\tstrikePrice:{}\tPE_LastPrice:{}".format(option['CE']['lastPrice'], option['strikePrice'],
                                                                       option['PE']['lastPrice']))
