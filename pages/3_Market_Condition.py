from math import e
import requests
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from components.Market_Condition import vix

st.write("In Progress")


# ALPHAVANTAGE_API_KEY = st.secrets["ALPHAVANTAGE_API_KEY"]

# apiUrls = {
#     "CPI": f"https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey={ALPHAVANTAGE_API_KEY}",
#     "GDP": f"https://www.alphavantage.co/query?function=GDP&interval=quarterly&apikey={ALPHAVANTAGE_API_KEY}",
#     "INFLATION": f"https://www.alphavantage.co/query?function=INFLATION&interval=monthly&apikey={ALPHAVANTAGE_API_KEY}",
#     "TREASUARY": f"https://www.alphavantage.co/query?function=TREAUARY&interval=daily&apikey={ALPHAVANTAGE_API_KEY}",
# }


# @st.cache_data
# def getData(apiName):
#     url = apiUrls[apiName]
#     response = requests.get(url)
#     data = response.json()

#     if "data" not in data:
#         print(data)
#         raise RuntimeError(
#             "Alpha Vantage API Error. It's either down or you've exceeded the number of requests allowed."
#         )

#     print("Data : ", data)

#     data_points = data["data"]
#     df = pd.DataFrame(data_points)
#     df["date"] = pd.to_datetime(df["date"])
#     df["value"] = pd.to_numeric(df["value"])
#     df.sort_values(by="date", inplace=True)
#     df.rename(columns={"value": apiName}, inplace=True)

#     return df


# try:
#     st.title("CPI Data")
#     st.line_chart(getData("CPI").set_index("date")["CPI"])

#     st.title("Inflation")
#     st.line_chart(getData("INFLATION").set_index("date")["INFLATION"])

#     cpi_df = getData("CPI")
#     inflation_df = getData("INFLATION")

#     merged_df = pd.merge(cpi_df, inflation_df, on="date", how="inner")

#     st.title("CPI and Inflation Data")

#     st.line_chart(merged_df.set_index("date"))
# except RuntimeError as e:
#     st.error(str(e))
# vix.show()
