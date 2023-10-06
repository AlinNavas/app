import streamlit as st
import streamlit.components.v1 as components
p = open("trial.htm",'r',encoding="windows-1252 ")
st.components.v1.html(p.read(), width=1600, height=800, scrolling=True)
#components.html(p.read())

