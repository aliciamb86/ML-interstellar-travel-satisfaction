import yaml

# Defino los best params de mi modelo
best_params = {
    'classifier': 'GradientBoostingRegressor',
    'classifier__max_depth': 10,
    'classifier__min_samples_leaf': 20,
    'classifier__min_samples_split': 20,
    'scaler': None
}

# Guardo el archivo .yaml 
filename = '../models/model_config.yaml'
with open(filename, 'w') as file:
    yaml.dump(best_params, file)
