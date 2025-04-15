# import os
# import joblib

# # # # Get the absolute path of the model file
# # model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

# # # # Load the model
# # trained_model = joblib.load(model_path)

# import numpy as np

# def preprocess(Open, High, Low, Volume):
#     test_data = [[int(Open), int(High), int(Low), int(Volume)]]
#     trained_model = joblib.load('model.pkl')
#     prediction = trained_model.predict(test_data)
#     return prediction


import os
import joblib
import numpy as np

# ✅ Load the model once globally (good for performance too)
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')

# Try to load the model with error handling
try:
    trained_model = joblib.load(model_path)
except FileNotFoundError:
    raise FileNotFoundError(f"Model file not found at path: {model_path}")

def preprocess(Open, High, Low, Volume):
    """
    Preprocesses the input and returns the model's prediction.
    
    Parameters:
        Open (float or str): Opening price
        High (float or str): Highest price
        Low (float or str): Lowest price
        Volume (float or str): Volume traded

    Returns:
        prediction (array): Predicted value (e.g., next Close price)
    """
    # Convert inputs to integers or floats as needed
    test_data = [[float(Open), float(High), float(Low), float(Volume)]]

    # Make prediction using the loaded model
    prediction = trained_model.predict(test_data)

    return prediction
