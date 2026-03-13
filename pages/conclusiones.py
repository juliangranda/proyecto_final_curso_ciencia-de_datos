import streamlit as st

# Título principal centrado
st.markdown("<h1 style='text-align: center;'>🏁 Conclusiones Finales</h1>", unsafe_allow_html=True)

st.divider()

# --- Conclusión 1: Ocupación (Riesgo) ---
# Usamos una columna vacía para centrar o simplemente contenedores de color
st.subheader("🏢 El Entorno Laboral")
st.error("""
**1) Impacto de la Ocupación:** Las profesiones en **salud, ingeniería y ventas** presentan los niveles de estrés más críticos. Existe una correlación directa donde estos picos de estrés reducen la calidad del sueño a niveles inferiores a **6/10**.
""")

# --- Conclusión 2: Actividad Física (Bienestar) ---
st.subheader("🏃‍♂️ Hábitos de Vida")
st.success("""
**2) Beneficios de la Actividad Física:** Superar los **7,000 pasos diarios** actúa como un protector del descanso. Se observa una mejora significativa en la calidad del sueño, demostrando que el movimiento físico ayuda a mitigar el impacto del estrés diario.
""")

# --- Conclusión 3: Calidad vs Cantidad (Revelación) ---
st.subheader("💡 El 'Insight' Principal")
st.info("""
**3) Calidad sobre Cantidad:** Dormir más no siempre es dormir mejor. El análisis revela que usuarios con **6 horas de alta calidad** manejan mejor el estrés que aquellos con **8 horas de sueño interrumpido** o de baja calidad.
""")

st.divider()

st.markdown("<h1 style='text-align: center;'>🏁 Recomendaciones</h1>", unsafe_allow_html=True)
