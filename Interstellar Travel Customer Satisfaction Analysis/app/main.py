import streamlit as st
from PIL import Image
import pandas as pd
import streamlit.components.v1 as c


st.set_page_config(page_title="Interstellar Travel Customer Satisfaction Analysis",
                   page_icon="img/nave_2.ico")

seleccion = st.sidebar.selectbox("Selecciona menu", ["Conoce nuestros destinos", "Diseña tu viaje"])

if seleccion == "Home":
    st.title("Viajes interestelares")

    # with st.expander("¿Qué es esta aplicación?"):
    #     st.write("Es una primera aproximación para solucionar la búsqueda de cargadores eléctricos para facilitar la transición a otras fuentes de energía")

    img = Image.open("img/viajes-interestelares.jpg")
    st.image(img)
# elif seleccion == "EDA":
#     st.write("Aquí irá el EDA")