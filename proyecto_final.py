import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

url = "https://raw.githubusercontent.com/juliangranda/Prueba/refs/heads/main/dbs/Sleep_health_and_lifestyle_dataset.csv"
df = pd.read_csv(url)

df.columns = df.columns.str.lower()
df.rename(columns= {"bmi category":"indice de masa corporal"}, inplace=True)

#Tratamiento de datos
df.fillna({"sleep disorder":"unknown"}, inplace=True)
print()