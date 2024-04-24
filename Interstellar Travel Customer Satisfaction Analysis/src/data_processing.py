import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# import sys
# sys.path.append('../')


# Exporto el archivo csv de raw
df = pd.read_csv('../data/raw/interstellar_travel.csv')

# Guardo información para poder hacer los selectbox de streamlit
star_system_destination = df[['Star System', 'Destination', 'Distance to Destination (Light-Years)']]
star_system_destination.to_csv('../app/data/star_system_destination.csv', index=False)

# Relleno los NaN de la columna 'Special Request' por 'Other'
df['Special Requests'] = df['Special Requests'].fillna('Other')

# Hago un mapeo de la columna 'Special Requests' para convertir las diferentes categorías en valores numéricos
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
list_star_system = list((df.groupby('Star System')['Customer Satisfaction Score'].mean().sort_values()).index)
dict_star_system = {}
for i in range(len(list_star_system)):
    dict_star_system[list_star_system[i]] = i
df_star_system = pd.DataFrame(list(dict_star_system.items()), columns=['star_system', 'num'])
df_star_system.to_csv('../app/data/star_system.csv', index=False)
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
df['Tiempo Espera']

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

# Guardo el nuevo dataframe en un archivo csv
df.to_csv('../data/processed/interstellar_travel_processed.csv', index=False)

