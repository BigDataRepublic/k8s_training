import os
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
import joblib


class Trainer:
    def __init__(self, data_path: str):
        # Input validation
        if not os.path.isfile(data_path):
            raise ValueError(f"Invalid data path: {data_path}")

        self.data_path = data_path
        self.X, self.y = self.load_data()
        self.model = RandomForestClassifier()

    def load_data(self):
        data = pd.read_csv(self.data_path)
        X = data.drop(columns=["price_range"])
        y = data["price_range"]
        return X, y

    def train(self):
        with mlflow.start_run():
            self.model.fit(self.X, self.y)
            mlflow.log_param("model_type", "RandomForestClassifier")
            mlflow.sklearn.log_model(self.model, "model")
            print("MLFlow run with run_id {}".format(mlflow.active_run().info.run_id))
        return self.model


class Model:
    def __init__(self, model):
        self.model = model

    def save(self, file_path):
        joblib.dump(self.model, file_path)


if __name__ == "__main__":
    trainer = Trainer("data/train.csv")
    model = trainer.train()
    print("Model trained")
    Model(model).save("rf.pkl")
    print("Model saved")
