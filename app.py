import streamlit as st
import analys
import prediction

navigasi = st.sidebar.selectbox('Pilih Halaman :', 
                                ('Model Prediction', 'Plant Growth Data Analysis'))

if navigasi == 'Model Prediction':
    prediction.main()
else :
    analys.main()
