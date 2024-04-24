import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.decomposition import PCA
import pickle
from sklearn.model_selection import train_test_split 
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingRegressor


# Exporto el archivo csv de interstellar_travel_processed
df = pd.read_csv('../data/processed/interstellar_travel_processed.csv')

# Divido el DataFrame interstellar_travel_processed de forma aleatoria en dos partes iguales
df_1, df_2 = train_test_split(df,
                              test_size=0.5,
                              random_state=42)

# Guardo una parte como test en un archivo csv
df_1.to_csv('../data/test/interstellar_travel_test.csv',  index=False)

# Guardo la otra parte como train en un archivo csv
df_2.to_csv('../data/train/interstellar_travel_train.csv',  index=False)

# Exporto el archivo csv de interstellar_travel_train
df_train = pd.read_csv('../data/train/interstellar_travel_train.csv')

# Exporto el archivo csv de interstellar_travel_test
df_test = pd.read_csv('../data/test/interstellar_travel_test.csv')

# Defino X_train e y_train
X_train_pca = df_train[['Age', 'Gender', 'Occupation', 
                        'Travel Class', 'Destination', 'Star System', 
                        'Distance to Destination (Light-Years)',
                        'Duration of Stay (Earth Days)', 'Number of Companions',
                        'Purpose of Travel', 'Transportation Type',
                        'Price (Galactic Credits)', 'Special Requests',
                        'Loyalty Program Member', 'Month',
                        'Tiempo Espera']]
y_train_pca = df_train['Customer Satisfaction Score']

# Defino X_test e y_test
X_test_pca = df_test[['Age', 'Gender', 'Occupation', 
                      'Travel Class', 'Destination', 'Star System', 
                      'Distance to Destination (Light-Years)',
                      'Duration of Stay (Earth Days)', 'Number of Companions',
                      'Purpose of Travel', 'Transportation Type',
                      'Price (Galactic Credits)', 'Special Requests',
                      'Loyalty Program Member', 'Month',
                      'Tiempo Espera']]
y_test_pca = df_test['Customer Satisfaction Score']


# Defino best_model con los best_params del modelo que mejor ha funcionado
best_model = Pipeline(steps=[
    ('pca', PCA(n_components=12)),
    ('classifier', GradientBoostingRegressor(
        random_state=42,
        max_depth=10,
        min_samples_split=10,
        min_samples_leaf=20
    ))
])

best_model.fit(X_train_pca, y_train_pca)

filename = '../models/best_model.pkl'
with open(filename, 'wb') as archivo_salida:
    pickle.dump(best_model, archivo_salida)
