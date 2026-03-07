import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("KPIs", text_alignment= "center")

#----------------------------Lectura del dataset--------------------
def cargar_datos():
    url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
    df = pd.read_csv(url)

    #Tratamiento de datos
    df.columns = df.columns.str.lower()
    df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)
    df.fillna({"sleep disorder":"unknown"}, inplace=True)
    return df

df = cargar_datos()

# Espaciado
st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)

#----------------------------Mapa de Calor--------------------
st.subheader("Mapa de calor de correlación entre variables", text_alignment= "center")

#Solo utilizamos las columnas numéricas para el análisis de correlación evitando generar errores con columnas tipo string.
numeric_df = df.select_dtypes(include=["number"])
if not numeric_df.empty:
    corr = numeric_df.corr()
    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="YlGnBu",
        labels={"x": "Variables", "y": "Variables", "color": "Correlación"},
        zmin=-1,
        zmax=1,
    )
    fig.update_layout(margin=dict(l=40, r=40, t=40, b=40))
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("No hay columnas numéricas para mostrar el mapa de calor.")


#----------------------------pie de roles ocupacionales--------------------
st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)
st.subheader("Distribución de roles ocupacionales", text_alignment= "center")
fig = px.pie(df, names="occupation")
st.plotly_chart(fig)

#----------------------------pie de edad-------------------
st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)
st.subheader("Distribución de edades", text_alignment= "center")
fig = px.pie(df, names="age")
st.plotly_chart(fig)

#----------------------------pie de Genero--------------------
st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)
st.subheader("Distribución de género", text_alignment= "center")
fig = px.pie(df, names="gender")
st.plotly_chart(fig)