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

    st.sidebar.header("Diabetes Predictor")
    st.sidebar.markdown("I developed a screening tool while I was in medical school that can predict the presence of diabetes based on symptoms exhibited when a patient is in a hyperglycaemic state using Support Vector Machine ML method.")   
    st.sidebar.markdown("Developed by: Dr. Alin Navas")                   



body = st.container()



with body:
    st.markdown("<h1 style='text-align: center; color: SkyBlue;'>Predict your risk of having diabetes!</h1>", unsafe_allow_html=True)
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('Studies have shown that a significant number of people who are diabetic are unaware of their condition. Even developed countries with high per capita expenditure on healthcare, like the US, have around 8.5 million adults with undiagnosed diabetes. This represents nearly 23 percent of all US adults with diabetes. ')
    st.markdown('On a global scale, some papers claim that 1 in 2 people living with diabetes don’t know that they have it.  ')
    st.markdown('This lack of awareness can be very dangerous. Uncontrolled diabetes mellitus may lead to many serious complications like the ones shown below:')
    st.markdown('  ')
    st.markdown('1)	Diabetic retinopathy : The development and progression of DR is primarily caused by the tissue-damaging effects of chronic hyperglycaemia that results in a complex interplay of multiple mechanisms ,which cause two basic changes within the retinal vessels, namely: abnormal permeability, and occlusion with ischemia and subsequent neovascularization.  ')
    image = Image.open('trial_files/image001.jpg')
    col1, col2, col3 = st.columns(3)
    col2.image(image, caption='Fundus of a patient with severe diabetic retinopathy')
    st.markdown('2)	Diabetic nephropathy : Hyperglycaemia results in production of advanced glycation end-products (AGE) and reactive oxygen species. These aberrant metabolic products activate intercellular signaling for proinflammatory and profibrotic gene expression with production of a host of mediators for cellular injury. ')
    image2 = Image.open('trial_files/image002.jpg')
    col1, col2, col3 = st.columns(3)
    col2.image(image2, caption='Immunofluorescence staining with IgG in a patient with diabetic nephropathy ')
    st.markdown('3)	Diabetic neuropathy : In diabetes, a complex array of metabolic and vascular factors shift the balance between nerve fiber damage and nerve fiber repair in favor of damage [2]. This occurs in a fiber-selective pattern that preferentially affects the more vulnerable distal sensory and autonomic fibers, leading to the progressive loss of sensation that underlies the clinical manifestations of diabetic polyneuropathy.  ')
    image3 = Image.open('trial_files/image003.jpg')
    col1, col2, col3 = st.columns(3)
    col2.image(image3, caption='Loss of pain and other sensations in foot')
    st.markdown(' 4)Diabetic foot Ulcers : Chronic ulceration in patients with diabetes is multifactorial, due to a combination of diabetic neuropathy, autonomic dysfunction, and vascular insufficiency. Nonischemic diabetic foot ulcers are due to a combination of foot deformities and neuropathy preventing the sensation of pain in areas of the foot that are traumatized. ')
    image4 = Image.open('trial_files/image004.jpg')
    col1, col2, col3 = st.columns(3)
    col2.image(image4, caption='Representation of ulcer in base of foot')
    st.markdown('5)	Macrovascular complications: Increases the risk of macrovascular complications like stroke, coronary artery disease, peripheral vascular disease. Chronic Hyperglycemia causes increased oxidative stress, protein kinase activation, and activation of the receptor for advanced glycation end products, factors that act on the endothelium of blood vessels.  ')
    image5 = Image.open('trial_files/image005.jpg')
    image6 = Image.open('trial_files/image006.jpg')
    image7 = Image.open('trial_files/image007.jpg')
    col1, col2, col3 = st.columns(3)
    col1.image(image6, caption='Stroke')
    col2.image(image5, caption='Coronary Artery Disease')
    col3.image(image7, caption='Peripheral Vascular Disease')


    st.markdown('This approach does not require any blood investigations and is therefore widely deployable with minimal infrastructural requirements.')


from streamlit_extras.switch_page_button import switch_page


st.markdown(' ')
st.markdown(' ')
st.markdown(' ')

col1, col2, col3 = st.columns(3)

with col2:
    want_to_predict = st.button("I want to check my risk of being diabetic!")

if want_to_predict:
    switch_page("ml_page")

st.markdown(' ')
st.markdown(' ')


col1, col2 = st.columns(2)

with col1:
    want_know_global = st.button("I want to know more about the global scale of this problem")

if want_know_global:
    switch_page("global_pop")

with col2:
    prev_diab = st.button("I would like to learn more about how to prevent diabetes.")

if prev_diab:
    switch_page("prevent_diab")
