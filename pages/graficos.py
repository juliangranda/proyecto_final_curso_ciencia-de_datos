import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Gráficos")

def cargar_datos():
    url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
    df = pd.read_csv(url)

    #Tratamiento de datos
    df.columns = df.columns.str.lower()
    df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)
    df.fillna({"sleep disorder":"unknown"}, inplace=True)
    return df

source = cargar_datos()

#revisar por que esta raro
st.bar_chart(source, x="occupation", y="stress level", color= "blue", stack=False)


source = source[["occupation", "stress level"]].groupby("occupation").mean().reset_index()
st.bar_chart(source, x="occupation", y="stress level", color= "blue", stack=False)


