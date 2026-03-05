import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

## Configuración de la página
st.set_page_config(page_title="Sleep Health", page_icon=":video_game:", layout="wide")
@st.cache_data

##---------------------------Lectura del dataset--------------------
def cargar_datos():
    url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
    df = pd.read_csv(url)

    #Tratamiento de datos
    df.columns = df.columns.str.lower()
    df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)
    df.fillna({"sleep disorder":"unknown"}, inplace=True)
    return df

df = cargar_datos()

##---------------------------Cuerpo del Proyecto--------------------


##---------------------------Navegación entre páginas--------------------


pg = st.navigation([
    st.Page("pages/home.py", title="Home", icon=":material/home:"),
    st.Page("pages/filtros.py", title="Filtros", icon=":material/filter_list:"),
    st.Page("pages/kpis.py", title="KPIs", icon=":material/insights:"),
    st.Page("pages/tablas.py", title="Tablas", icon=":material/table_chart:"),
    st.Page("pages/graficos.py", title="Gráficos", icon=":material/insert_chart:"),
])

pg.run()

