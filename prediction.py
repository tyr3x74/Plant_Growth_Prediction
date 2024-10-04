import streamlit as st
import pickle
import pandas as pd

with open('model.pkl', 'rb') as result:
    model = pickle.load(result)


def main():
    st.title("Model Prediction")
    st.image('https://asset-a.grid.id/crop/0x0:0x0/x/photo/2019/03/18/4024791148.jpg')
    with st.form(key='form parameters'):
        a = st.selectbox('Soil Type :', ('loam', 'clay', 'sandy'))
        if a == "loam":
            a = 0
        elif a == "clay":
            a = 1
        elif a == "sandy":
            a = 2
        b = st.number_input('Sunlight', min_value=0)
        e = st.selectbox('Water Frequency :', ('daily', 'weekly', 'bi-weekly'))
        if e == "daily":
            e = 0
        elif e == "weekly":
            e = 1
        elif e == "bi-weekly":
            e = 2
        f = st.selectbox('FertilizerType	 :', ('none','organic','chemical'))
        if f == "none":
            f = 0
        elif f == "organic":
            f = 1
        elif f == "chemical":
            f = 2
        c = st.number_input('Temperature', min_value=0)
        d = st.number_input('Humidity', min_value=0)
    
        submit = st.form_submit_button('Predict')

    data_baru = {
    'Soil_Type' : a,
    'Sunlight_Hours': b,
    'Water_Frequency' :  e,
    'Fertilizer_Type' : f,
    'Temperature': c,
    'Humidity': d
    }

    data_inf = pd.DataFrame([data_baru])
    st.dataframe(data_inf)

    if submit:
        score = model.predict(data_inf)
        if score == 1:
            st.write('# Status : Grown')
        else: 
            st.write('# Status : Not Grown')

if __name__ == '__main__' :
    main()