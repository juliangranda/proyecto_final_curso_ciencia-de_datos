import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


st.title("Gráficos", text_alignment= "center")

def cargar_datos():
    url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
    df = pd.read_csv(url)

    #Tratamiento de datos
    #df.columns = df.columns.str.strip().str.lower()
    df.columns = df.columns.str.lower()
    df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)
    df.fillna({"sleep disorder":"unknown"}, inplace=True)
    return df

df = cargar_datos()

st.title("📊 Análisis de Gráficos")
st.write("Explora las relaciones entre el estilo de vida y la salud del sueño a través de datos.")

if "df_filtrado" in st.session_state:
    df = st.session_state["df_filtrado"]
    # --- SECCIÓN 1: IMPACTO LABORAL ---
    with st.container():
        st.header("🏢 Salud Laboral por Profesión")
        
        # Agrupamos y sacamos el promedio
        df_resumen = df.groupby('occupation')[['stress level', 'quality of sleep']].mean().reset_index()
        
        fig_prof = px.bar(
            df_resumen, 
            x='occupation', 
            y=['stress level', 'quality of sleep'],
            barmode='group',
            title="Estrés vs. Calidad de Sueño",
            labels={'value': 'Puntaje', 'occupation': 'Profesión', 'variable': 'Indicador'},
            color_discrete_map={'stress level': '#ef553b', 'quality of sleep': '#636efa'}
        )
        st.plotly_chart(fig_prof, use_container_width=True)

    st.divider()

    # --- SECCIÓN 2: ACTIVIDAD FÍSICA ---
    with st.container():
        st.header("🏃‍♂️ El Factor del Movimiento")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Pasos vs. Actividad")
            # Gráfica simple de Streamlit
            st.scatter_chart(
                df.sort_values("daily steps"), 
                x="daily steps", 
                y="physical activity level", 
                color="quality of sleep" 
            )
        
        with col2:
            st.subheader("Calidad en Usuarios Activos")
            # Filtrado para >7000 pasos
            active = df[df["daily steps"] > 7000]
            sleep_counts = active["quality of sleep"].value_counts().sort_index().reset_index()
            sleep_counts.columns = ["Calidad de Sueño", "Personas"]
            
            st.bar_chart(sleep_counts, x="Calidad de Sueño", y="Personas", color="#2E86C1")
        
    st.divider()

    # --- SECCIÓN 3: RELACIONES MULTIDIMENSIONALES ---
    with st.container():
        st.header("🔍 Relaciones Profundas")
        
        tab1, tab2 = st.tabs(["Pasos y Calidad", "Sueño vs. Estrés"])
        
        with tab1:
            fig_scatter1 = px.scatter(
                df, x="daily steps", y="quality of sleep",
                color="stress level", size="sleep duration",
                title="Relación Pasos, Calidad y Duración",
                color_continuous_scale="Viridis"
            )
            st.plotly_chart(fig_scatter1, use_container_width=True)
            
        with tab2:
            fig_scatter2 = px.scatter(
                df, x="sleep duration", y="stress level",
                color="quality of sleep", size="quality of sleep",
                title="El balance entre Horas de Sueño y Estrés",
                color_continuous_scale="RdYlGn"
            )
            st.plotly_chart(fig_scatter2, use_container_width=True)