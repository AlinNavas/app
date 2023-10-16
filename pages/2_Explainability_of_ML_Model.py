import streamlit as st
import base64
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit_extras
st.set_option('deprecation.showPyplotGlobalUse', False)
from streamlit_extras.switch_page_button import switch_page

body = st.container()



with body:
    st.markdown("<h1 style='text-align: center; color: SkyBlue;'>Learn more about how the app makes a prediction!</h1>", unsafe_allow_html=True)
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')
    st.markdown(' SVMs are mainly used for classification and are based on the idea of finding a hyperplane that best divides a dataset into two classes, as shown in the image below.')
with open("trial_files/svm_base.png", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(
        f"""
        <div style="display:table;margin-bottom:0%;margin-left:0%;">
            <img src="data:image/png;base64,{data}" width="600" height="300">
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(' If the model is unable to find a clear hyperplane like in the example above, it increases the dimensionality of data via kernelling to create a suitable hyperplane. ')

with open("trial_files/svm2.png", "rb") as f:
    data = base64.b64encode(f.read()).decode("utf-8")

    st.markdown(
        f"""
        <div style="display:table;margin-bottom:0%;margin-left:0%;">
            <img src="data:image/png;base64,{data}" width="600" height="300">
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(' The SVM model was chosen after comparing multiple machine learning models including Decision Trees, Logistic Regression, K Nearest Neighbors and comparing their classification metrics.')

st.markdown(' ')
st.markdown(' ')

col1, col2, col3 = st.columns(3)

with col2:
    want_to_predict = st.button("I want to go back to the Home Page!")

if want_to_predict:
    switch_page("Home_Page")

