import pandas as pd
import joblib

# Predict function
class Inference:
    def __init__(self, model_path, data_path):
        self.model_path = model_path
        self.data_path = data_path

    def predict(self):
        # Load model and data
        model = joblib.load(self.model_path)
        data = pd.read_csv(self.data_path)
        data = data.drop(columns=["id"])
        
        # Make predictions
        predictions = model.predict(data)
        print(predictions)
        
        return predictions
