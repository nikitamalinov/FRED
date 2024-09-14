# Listing and delisting status
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data/alphavantage/listing_status_combined.csv')

active_count = df[df['status'] == 'Active'].shape[0]
st.write(f"Number of Active Companies:  {active_count}")


st.line_chart(df['ipoDate'].value_counts().sort_index())	
df['ipoDate'] = pd.to_datetime(df['ipoDate'], errors='coerce')

active_df = df[df['status'] == 'Active']
active_df['year'] = active_df['ipoDate'].dt.year


ipo_counts = active_df.groupby('year').size()
ipo_counts.index = ipo_counts.index.astype(str) # convert index to string for plotting it as 1990 instead of 1,990
ipo_counts = ipo_counts.cumsum()



st.write('Number of Active Companies')
st.line_chart(ipo_counts)



st.dataframe(df)