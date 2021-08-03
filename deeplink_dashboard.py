import streamlit as st
import pandas as pd
import numpy as np

st.title("Deeplink Test Data")
st.text('Region: us-east-1')

params_to_show = ['params/country', 'params/artist', 'params/song', 'params/album', 'params/soundtrack', 'params/search']

file = st.file_uploader('Upload deeplink CSV', ['csv'])
if file:
    data = pd.read_csv(file)
    #data = get_data('/Users/znusbaum/Downloads/Aug3-us-east-1-deeplinks.csv')

    apple_data = data[params_to_show + ['apple_data/type', 'apple_data/deeplink']]
    spotify_data = data[params_to_show + ['spotify_data/type', 'spotify_data/deeplink']]
    amazon_data = data[params_to_show + ['amazon_data/type', 'amazon_data/deeplink']]

    service = st.radio("Choose a service", ('Spotify', 'Amazon', 'Apple'))

    if service == "Spotify":
        st.header("Spotify")
        st.table(spotify_data)
    elif service == "Apple":
        st.header("Apple")
        st.table(apple_data)
    elif service == "Amazon":
        st.header("Amazon")
        st.table(amazon_data)