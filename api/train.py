import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Train function
def train(data_path):
    # Load data
    data = pd.read_csv(data_path)
    X = data.drop(columns=["price_range"])
    y = data["price_range"]
    
    # # Initialize and train model
    model = RandomForestClassifier()
    model.fit(X, y)
    
    return model
    

if __name__ == "__main__":
    # Example usage
    model = train("data/train.csv")
    print("Model trained")
    
    # Save the model
    joblib.dump(model, 'rf.pkl')
    print("Model saved")