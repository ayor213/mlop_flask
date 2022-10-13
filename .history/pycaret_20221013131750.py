# load dataset
from pycaret.datasets import get_data
insurance = get_data('insurance')

# init environment
from pycaret.regression import *
r1 = setup(insurance,
           target = 'charges',
           session_id = 123,
           normalize = True,
           polynomial_features = True,
           trigonometry_features = True,
           feature_interaction=True,
           bin_numeric_features= ['age', 'bmi'])
#Model training and selection
best_lr= compare_models()

# Analyse best model
evaluate_model(best_lr)

# predictions on new data
predictions = predict_models(best_lr)

# save pipeline/model
save_model(best_lr,'MLOps_Pipeline')