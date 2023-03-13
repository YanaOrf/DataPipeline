import gspread
import streamlit as st
import pandas as pd
def get_data():
    gc = gspread.service_account(filename="./service_account.json")
    wks = gc.open("Tesla price").sheet1
    dataframe = pd.DataFrame(wks.get_all_records())
    return dataframe
  


def display():
    data_chart=get_data()
    st.line_chart(data=data_chart,x="Date",y="Price")

display()