import streamlit as st
from PIL import Image
import pandas as pd
import streamlit.components.v1 as c
import pickle
import streamlit as st
from datetime import datetime, timedelta

star_system_destination = pd.read_csv('../app/data/star_system_destination.csv') 

st.set_page_config(page_title="Interstellar Travel Customer Satisfaction Analysis",
                   page_icon="img/nave_2.ico")

seleccion = st.sidebar.selectbox("Select menu",  ["Home", "Model", "Design your trip"])

if seleccion == "Home":
    st.title("Interstellar Travel")
    img = Image.open("img/viajes-interestelares.jpg")
    st.image(img)

elif seleccion == "Design your trip":
    st.markdown("### Design your trip to get the best experience")
    img = Image.open("img/odisea-interestelar-800x445.jpg")
    st.image(img)

    age = st.slider("Enter your age:", min_value=0, max_value=100, value=0)

    gender = st.selectbox("Enter your gender:", ["Male", "Female"])

    loyalty_program = st.selectbox("Are you a member of the Loyalty Program?:", ["Yes", "No"])

    occupation = st.selectbox("Enter your occupation:", ["Scientist", "Businessperson", "Explorer", "Tourist", "Colonist", "Other"])

    purpose_of_travel = st.selectbox("Enter your purpose of travel:", ["Tourism", "Research", "Business", "Colonization", "Other"])
    

    distance_to_destination = st.number_input("Enter the distance (in light years) you would like to travel to:", min_value=0.0, max_value=2625.0, value=0.0, step=0.1)
    

    col1, col2 = st.columns([1, 1])
    
    with col1:
        options_destinations = pd.DataFrame({'Destinations': star_system_destination[star_system_destination['Distance to Destination (Light-Years)'] >= distance_to_destination].sort_values(by='Distance to Destination (Light-Years)')['Destination'].unique()})
        destination = st.selectbox("Select Destination:", options_destinations["Destinations"].tolist())

    with col2:
        options_star_system = pd.DataFrame({'Star System': star_system_destination[star_system_destination['Destination'] == destination]['Star System'].unique()})
        star_system = st.selectbox("Select Star System:", options_star_system["Star System"].tolist())

    transportation_type = st.selectbox("Enter the transportation you would like to travel into:", ["Ion Thruster", "Solar Sailing", "Warp Drive", "Other"]) 


    col1, col2 = st.columns([1, 1])

    with col1:
        travel_class = st.selectbox("Enter the travel class you would like to travel in:", ["Luxury", "Business", "Economy"]) 
        
    with col2:
        special_requests = st.selectbox("Enter the special requests for your travel:", ["Window Seat", "Special Meal", "Extra Space Suit", "Other"]) 

    companions = st.number_input("Enter the number of companions for your travel:", min_value=0, max_value=13, value=0)

    duration_of_stay = st.number_input("Enter how long would you like to stay (in earth days):", min_value=0, max_value=450, value=0)

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
    month = booking_date.month

    price_of_trip = st.number_input("Enter the price of the trip in Galactic Credits:", min_value=0.0, max_value=105000.0, value=0.0, step=0.1)
    

    df = pd.DataFrame({'Age': [age], 
                       'Gender': [gender],
                       'Occupation': [occupation],
                       'Travel Class': [travel_class], 
                       'Destination': [destination],
                       'Star System': [star_system], 
                       'Distance to Destination (Light-Years)': [distance_to_destination],
                       'Duration of Stay (Earth Days)': [duration_of_stay], 
                       'Number of Companions': [companions],
                       'Purpose of Travel': [purpose_of_travel], 
                       'Transportation Type': [transportation_type], 
                       'Price (Galactic Credits)': [price_of_trip],
                       'Booking Date': [booking_date], 
                       'Departure Date': [departure_date],
                       'Special Requests': [special_requests],
                       'Loyalty Program Member': [loyalty_program], 
                       'Month': [month]})
    

    df['Special Requests'] = df['Special Requests'].map({'Other' : 0,
                                                     'Special Meal' : 1, 
                                                     'Window Seat' : 1,        
                                                     'Extra Space Suit' :1})

    # Hago un mapeo de la columna 'Gender' para convertir las diferentes categorías en valores numéricos
    df['Gender'] = df['Gender'].map({'Male': 0,
                                    'Female': 1})

    # Hago un mapeo de la columna 'Occupation' para convertir las diferentes categorías en valores numéricos  
    df['Occupation'] = df['Occupation'].map({'Scientist' : 0,
                                             'Businessperson' : 1, 
                                             'Explorer' : 3,        
                                             'Other' :3,           
                                             'Tourist' :3,        
                                             'Colonist' : 3})        

    # Hago un mapeo de la columna 'Travel Class' para convertir las diferentes categorías en valores numéricos 
    df['Travel Class'] = df['Travel Class'].map({'Economy': 0,
                                                 'Business': 0,
                                                 'Luxury': 1})

    # Hago un mapeo de la columna 'Destination' para convertir las diferentes categorías en valores numéricos 
    df['Destination'] = df['Destination'].map({'Alpha Centauri': 0,
                                               'Trappist-1': 0,
                                               'Exotic Destination 1': 5,
                                               'Gliese 581': 5,
                                               'Tau Ceti': 5,
                                               'Epsilon Eridani': 5,
                                               'Proxima Centauri': 5,
                                               'Kepler-22b': 5,
                                               'Lalande 21185': 5,
                                               'Exotic Destination 10': 5,
                                               'Exotic Destination 4': 5,
                                               'Exotic Destination 5': 5,
                                               'Exotic Destination 2': 5,
                                               'Exotic Destination 3': 5,
                                               'Exotic Destination 9': 5,
                                               'Barnard\'s Star': 5,
                                               'Zeta II Reticuli': 5,
                                               'Exotic Destination 7': 5,
                                               'Exotic Destination 8': 5,
                                               'Exotic Destination 6': 5})  

    # Hago un mapeo de la columna 'Star System' para convertir las diferentes categorías en valores numéricos 
    df_star_system = pd.read_csv('../app/data/star_system.csv') 
    df['Star System'] = df['Star System'].map(df_star_system.set_index('star_system')['num'])

    # Hago un mapeo de la columna 'Purpose of Travel' para convertir las diferentes categorías en valores numéricos 
    df['Purpose of Travel'] = df['Purpose of Travel'].map({'Tourism' : 0,
                                                           'Research' : 1, 
                                                           'Business' : 1,        
                                                           'Colonization' :1,           
                                                           'Other' :1})

    # Hago un mapeo de la columna 'Transportation Type' para convertir las diferentes categorías en valores numéricos 
    df['Transportation Type'] = df['Transportation Type'].map({'Ion Thruster' : 0,
                                                               'Other' : 0, 
                                                               'Solar Sailing' : 0,        
                                                               'Warp Drive' :2})

    # Convierto las columnas 'Booking Date' y 'Departure Date' a tipo datetime, y creo una nueva columna 'Tiempo Espera' 
    df['Booking Date'] = pd.to_datetime(df['Booking Date'])
    df['Departure Date'] = pd.to_datetime(df['Departure Date'])
    df['Tiempo Espera'] = df['Departure Date'] - df['Booking Date']
    df['Tiempo Espera'] = pd.to_numeric(df['Tiempo Espera'])
    df['Tiempo Espera'] = df['Tiempo Espera']/10**16


    # Hago un mapeo de la columna 'Loyalty Program' para convertir las diferentes categorías en valores numéricos 
    df['Loyalty Program Member'] = df['Loyalty Program Member'].map({'No': 0,
                                                                     'Yes': 4})

    # Hago un mapeo de la columna 'Month' para convertir las diferentes categorías en valores numéricos 
    df['Month'] = df['Month'].map({6: 0,
                                   7: 1,
                                   8: 1,
                                   2: 3,
                                   3: 3,
                                   4: 4,
                                   5: 4,
                                   1: 6,
                                   9: 7,
                                   12: 7,
                                   10: 7,
                                   11: 7})
    
    df_predict = df[['Age', 'Gender', 'Occupation', 
        'Travel Class', 'Destination', 'Star System', 
        'Distance to Destination (Light-Years)',
        'Duration of Stay (Earth Days)', 'Number of Companions',
        'Purpose of Travel', 'Transportation Type',
        'Price (Galactic Credits)', 'Special Requests',
        'Loyalty Program Member', 'Month',
        'Tiempo Espera']]
    
    # Cargar el modelo guardado con pickle
    filename = '../models/best_model.pkl'
    with open(filename, "rb") as archivo_entrada:
        best_model = pickle.load(archivo_entrada)


    # Agregar un botón para realizar la predicción
    if st.button('Predict Satisfaction Level'):
    # Realizar la predicción solo cuando se presiona el botón
        prediccion = best_model.predict(df_predict)
        st.markdown("### Predicted Satisfaction Level:")
        st.markdown(f"- **The predicted satisfaction level for your trip is:** {prediccion}")


elif seleccion == "Model":
    st.markdown("### Model Information")
    st.write("Here you can learn more about the predictive model and view charts.")
    
    # Cargar el modelo guardado con pickle
    filename = '../models/best_model.pkl'
    with open(filename, "rb") as archivo_entrada:
        best_model = pickle.load(archivo_entrada)
    
    # # Agregar una sección para mostrar información sobre el modelo
    st.subheader("Model Summary")
    img = Image.open("img/summary.png")
    st.image(img)
    
    # Agregar secciones para mostrar gráficos relevantes
    st.subheader("Model Performance")
    st.write("Performance of model 10_PCA12_GBoosting")
    img = Image.open("img/mod4.png")
    st.image(img)
    img = Image.open("img/performance1.png")
    st.image(img)
    img = Image.open("img/performance2.png")
    st.image(img)
    


    

