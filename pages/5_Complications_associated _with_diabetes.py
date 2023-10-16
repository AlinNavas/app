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
    st.markdown("<h1 style='text-align: center; color: SkyBlue;'>The complications associated with chronic uncontrolled diabetes</h1>", unsafe_allow_html=True)
    st.markdown('  ')
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
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('  ')

col1, col2, col3 = st.columns(3)

with col2:
    want_to_predict = st.button("Now I'd like to know my risk of being diabetic!")

if want_to_predict:
    switch_page("Predict_risk_of_Diabetes")