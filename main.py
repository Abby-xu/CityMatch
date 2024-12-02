# Author: Abby Xu
# Date: 12/02/2024

import webbrowser
import pandas as pd
from PIL import Image
import streamlit as st

from SurveyApp import *

def display_results(result_data):
    def card(rank, city_name, avg_income=100, population=1000, crime=23, img="1.jpg", sentence="this is a sentence", link='https://realestate.usnews.com/places/rankings/best-places-to-live'):
        st.markdown('----')
        col1, col2 = st.columns(2)
        col1.header(city_name)
        col1.markdown(":sunglasses: #"+str(rank)+" in Best Places to live")
        col1.write(sentence)
        if st.button("more", key=f"more_button_{rank}"):
            webbrowser.open_new_tab(link)
        
        image = Image.open(img)
        col2.image(image, width=300)
        col2.subheader(f"Average income:{avg_income}")
        col2.subheader(f"Population:{population}")
        col2.subheader(f"Crime rate:{crime}")
        st.markdown('----')

    # Background
    st.markdown('''
    <style>
    body {
    background-image: url("https://sfwallpaper.com/images/background-image-for-website-1.jpg");
    background-size: cover;
    }
    </style>
    ''', unsafe_allow_html=True)

    st.title("Search Results")
    city_show = st.slider("Please select the number of cities you want to check", 
                         min_value=1, max_value=15, step=1, key="city_slider_key")
    st.write(f"There is the list of {city_show} cities we selected for you")

    # Display map
    map_data = pd.DataFrame({
        'awesome cities': result_data[0][:city_show],
        'lat': result_data[1][:city_show],
        'lon': result_data[2][:city_show]
    })
    st.map(map_data)

    # Display city cards
    for i in range(city_show):
        card(rank=i+1,
             city_name=result_data[0][i],
             img=f"photo_city/{result_data[7][i]}",
             sentence=result_data[6][i],
             avg_income=result_data[3][i],
             population=result_data[4][i],
             crime=result_data[5][i],
             link=result_data[8][i])
        
def main():
    survey = SurveyApp()
    user_preferences = survey.run()
    
    # display results where the `result_data` should be processed by class CityAnalyzer
    # display_results(result_data)

if __name__ == '__main__':
    main()