import streamlit as st
import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.title("🎯 KPIs", text_alignment= "center")

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


if "df_filtrado" in st.session_state:
    df = st.session_state["df_filtrado"]
    # --- Sección 1: Distribuciones Demográficas (En 3 Columnas) ---
    st.subheader("📊 Perfil de la Muestra", text_alignment="center")
    col1, col2, col3 = st.columns(3)
    col1,col2,col3 = st.tabs(["Ocupación","Edad","Género"])

    with col1:
        st.markdown("**Roles Ocupacionales**")
        fig1 = px.pie(df, names="occupation", hole=0.4, color_discrete_sequence=px.colors.qualitative.Pastel)
        fig1.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0))
        fig1.update_traces(textfont_color="black", textinfo="percent+label")
        st.plotly_chart(fig1, width="stretch")

    with col2:
        st.markdown("**Distribución por Edad**")
        fig2 = px.pie(df, names="age", hole=0.4, color_discrete_sequence=px.colors.qualitative.Safe)
        fig2.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig2, width="stretch")

    with col3:
        st.markdown("**Género**")
        fig3 = px.pie(df, names="gender", hole=0.4, color_discrete_sequence=['#636EFA', '#EF553B'])
        fig3.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        st.plotly_chart(fig3, width="stretch")
    st.divider()

    st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)


    #----------------------------Mapas de Calor--------------------
    # PROMEDIO de Estrés por Ocupación y Categoría de IMC
    st.subheader("📊 Intensidad de Estrés por Profesión e IMC", text_alignment="center")
    heatmap_avg = df.pivot_table(
        index='occupation', 
        columns='indice de masa corporal', 
        values='stress level', 
        aggfunc='mean'
    )

    fig_heat = px.imshow(
        heatmap_avg,
        text_auto=".1f", # Muestra el promedio con un decimal
        color_continuous_scale='Viridis',
        labels=dict(x="Categoría IMC", y="Ocupación", color="Estrés Promedio"),
        
    )
    st.plotly_chart(fig_heat, width="stretch")
    st.markdown("---")
    #---------------------------------------------------------------
    st.markdown("<div style='margin-top: 30px'></div>", unsafe_allow_html=True)
    st.subheader("📊 ¿Qué variables se relacionan entre sí?", text_alignment="center")

    # 1. Seleccionar solo números (esto evita errores con texto)
    df_numerico = df.select_dtypes(include=["number"])

    # 2. Calcular la correlación (es una tablita de números entre -1 y 1)
    matriz_correlacion = df_numerico.corr()

    # 3. Crear el mapa de calor con Plotly Express
    fig_corr = px.imshow(
        matriz_correlacion,
        text_auto=".2f", # Muestra solo 2 decimales
        color_continuous_scale="RdBu_r", # Rojo (negativo), Azul (positivo)
        zmin=-1, zmax=1 # Rango estándar de correlación
    )

    # 4. Mostrar en la pantalla
    st.plotly_chart(fig_corr, width="stretch")