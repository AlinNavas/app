import streamlit as st
import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit_extras
st.set_option('deprecation.showPyplotGlobalUse', False)
from PIL import Image


with open("img.png", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

    st.sidebar.markdown(
        f"""
        <div style="display:table;margin-bottom:0%;margin-left:-0%;">
            <img src="data:image/png;base64,{data}" width="300" height="150">
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.header("Machine Learning powered Diabetes Predictor")
    st.sidebar.markdown("Predicts the presence of diabetes based on symptoms exhibited when a patient is in a hyperglycaemic state using Support Vector Machine ML method.")   
    st.sidebar.markdown("Developed by: Dr. Alin Navas")                   



body = st.container()



with body:
    st.markdown("<h1 style='text-align: center; color: SkyBlue;'>Predict your risk of having diabetes!</h1>", unsafe_allow_html=True)
    st.markdown('  ')
    st.markdown('  ')
with open("home.jpg", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(
        f"""
        <div style="display:table;margin-bottom:0%;margin-left:20%;">
            <img src="data:image/png;base64,{data}" width="400" height="300">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('Studies have shown that a significant number of people who are diabetic are unaware of their condition. Even developed countries with high per capita expenditure on healthcare, like the US, have around 8.5 million adults with undiagnosed diabetes. This represents nearly 23 percent of all US adults with diabetes. ')
    st.markdown('On a global scale, some papers claim that 1 in 2 people living with diabetes don’t know that they have it.  ')
    st.markdown('This lack of awareness can be very dangerous. Uncontrolled diabetes mellitus may lead to many serious complications. Select the "Complications button" button to learn more about it')
    
    st.markdown('This web app can act as a screening tool to pickup undiagnosed diabetic patients via an online questionnaire. It does not require any blood investigations and is therefore widely deployable with minimal infrastructural requirements.')


from streamlit_extras.switch_page_button import switch_page


st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

col1, col2, col3 = st.columns(3)

with col2:
    want_to_predict = st.button("I want to check my risk of being diabetic!")

if want_to_predict:
    switch_page("Predict_risk_of_Diabetes")

st.markdown(' ')
st.markdown(' ')


col1, col2 = st.columns(2)

with col1:
    want_know_global = st.button("I want to know more about the global scale of this problem")

if want_know_global:
    switch_page("Global_Diabetic_Population")

with col2:
    prev_diab = st.button("I would like to learn more about complications associated with chronic diabetes.")

if prev_diab:
    switch_page("Complications_associated_with_diabetes")
