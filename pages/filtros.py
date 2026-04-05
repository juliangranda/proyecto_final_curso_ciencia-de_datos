import streamlit as st
import pandas as pd
import plotly.express as px
import pages.cargar_datos as datos

df_filtrado = datos.dataset()

st.title("Filtros", text_alignment= "center")
if "df_filtrado" in st.session_state:
    df_filtrado = st.session_state["df_filtrado"]
    st.subheader("📈 Sueño y Estrés según la Edad", text_alignment= "center")
    # Agrupamos por edad y sacamos promedios
    df_edad = df_filtrado.groupby('age')[['sleep duration', 'stress level', 'quality of sleep']].mean().reset_index()

    fig_edad = px.line(
        df_edad,
        x='age',
        y=['sleep duration', 'stress level', 'quality of sleep'],
        title="Tendencia: Edad vs. Indicadores de Salud",
        labels={
            'value': 'stress level/ sleep duration',
            'age': 'Edad',
            'variable': 'Métrica'}
    )
    #Centrar el título del gráfico
    fig_edad.update_layout(
        title_x=0.5,
        title_xanchor='center'
    )
    st.plotly_chart(fig_edad, width = "stretch")

    st.subheader("🏢 Comparativa por Profesión", text_alignment= "center")
    df_occ = df_filtrado.groupby('occupation')[['quality of sleep', 'stress level']].mean().reset_index()

    fig_occ = px.bar(
        df_occ, x='occupation', y=['quality of sleep', 'stress level'],
        barmode='group',
        title="Calidad de Sueño y Estrés por Ocupación",
        color_discrete_sequence=['#636EFA', '#EF553B'] # Azul para sueño, Rojo para estrés
    )
    #Centrar el título del gráfico
    fig_occ.update_layout(
        title_x=0.5,
        title_xanchor='center'
    )
    st.plotly_chart(fig_occ, width = "stretch")

    st.subheader("🚻 Diferencias por Género", text_alignment="center")
    col1, col2 = st.columns(2)

    with col1:
        fig_gen1 = px.box(df_filtrado,
                          x='gender', 
                          y='sleep duration', 
                          color='gender', 
                          title="Duración de Sueño")
        fig_gen1.update_layout(
                title_x=0.5,
                title_xanchor='center'
            )                  
        st.plotly_chart(fig_gen1, width = "stretch")

    with col2:
        fig_gen2 = px.box(df_filtrado,
                          x='gender', 
                          y='stress level', 
                          color='gender', 
                          title="Nivel de Estrés")
        fig_gen2.update_layout(
                title_x=0.5,
                title_xanchor='center'
            )  
        st.plotly_chart(fig_gen2, width = "stretch")