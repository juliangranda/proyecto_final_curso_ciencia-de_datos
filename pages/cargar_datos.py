import pandas as pd
import streamlit as st
def dataset():
    url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
    df = pd.read_csv(url)

    #Tratamiento de datos
    df.columns = df.columns.str.lower()
    df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)
    df.fillna({"sleep disorder":"unknown"}, inplace=True)
    return df
