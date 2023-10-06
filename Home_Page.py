import streamlit as st
import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit_extras
st.set_option('deprecation.showPyplotGlobalUse', False)



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

    st.sidebar.header("Diabetes Predictor")
    st.sidebar.markdown("I developed a screening tool while I was in medical school that can predict the presence of diabetes based on symptoms exhibited when a patient is in a hyperglycaemic state using ML XYZ methods.")   
    st.sidebar.markdown("Developed by: Dr. Alin Navas")                   

import streamlit.components.v1 as components
p = open("trial.htm",'r',encoding="ISO-8859-1")
components.html(p.read())

header = st.container()
chart = st.container()
ii_para =st.container()

with header:
    st.title('Predicting diabetic risk')
    st.markdown('The global prevalence of diabetes mellitus in 2019 was around 9.3% which is estimated to rise to 10.2% by 2030 and 10.9% by 2045. This future spike in diabetes can be attributed to a number of factors including the rising standard of living in developing nations which is generally associated with increased availability and consumption of processed foods and transitioning to sedentary lifestyles. ')


with chart:

    df= pd.read_csv("data/idf_count_diabetes.csv")
    st.markdown("View the increase in diabetic population in different region by selecting the year of choice")
    year = st.selectbox('Select Year',df.columns[3:8])


    plt.figure(figsize=(6,6))
    plt.bar(df['Region'],df[year])
    plt.xlabel('Region')
    plt.ylabel('Diabetic population')
    plt.xticks(rotation=30,fontsize=10,ha="right")
    plt.yticks(range(0,280000,20000))
    plt.title(f'No of individuals with diabetes in {year}')
    plt.tight_layout()
    st.pyplot(plt)

with ii_para:

    st.markdown('This combined with limited access to healthcare facilities has led to a massive underestimation of the prevalence of diabetes in developing nations. Studies have shown that one in two people living with diabetes are unaware of their condition. This is especially dangerous as chronic uncontrolled diabetes can manifest itself as several irreversible and serious complications with lifelong impacts.')

    st.markdown('This approach does not require any blood investigations and is therefore widely deployable with minimal infrastructural requirements.')


from streamlit_extras.switch_page_button import switch_page

want_to_predict = st.button("I want to check my risk of diabetes!")
if want_to_predict:
    switch_page("ml_page")

    

