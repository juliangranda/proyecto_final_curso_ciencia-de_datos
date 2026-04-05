import streamlit as st
import pandas as pd
st.title("🛌Análisis del Sueño", text_alignment= "center")
st.header("Bienvenido al análisis de datos sobre calidad del sueño y estilo de vida.")

def espacio():
    st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)
def cargar_datos():
    url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
    df = pd.read_csv(url)

    #Tratamiento de datos
    df.columns = df.columns.str.lower()
    df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)
    df.fillna({"sleep disorder":"unknown"}, inplace=True)
    return df

df = cargar_datos()
with st.expander("Exploración Inicial del DataSet", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Filas", df.shape[0], help="Número total de registros")
    with col2:
        st.metric("Características", df.shape[1], help="Número de variables analizadas")
    with col3:
        st.metric("Ocupaciones", len(df['occupation'].unique()), help="Diversidad de empleos")

st.markdown("---")
#----------------------------Descripción del DataSet--------------------
with st.expander("Descripción del DataSet", expanded=True):
    st.write("El DataSet analiza la calidad del sueño y el estilo de vida. Las variables incluidas son:")
    st.info(f"**Columnas:** {', '.join(df.columns)}")

st.markdown("---")
# --- Visualización Dinámica del DataFrame ---
with st.expander("Ver datos crudos del DataSet", expanded=True):
    st.subheader("📋 Descripción de Variables")
    st.write("El DataSet analiza la **calidad del sueño** y el **estilo de vida**. Las variables incluidas son:")
    filas = st.slider("Ajusta cuántas filas quieres explorar:", 5, df.shape[0], 10)
    st.write(f"Mostrando las primeras **{filas}** entradas:")
    # st.dataframe es más interactivo que st.write
    st.dataframe(df.head(filas), width="stretch")

st.markdown("---")
#----------------------------Ocupaciones Laborales--------------------
with st.expander("Profesiones Representadas", expanded=True):
    st.write("El DataSet incluye una variedad de profesiones, lo que permite analizar cómo el estrés y la calidad del sueño varían según el tipo de trabajo.")
    st.success(f"**Ocupaciones únicas encontradas:** \n\n {', '.join(df['occupation'].unique())}")

st.markdown("---")
#----------------------------Objetivos--------------------
with st.expander("Objetivos del Análisis", expanded=True):
    st.markdown("""
    **Objetivo General:** Analizar la relación multidimensional entre hábitos de vida (actividad física, ocupación, IMC) y la calidad del sueño.

    * **Objetivo 1:** Identificar profesiones con niveles críticos de estrés y su impacto en el sueño.
    * **Objetivo 2:** Validar si superar los 7,000 pasos diarios mejora el descanso subjetivo.
    * **Objetivo 3:** Cruzar el IMC con la calidad de sueño para detectar perfiles de riesgo.
    """)



