import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Prediction of COVID-19')

with st.expander('Data'):
  df = pd.read_csv('alzheimers_disease_patient_data.csv')  
