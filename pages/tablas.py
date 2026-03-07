import streamlit as st
import pandas as pd
st.title("Tablas", text_alignment= "center")

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
#------------------------------Nivel de estrés promedio por ocupación--------------------
st.subheader("Nivel de estrés promedio por ocupación", text_alignment= "center")
df_estres = df.groupby('occupation')['stress level'].mean().reset_index()
df_estres = df_estres.sort_values(by='stress level', ascending=False)
datos = {
    "occupation": df_estres['occupation'],
    "stress level": df_estres['stress level'].round(2)
}
st.dataframe(datos)

#------------------------------Nivel de sueño promedio por ocupación--------------------
st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)
st.subheader("Nivel de sueño promedio por ocupación", text_alignment= "center")
df_sueño = df.groupby('occupation')['sleep duration'].mean().reset_index()
df_sueño = df_sueño.sort_values(by='sleep duration', ascending=False)
datos_sueño = {
    "occupation": df_sueño['occupation'],
    "sleep duration": df_sueño['sleep duration'].round(2)
}
st.dataframe(datos_sueño)

#------------------------------Nivel de actividad física promedio por ocupación--------------------
st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)
st.subheader("Nivel de actividad física promedio por ocupación", text_alignment= "center")
df_exercise = df.groupby('occupation')['physical activity level'].agg(["min", "max", "mean"]).round(2).reset_index()
st.dataframe(df_exercise)