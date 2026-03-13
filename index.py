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
    st.Page("pages/conclusiones.py", title="Conclusiones", icon=":material/emoji_events:"),
])

st.sidebar.header("🔍 Filtros Globales")

# 1. Filtro de Género
generos_sel = st.sidebar.multiselect(
    "Género:", options=df['gender'].unique(), default=list(df['gender'].unique())
)

# 2. Filtro de Ocupación
ocupaciones_sel = st.sidebar.multiselect(
    "Ocupaciones:", options=df['occupation'].unique(), default=list(df['occupation'].unique())
)

# 3. NUEVO: Filtro de Edad (Slider de Rango)
# Calculamos el mínimo y máximo real del dataset para que el slider sea exacto
min_age = int(df['age'].min())
max_age = int(df['age'].max())

rango_edad = st.sidebar.slider(
    "Rango de Edad:",
    min_value=min_age,
    max_value=max_age,
    value=(min_age, max_age) # Selecciona todo el rango por defecto
)

# --- APLICAR TODOS LOS FILTROS (Incluyendo Edad) ---
# Usamos .between() para el rango del slider
st.session_state["df_filtrado"] = df[
    (df['gender'].isin(generos_sel)) & 
    (df['occupation'].isin(ocupaciones_sel)) & 
    (df['age'].between(rango_edad[0], rango_edad[1]))
]

pg.run()


