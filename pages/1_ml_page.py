import streamlit as st
import pandas as pd
import pickle
import numpy as np
import sklearn

header = st.container()
model_training = st.container()



with header:
    st.title('Predict the risk of having diabetes based on your symptoms')
    st.markdown('Note: This algorithm is more specifically meant to screen untested individuals to check for the presence of diabtes based on ')




with model_training:
    st.header('Time to train the model')

    
    Age = st.text_input("Enter your Age ","Type Here")
    Polyuria = st.selectbox('Polyuria',['Yes','No'])
    Polydipsia= st.selectbox('Polydipsia',['Yes','No'])
    sudden_weight_loss = st.selectbox('sudden_weight_loss',['Yes','No'])
    weakness= st.selectbox('weakness',['Yes','No'])
    Polyphagia= st.selectbox('Polyphagia',['Yes','No'])
    Genital_thrush= st.selectbox('Genital_thrush',['Yes','No'])
    visual_blurring= st.selectbox('visual_blurring',['Yes','No'])
    Irritability= st.selectbox('Irritability',['Yes','No'])
    partial_paresis= st.selectbox('partial_paresis',['Yes','No'])
    muscle_stiffness= st.selectbox('muscle_stiffness',['Yes','No'])
    Obesity= st.selectbox('Obesity',['Yes','No'])

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

modelsvc = pickle.load(open('demo_svc_model.pkl','rb'))
modellr = pickle.load(open('demo_lr_model.pkl','rb'))

def pred_diab( Age,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,Irritability,partial_paresis,muscle_stiffness,Obesity):
    input=np.array([[Age,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,Irritability,partial_paresis,muscle_stiffness,Obesity]]).astype(np.float64)
    prediction1 =modelsvc.predict(input)
    prediction2 =modellr.predict_proba(input)
    return (prediction1,prediction2)

if st.button("Predict diabetes"):
        output1,output2 = pred_diab(Age,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,Irritability,partial_paresis,muscle_stiffness,Obesity)
        if output1 == 1:
             outputp = "Diabetic"
        else:
             outputp = "Non-Diabetic"
        st.success('You are likely {}'.format(outputp))
        st.success('You are likely {}'.format(output2[::,1]))


