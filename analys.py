import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
import pandas as pd 
import streamlit as st

def babi():
    df = pd.read_csv('plant_growth_data.csv')
    Water_Frequency_counts = df['Water_Frequency'].value_counts()

    fig, ax = plt.subplots(figsize=(8, 8))

    Water_Frequency_counts.plot.pie(
        ax=ax,
        autopct='%1.0f%%',  # For percentage
        startangle=90,      # For better view
        colors=plt.get_cmap('Pastel1').colors  # For Colors
    )


    ax.set_title('Distribution of Water Frequency')


    ax.axis('equal')

    st.pyplot(fig, ax)


def burung():
    df = pd.read_csv('plant_growth_data.csv')
    # Getting the counts of each different Fertilizer types
    Fertilizer_Type_counts = df['Fertilizer_Type'].value_counts()

    fig, ax = plt.subplots(figsize=(8, 8))

    Fertilizer_Type_counts.plot.pie(
        ax=ax,
        autopct='%1.0f%%',  # For percentage
        startangle=90,      # For better view
        colors=plt.get_cmap('Set3').colors  # For Colors
    )


    ax.set_title('Distribution of Fertilizer Types')


    ax.axis('equal')

    # Show the plot
    st.pyplot(fig, ax)
def ayam():
    df = pd.read_csv('plant_growth_data.csv')
    soil_type_counts = df['Soil_Type'].value_counts()

    fig, ax = plt.subplots(figsize=(8, 8))
    soil_type_counts.plot.pie(
        ax=ax,
        autopct='%1.0f%%',  # For percentage
        startangle=90,      # For better view
        colors=plt.get_cmap('Dark2').colors  # For Colors
    )
    ax.set_title('Distribution of Soil Types')
    ax.axis('equal')
    st.pyplot(fig, ax)

def main():
    df = pd.read_csv('plant_growth_data.csv')
    st.write('# RawData')
    st.dataframe(df)

    st.write('# Data Distribution')

    opsi = st.selectbox('Choose columm : ', ('Sunlight_Hours', 'Temperature', 'Humidity','Soil_Type','Water_Frequency','Fertilizer_Type'))

    if opsi == 'Soil_Type':
        ayam()
    elif opsi == 'Water_Frequency':
        babi()
    elif opsi == 'Fertilizer_Type':
        burung()
    else:
        fig = plt.figure(figsize=(15,10))
        sns.histplot(df[opsi], bins=20, kde=True)
        st.pyplot(fig)
    st.write('# Pairplots sample')
    a = sns.pairplot(df, vars=['Sunlight_Hours', 'Temperature', 'Humidity'])
    st.pyplot(a)

if __name__ == "__main__":
    main()