import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# 1. Título de tu app
st.title("INVENTUM.")

# 2. Conexión con tu Google Sheets (Pega tu link aquí abajo)
url = "https://docs.google.com/spreadsheets/d/17DwdL-AySwXzvh1lffypPUKf3zKpPw7wCLVXK_tuwTo/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(spreadsheet=url)

# 3. Mostrar lo que hay en el inventario
st.subheader("¿Qué tenemos hoy?")
st.dataframe(df)

# 4. Formulario para agregar cosas
with st.form("nuevo"):
    nombre = st.text_input("¿Cómo se llama el componente?")
    cantidad = st.number_input("¿Cuántos hay?", min_value=0)
    if st.form_submit_button("Guardar"):
        st.success(f"¡Anotado! Guardaste {cantidad} de {nombre}")
        # Aquí se guardaría en el Excel
