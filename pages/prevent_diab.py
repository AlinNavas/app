import streamlit as st
import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit_extras
st.set_option('deprecation.showPyplotGlobalUse', False)
from PIL import Image
from streamlit_extras.switch_page_button import switch_page



body = st.container()

with body:
    st.markdown("<h1 style='text-align: center; color: SkyBlue;'>Learn more about preventing diabetes</h1>", unsafe_allow_html=True)
    
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')
    video_file = open('trial_files/prev_vid.mp4', 'rb')
    vid = video_file.read()
    st.video(vid)
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')



    col1, col2, col3 = st.columns(3)

with col2:
    want_to_predict = st.button("Now I'd like to know my risk of being diabetic!")

if want_to_predict:
    switch_page("ml_page")