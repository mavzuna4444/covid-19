import streamlit as st

st.title('Prediction of COVID-19')

with st.expander('Data'):
  df = pd.read_csv('alzheimers_disease_patient_data.csv')  
