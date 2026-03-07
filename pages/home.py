import streamlit as st
import pandas as pd
st.title("Análisis del Sueño")
st.subheader("Bienvenido al análisis de datos sobre calidad del sueño y estilo de vida.")


def cargar_datos():
    url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
    df = pd.read_csv(url)

    #Tratamiento de datos
    df.columns = df.columns.str.lower()
    df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)
    df.fillna({"sleep disorder":"unknown"}, inplace=True)
    return df

df = cargar_datos()

st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)
#374 filas tiene el data set y 13 columnas
st.write("El dataset contiene {} filas y {} columnas.".format(df.shape[0], df.shape[1]))
filas = st.slider("Selecciona el número de filas a mostrar:", 0, 374, 187)
st.write(df.head(filas))
