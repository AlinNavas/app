import streamlit as st
import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit_extras
st.set_option('deprecation.showPyplotGlobalUse', False)
from streamlit_extras.switch_page_button import switch_page


chart=st.container()
ii_para=st.container()

with chart: 
    st.markdown("<h1 style='text-align: center; color: LightSkyBlue;'>Diabetes on a Worldwide Scale Over the Years</h1>", unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    df= pd.read_csv("data/idf_count_diabetes.csv")
    st.markdown("<h5 style='text-align: center; color: black;'>View the increase in diabetic population in different region by selecting the year of choice</h5>", unsafe_allow_html=True)

    st.markdown("")
    year = st.selectbox('Select Year',df.columns[3:8])


    plt.figure(figsize=(5,5))
    plt.bar(df['Region'],df[year])
    plt.xlabel('Region')
    plt.ylabel('Diabetic population')
    plt.xticks(rotation=30,fontsize=10,ha="right")
    plt.yticks(range(0,280000,20000))
    plt.title(f'No of individuals with diabetes in {year}')
    plt.tight_layout()
    st.pyplot(plt)

with ii_para:

    st.markdown("<h6 style='text-align: center; color: black;'>This increase in diabetic patients combined with limited access to healthcare facilities has led to disastrous impacts on the healthcare systems of developing nations.</h6>", unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
col1, col2, col3 = st.columns(3)

with col2:
    want_to_predict = st.button("Now I'd like to know my risk of being diabetic!")

if want_to_predict:
    switch_page("ml_page")