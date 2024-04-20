import streamlit as st
from PIL import Image
import pandas as pd
import streamlit.components.v1 as c

import streamlit as st
from PIL import Image
import pandas as pd
import streamlit.components.v1 as c

st.set_page_config(page_title="Interstellar Travel Customer Satisfaction Analysis",
                   page_icon="img/nave_2.ico")

seleccion = st.sidebar.selectbox("Select menu", ["Home", "Explore our destinations", "Design your trip"])

if seleccion == "Home":
    st.title("Interstellar Travel")
 
    img = Image.open("img/viajes-interestelares.jpg")
    st.image(img)

elif seleccion == "Design your trip":
    st.write("Design your trip to get the best experience")
    img = Image.open("img/odisea-interestelar-800x445.jpg")
    st.image(img)

    age = st.number_input("Enter your age", min_value=0, max_value=150, value=0)

    gender = st.selectbox("Enter your gender", ["Male", "Female"])

    occupation = st.selectbox("Enter your occupation", ["Scientist", "Businessperson", "Explorer", "Tourist", "Colonist", "Other"])

    purpose_of_travel = st.selectbox("Enter your purpose of travel", ["Tourism", "Research", "Business", "Colonization", "Other"])

    