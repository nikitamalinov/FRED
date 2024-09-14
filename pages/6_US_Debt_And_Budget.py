import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(layout="wide")



def create_iframe(url, width="100%", height=1000):
    # Use HTML to create a responsive iframe
    iframe_html = f"""
        <style>
            .iframe-container {{
                position: relative;
                width: 100%;
                padding-bottom: 56.25%; /* 16:9 aspect ratio */
                height: 0;
                overflow: hidden;
            }}
            .iframe-container iframe {{
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
            }}
        </style>
        <div class="iframe-container">
            <iframe src="{url}" width="100%" height="100%" frameborder="0"></iframe>
        </div>
    """
    st.components.v1.html(iframe_html, height=height)
    
create_iframe("https://www.usdebtclock.org/")

create_iframe("https://www.usaspending.gov/explorer/budget_function")

