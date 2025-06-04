import streamlit as st
import pickle
file=open(r"C:\Users\Meera\Downloads\p3.pkl",'rb')
regressor=pickle.load(file)
file.close()
a=st.number_input("Enter the SO2 level")
b=st.number_input("Enter the CO level")
c=st.number_input("Enter the NO level")
d=st.number_input("Enter the NO2 level")
e=st.number_input("Enter the NOX level")
f=st.number_input("Enter the NH3 level")
g=st.number_input("Enter the O3 level")
if st.button('predict'):
    result=regressor.predict([[a,b,c,d,e,f,g]])[0]
    st.write(result)
    if result is not None and result>=50:
       label="good"
       color="orange"
    elif result is not None and result<=50:
       label="moderate"
       color="green"
    else:
       label="poor"
       color="red"