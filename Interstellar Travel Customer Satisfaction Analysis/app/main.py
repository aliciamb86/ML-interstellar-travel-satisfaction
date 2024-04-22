import streamlit as st
from PIL import Image
import pandas as pd
import streamlit.components.v1 as c


star_system_destination = pd.read_csv('../app/data/star_system_destination.csv') 

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

    age = st.number_input("Enter your age:", min_value=0, max_value=150, value=0)

    gender = st.selectbox("Enter your gender:", ["Male", "Female"])

    loyalty_program = st.selectbox("Are you a member of the Loyalty Program?:", ["Yes", "No"])

    occupation = st.selectbox("Enter your occupation:", ["Scientist", "Businessperson", "Explorer", "Tourist", "Colonist", "Other"])

    purpose_of_travel = st.selectbox("Enter your purpose of travel:", ["Tourism", "Research", "Business", "Colonization", "Other"])
    

    distance_to_destination = st.slider("Enter the distance (in light years) you would like to travel to:", min_value=0, max_value=2625, value=0)
    

    col1, col2 = st.columns([1, 1])
    
    with col1:
        destination = st.text_input("Enter interstellar destination:", "")
        st.markdown("Destination options:")
        suggested_destinations = star_system_destination[star_system_destination['Distance to Destination (Light-Years)'] >= distance_to_destination ]['Destination'].unique()
        st.write(suggested_destinations)

    with col2:
        star_system = st.text_input("Enter star system of the destination:", "")
        st.markdown("Star System options:")
        suggested_options_star_system = star_system_destination[star_system_destination['Destination'] == destination]['Star System'].unique()
        st.write(suggested_options_star_system)

    transportation_type = st.selectbox("Enter the transportation you would like to travel into:", ["Ion Thruster", "Solar Sailing", "Warp Drive", "Other"]) 


    col1, col2 = st.columns([1, 1])

    with col1:
        travel_class = st.selectbox("Enter the travel class you would like to travel in:", ["Luxury", "Business ", "Economy"]) 
        
    with col2:
        special_requests = st.selectbox("Enter the special requests for your travel:", ["Window Seat", "Special Meal", "Extra Space Suit", "Other"]) 

    companions = st.number_input("Enter the number of companions for your travel (13 companions per travel max):", min_value=0, max_value=13, value=0)

    duration_of_stay = st.slider("Enter how long would you like to stay (in earth days):", min_value=0, max_value=450, value=0)

    import streamlit as st
    from datetime import datetime, timedelta

    # Dividir la pantalla en dos columnas
    col1, col2 = st.columns(2)
    
    # Selector de fecha para la primera fecha en la primera columna
    with col1:
        today = datetime.today()
        booking_date = st.date_input("Enter booking date", today)
    
    # Selector de fecha para la segunda fecha en la segunda columna con un rango mínimo aproximadamente 2 años después de la primera fecha
    with col2:
        departure = booking_date + timedelta(days=365*2)
        departure_date = st.date_input("Enter departure date", departure)
    
    from datetime import datetime

    # Definir la fecha
    fecha = datetime.strptime("2023-09-17", "%Y-%m-%d")

    # Obtener el valor numérico del mes
    month = departure_date.month

    