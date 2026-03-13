import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def cargar_datos():
    url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
    df = pd.read_csv(url)

    #Tratamiento de datos
    df.columns = df.columns.str.lower()
    df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)
    df.fillna({"sleep disorder":"unknown"}, inplace=True)
    return df

df_filtrado = cargar_datos()
st.title("Filtros", text_alignment= "center")
if "df_filtrado" in st.session_state:
    df_filtrado = st.session_state["df_filtrado"]
    st.subheader("📈 Evolución de la Salud según la Edad")
    # Agrupamos por edad y sacamos promedios
    df_edad = df_filtrado.groupby('age')[['sleep duration', 'stress level', 'quality of sleep']].mean().reset_index()

    fig_edad = px.line(
        df_edad, x='age', y=['sleep duration', 'stress level', 'quality of sleep'],
        title="Tendencia: Edad vs. Indicadores de Salud",
        labels={'value': 'Puntaje / Horas', 'age': 'Edad', 'variable': 'Métrica'}
    )
    st.plotly_chart(fig_edad, use_container_width=True)

    st.subheader("🏢 Comparativa por Profesión")
    df_occ = df_filtrado.groupby('occupation')[['quality of sleep', 'stress level']].mean().reset_index()

    fig_occ = px.bar(
        df_occ, x='occupation', y=['quality of sleep', 'stress level'],
        barmode='group',
        title="Calidad de Sueño y Estrés por Ocupación",
        color_discrete_sequence=['#636EFA', '#EF553B'] # Azul para sueño, Rojo para estrés
    )
    st.plotly_chart(fig_occ, use_container_width=True)

    st.subheader("🚻 Diferencias por Género")
    col1, col2 = st.columns(2)

    with col1:
        fig_gen1 = px.box(df_filtrado, x='gender', y='sleep duration', color='gender', title="Duración de Sueño")
        st.plotly_chart(fig_gen1, use_container_width=True)

    with col2:
        fig_gen2 = px.box(df_filtrado, x='gender', y='stress level', color='gender', title="Nivel de Estrés")
        st.plotly_chart(fig_gen2, use_container_width=True)