import streamlit as st
import pandas as pd
import requests
import os

FRED_API_KEY = st.secrets['FRED_API_KEY']
def tags():
  url=f"https://api.stlouisfed.org/fred/tags?api_key={FRED_API_KEY}&file_type=json"
  r = requests.get(url)
  data = r.json()
  df = pd.DataFrame(data['tags'])
  df.index = df.index + 1
  return df


def sources():
  url = f"https://api.stlouisfed.org/fred/sources?api_key={FRED_API_KEY}&file_type=json"
  r = requests.get(url)
  data = r.json()

  df = pd.DataFrame(data['sources'])
  df.index = df.index + 1
  return df


def releases():
  url = f"https://api.stlouisfed.org/fred/releases?api_key={FRED_API_KEY}&file_type=json"
  r = requests.get(url)
  data = r.json()

  df = pd.DataFrame(data['releases'])
  df.index = df.index + 1
  return df


tags_df = tags()
st.header("Get all tags")
st.dataframe(tags_df, use_container_width=True, column_order=[ 'name',  'popularity', 'notes',  'group_id','created', 'series_count'])


sources_df = sources()
st.header("Get all sources")
st.dataframe(sources_df, use_container_width=True, column_order=['name',  'link','notes', 'realtime_start', 'realtime_end'])


releases_df = releases()
st.header("Get all releases")
st.dataframe(releases_df, use_container_width=True, column_order=['name', 'link', 'press_release', 'notes', 'realtime_start', 'realtime_end'])



