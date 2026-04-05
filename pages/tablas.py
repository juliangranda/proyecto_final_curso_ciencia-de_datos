import streamlit as st
import pandas as pd
st.title(":material/table_chart: database", text_alignment= "center")

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
    st.subheader("🔥 Nivel de Estrés", text_alignment="center")
    # Simplificamos el cálculo
    df_estres = df.groupby('occupation')['stress level'].mean().sort_values(ascending=False).reset_index()
    # Usamos st.dataframe con un ajuste de ancho automático
    st.dataframe(df_estres.rename(columns={'stress level': 'Estrés Promedio'}), hide_index=True, width = "stretch")

with col2:
    st.subheader("😴 Duración de Sueño", text_alignment= 'center')
    df_sueno = df.groupby('occupation')['sleep duration'].mean().sort_values(ascending=False).reset_index()
    st.dataframe(df_sueno.rename(columns={'sleep duration': 'Horas Promedio'}), hide_index=True, width = "stretch")

st.divider()

# --- SECCIÓN 2: ACTIVIDAD FÍSICA DETALLADA ---
st.subheader("🏃‍♂️ Actividad Física "  , text_alignment="center")

df_exercise = df.groupby('occupation').agg({
    'physical activity level': ['min', 'max', 'mean'],
    'stress level': 'mean'
}).round(2).reset_index()

# Ordenamos por estrés para ver quiénes están "peor"
df_exercise.columns = [
    'Ocupación', 
    'Act.Mín', 'Act.Máx', 'Act.Prom',
    'Estres.Prom'
]
df_exercise = df_exercise.sort_values('Estres.Prom', ascending=False)
st.dataframe(df_exercise, hide_index=True, width = "stretch")

# Tip Junior: Un pequeño mensaje que conecte los datos
st.info("**Nota:** Compara cómo las profesiones con más estrés (arriba a la izquierda) suelen coincidir con menos horas de actividad física.")

