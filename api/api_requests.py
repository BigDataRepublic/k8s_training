import os
import requests
import time

MODEL_PATH = os.environ.get("MODEL_PATH", "artifacts/rf.pkl")
DATA_PATH = os.environ.get("DATA_PATH", "data/test.csv")
API_URL = os.environ.get("API_URL", "http://localhost:8000/predict")


def api_request(model_path: str, data_path: str) -> None:
    """
    Make a post request to the API with the provided model and data paths.
    Prints the predictions if the request is successful, otherwise prints the error message.
    """
    # input validation
    if not os.path.isfile(model_path):
        raise ValueError(f"Invalid model path: {model_path}")
    if not os.path.isfile(data_path):
        raise ValueError(f"Invalid data path: {data_path}")
    try:
        response = requests.post(
            API_URL, data={"model_path": model_path, "data_path": data_path}
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"An error occurred: {e}")
    else:
        predictions = response.json()
        print(predictions)


if __name__ == "__main__":
    begin = time.time()
    api_request(MODEL_PATH, DATA_PATH)
    print("Time taken:", round(time.time() - begin, 2), "seconds")
