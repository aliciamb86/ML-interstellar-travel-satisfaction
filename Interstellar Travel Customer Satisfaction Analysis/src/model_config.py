import yaml

# Define los mejores parámetros
best_params = {
    'scaler': 'None',
    'pca': {'n_components': 12},
    'classifier': {
        'class_name': 'GradientBoostingRegressor',
        'params': {
            'max_depth': 10,
            'min_samples_leaf': 20,
            'min_samples_split': 10,
            'random_state': 42
        }
    }
}

# Define la ruta del archivo YAML
yaml_file = '../models/best_params_modelo.yaml'

# Guarda los mejores parámetros en formato YAML
with open(yaml_file, 'w') as file:
    yaml.dump(best_params, file)

