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

# --- SECCIÓN 1: ESTRÉS VS SUEÑO (Comparativa) ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🔥 Nivel de Estrés")
    # Simplificamos el cálculo
    df_estres = df.groupby('occupation')['stress level'].mean().sort_values(ascending=False).reset_index()
    # Usamos st.dataframe con un ajuste de ancho automático
    st.dataframe(df_estres.rename(columns={'stress level': 'Estrés Promedio'}), hide_index=True, use_container_width=True)

with col2:
    st.subheader("😴 Duración de Sueño")
    df_sueno = df.groupby('occupation')['sleep duration'].mean().sort_values(ascending=False).reset_index()
    st.dataframe(df_sueno.rename(columns={'sleep duration': 'Horas Promedio'}), hide_index=True, use_container_width=True)

st.divider()

# --- SECCIÓN 2: ACTIVIDAD FÍSICA DETALLADA ---
st.subheader("🏃‍♂️ Actividad Física (Min, Max y Promedio)")

# Tu lógica de agregación es excelente, solo la mostramos más limpia
df_exercise = df.groupby('occupation')['physical activity level'].agg(["min", "max", "mean"]).round(2).reset_index()

# Renombramos las columnas para que el usuario final las entienda mejor
df_exercise.columns = ["Ocupación", "Mínimo", "Máximo", "Promedio"]

st.dataframe(df_exercise, hide_index=True, use_container_width=True)

# Tip Junior: Un pequeño mensaje que conecte los datos
st.info("**Nota:** Compara cómo las profesiones con más estrés (arriba a la izquierda) suelen coincidir con menos horas de sueño.")

