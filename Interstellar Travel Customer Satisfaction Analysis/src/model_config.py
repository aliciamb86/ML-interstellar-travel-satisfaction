import yaml

# Defino los best params de mi modelo
best_params = {
    'PCA': {
        'n_components': 11
    },
    'GradientBoostingRegressor': {
        'max_depth': 10,
        'min_samples_leaf': 20,
        'min_samples_split': 20,
        'random_state': 42
    }
}

# Guardo el archivo .yaml 
filename = '../models/model_config.yaml'
with open(filename, 'w') as file:
    yaml.dump(best_params, file)
