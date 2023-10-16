import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn
from streamlit_extras.switch_page_button import switch_page

header = st.container()
model_training = st.container()



with header:
    st.markdown("<h1 style='text-align: center; color: SkyBlue;'>Predict the risk of having diabetes based on your symptoms</h1>", unsafe_allow_html=True)
    st.markdown('  ')
    st.markdown('  ')
    st.markdown('Note: This algorithm is specifically meant to screen untested individuals (i.e individuals who have not done RBS, HbA1c blood tests) to check for the presence of diabetes based on symptoms associated with chronic hyperglycemia ( seen in undiagnosed, untreated diabetic individuals).')




with model_training:
    st.markdown("<h4 style='text-align: center; color: black;'>Please answer the following questions:</h4>", unsafe_allow_html=True)

    
    Age = st.text_input("Enter your Age ","Type Here")
    Polyuria = st.selectbox('Have you experienced an increase in the frequency and duration of voiding of urine? ( greater than 7 times per day)',['Yes','No'])
    Polydipsia= st.selectbox('Have you experienced persistent and unexplained thirst, regardless of how much water/ fluids you drink?',['Yes','No'])
    sudden_weight_loss = st.selectbox('Have you undergone a 3-5 kg weight loss within 6 months, without changing your diet or exercise routine? ',['Yes','No'])
    weakness= st.selectbox('Are you suffering from chronic fatigue (decreased level of physical endurance, low levels of energy or tiredness for long durations)',['Yes','No'])
    Polyphagia= st.selectbox('Do you experience constantly extreme, insatiable hunger? ',['Yes','No'])
    Genital_thrush= st.selectbox('Do you experience recurrent episodes of itching and irritation in the genital region?',['Yes','No'])
    visual_blurring= st.selectbox('Have you noticed your vision being either always blurry, sometimes burry, or occasionally blurry (out of focus) ?',['Yes','No'])
    Irritability= st.selectbox('Do you experience constant mood swings, bouts of irritability , confusion or aggressiveness?',['Yes','No'])
    partial_paresis= st.selectbox('Do you have recurrent episodes of nausea,bloating,vomiting, abdominal discomfort ?',['Yes','No'])
    muscle_stiffness= st.selectbox('Have you experienced persistent muscle cramps or stiffness of muscles?',['Yes','No'])
    Obesity= st.selectbox('Is your body mass index(BMI) greater than 30? (Google "BMI calculator" and enter weight and height)',['Yes','No'])

Polyuria = 1 if Polyuria == "Yes" else 0
Polydipsia = 1 if Polydipsia == "Yes" else 0
sudden_weight_loss = 1 if sudden_weight_loss == "Yes" else 0
weakness = 1 if weakness == "Yes" else 0
Polyphagia = 1 if Polyphagia == "Yes" else 0
Genital_thrush = 1 if Genital_thrush == "Yes" else 0
visual_blurring = 1 if visual_blurring == "Yes" else 0
Irritability = 1 if Irritability == "Yes" else 0
partial_paresis = 1 if Irritability == "Yes" else 0
muscle_stiffness = 1 if Irritability == "Yes" else 0
Obesity = 1 if Irritability == "Yes" else 0

modelsvm = pickle.load(open('demo_svm_model.pkl','rb'))
modellr = pickle.load(open('demo_lr_model.pkl','rb'))

def pred_diab( Age,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,Irritability,partial_paresis,muscle_stiffness,Obesity):
    input=np.array([[Age,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,Irritability,partial_paresis,muscle_stiffness,Obesity]]).astype(np.float64)
    prediction1 =modelsvm.predict(input)
    prediction2 =modellr.predict_proba(input)
    return (prediction1,prediction2)

st.markdown('  ')
st.markdown('  ')
col1, col2, col3 = st.columns(3)

with col2:
    if st.button("Predict diabetes"):
        output1,output2 = pred_diab(Age,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,Irritability,partial_paresis,muscle_stiffness,Obesity)
        if output1 == 1:
             outputp = "Diabetic"
        else:
             outputp = "Non-Diabetic"
        
        
        st.success('You are likely {}'.format(outputp))
        st.success('Your probability of being diabetic is {} (MAX value is 1)'.format(output2[::,1]))


col1, col2 = st.columns(2)
with col2:
    prev_diab = st.button("I would like to learn more about how to prevent diabetes.")

if prev_diab:
    switch_page("Prevent_Diabetes")