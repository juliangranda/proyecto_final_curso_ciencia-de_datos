import streamlit as st
import plotly.express as px
import pages.cargar_datos as datos

st.title("📊 Análisis Gráficos", text_alignment= "center")
df = datos.dataset()

if "df_filtrado" in st.session_state:
    df = st.session_state["df_filtrado"]
    # --- SECCIÓN 1: IMPACTO LABORAL ---
    with st.container():
        st.header("🏢 Estres Laboral por Profesión")
        
        tab1, tab2 = st.tabs(["Nivel de Estrés vs Occupacion","Calidad de Sueño vs Nivel de Estrés"])
        
        with tab1:
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
            st.plotly_chart(fig_prof, width = "stretch")

        with tab2:
            fig_scatter2 = px.scatter(
                df, x="sleep duration", y="stress level",
                color="quality of sleep", size="quality of sleep",
                title="El balance entre Horas de Sueño y Estrés",
                color_continuous_scale="RdYlGn"
            )
            st.plotly_chart(fig_scatter2, width = "stretch")
    st.divider()

    # --- SECCIÓN 2: ACTIVIDAD FÍSICA ---
    with st.container():
        st.header("🏃‍♂️ El Factor del Movimiento")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Pasos Diarios vs. Actividad Física ",text_alignment="center")
            # Gráfica simple de Streamlit
            st.scatter_chart(
                df.sort_values("daily steps"), 
                x="daily steps", 
                y="physical activity level", 
                color="quality of sleep" 
            )
        
        with col2:
            st.subheader("Calidad de Sueño por Número de Personas ",text_alignment="center")
            # Filtrado para >7000 pasos
            active = df[df["daily steps"] > 7000]
            sleep_counts = active["quality of sleep"].value_counts().sort_index().reset_index()
            sleep_counts.columns = ["Calidad de Sueño", "Personas"]
            
            st.bar_chart(sleep_counts, x="Calidad de Sueño", y="Personas", color="#2E86C1")
        
    st.divider()

    with st.container():
        df_f = st.session_state["df_filtrado"]

        st.subheader("🏃‍♂️ Relación: Pasos Diarios vs. Calidad de Sueño", text_alignment="center")

        fig_pasos = px.scatter(
            df_f, 
            x='daily steps',            
            y='quality of sleep',       
            color='occupation',         
            size='physical activity level', 
            title="Impacto de la actividad física en la calidad del sueño",
            labels={
                "daily steps": "Pasos diarios", 
                "quality of sleep": "Calidad de Sueño (1-10)",
                "occupation": "Ocupación"
            },
            template="plotly_white"
        )

        st.plotly_chart(fig_pasos, width = "stretch")
