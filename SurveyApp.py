# Author: Yibo Wang
# Date: 11/15/2024
# Description: Create the Survey App interface and provide functionalities
import streamlit as st
from PIL import Image
import time

class SurveyApp:
    def __init__(self):
        self.option_list = []
        
    def local_css(self, file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
            
    def set_background(self):
        page_bg_img = '''
        <style>
        body {
        background-image: url("https://sfwallpaper.com/images/background-image-for-website-1.jpg");
        background-size: cover;
        }
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
        
    def display_header(self):
        st.title("City Match")
        t = "<div><span class='bold'>By completing the following survey to find cities that fit you the best</span></div>"
        st.markdown(t, unsafe_allow_html=True)
        img = Image.open("american map.jpg")
        st.image(img, width=700)
        
    def get_survey_responses(self):
        # Pollution
        pollution_sub = "<div><span class='color'>Consider the pollution as an essential factor to rank your cities?</span></div>"
        st.markdown(pollution_sub, unsafe_allow_html=True)
        pollution_consideration = st.radio("", ("Yes","No"), key="pollution_key")
        self.option_list.append(1 if pollution_consideration == 'Yes' else 0)
        st.success(pollution_consideration)
        
        # Crime
        crime_sub = "<div><span class='color'>Consider the crime rate as an essential factor to rank your cities?</span></div>"
        st.markdown(crime_sub, unsafe_allow_html=True)
        crime_status = st.radio("", ("Yes","No"), key="crime_key")
        self.option_list.append(1 if crime_status == 'Yes' else 0)
        st.success(crime_status)
        
        # Income
        income_sub = "<div><span class='color'>What is your expected average income?</span></div>"
        st.markdown(income_sub, unsafe_allow_html=True)
        income_option = st.selectbox("", ('None','Low','Medium','High'), key="income_key")
        st.write('You selected:', income_option)
        self.option_list.append({'None': 0, 'Low': 1, 'Medium': 2, 'High': 3}[income_option])
        
        # Education
        education_sub = "<div><span class='color'>Expected Educational Level?</span></div>"
        st.markdown(education_sub, unsafe_allow_html=True)
        education_option = st.selectbox("", ('None','Low','Medium','High'), key="education_key")
        st.write('You selected:', education_option)
        self.option_list.append({'None': 0, 'Low': 1, 'Medium': 2, 'High': 3}[education_option])
        
        # Health
        health_sub = "<div><span class='color'>Expected Health Care Level?</span></div>"
        st.markdown(health_sub, unsafe_allow_html=True)
        health_option = st.selectbox("", ('None','Low','Medium','High'), key="health_key")
        st.write('You selected:', health_option)
        self.option_list.append({'None': 0, 'Low': 1, 'Medium': 2, 'High': 3}[health_option])
        
        # Population
        population_sub = "<div><span class='color'>Expected Population Density?</span></div>"
        st.markdown(population_sub, unsafe_allow_html=True)
        population_option = st.selectbox("", ('None','Low','Medium','High'), key="population_key")
        st.write('You selected:', population_option)
        self.option_list.append({'None': 0, 'Low': 1, 'Medium': 2, 'High': 3}[population_option])
        
    def show_submit_button(self):
        if st.button("Submit", key="submit_key"):
            my_bar = st.progress(0)
            for n in range(100):
                my_bar.progress(n)
                time.sleep(0.000001)
            with st.spinner('Waiting'):
                time.sleep(0.1)
            st.success('Submitted')
            
    def run(self):
        self.set_background()
        self.local_css("style.css")
        self.display_header()
        self.get_survey_responses()
        self.show_submit_button()
        return self.option_list