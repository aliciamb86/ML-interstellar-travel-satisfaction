import pandas as pd
import numpy as np

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pickle

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

# Exporto el modelo.pkl para evaluarlo
filename = '../models/best_model.pkl'
with open(filename, "rb") as archivo_entrada:
    best_model = pickle.load(archivo_entrada)


# Evalúo mi modelo sobre train
y_pred_train_pca = best_model.predict(X_train_pca)

print("RESULTADOS SOBRE TRAIN")

print("R^2 train:", round(r2_score(y_train_pca, y_pred_train_pca), 2))
print("MAE train:", round(mean_absolute_error(y_train_pca, y_pred_train_pca), 2))
print("MSE train:", round(mean_squared_error(y_train_pca, y_pred_train_pca), 2))
print("RMSE train:", round(np.sqrt(mean_squared_error(y_train_pca, y_pred_train_pca)), 2))

# Evalúo mi modelo sobre test
y_pred_test_pca = best_model.predict(X_test_pca)

print("\nRESULTADOS SOBRE TEST")

print("R^2 test:", round(r2_score(y_test_pca, y_pred_test_pca), 2))
print("MAE test:", round(mean_absolute_error(y_test_pca, y_pred_test_pca), 2))
print("MSE test:", round(mean_squared_error(y_test_pca, y_pred_test_pca), 2))
print("RMSE test:", round(np.sqrt(mean_squared_error(y_test_pca, y_pred_test_pca)), 2))