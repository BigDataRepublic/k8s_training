import os
import requests
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-e", "--endpoint", type=str, default="predict", help="The API endpoint to call"
)
args = parser.parse_args()


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

    env = os.environ.get("ENV", "local")
    if env == "local":
        url = f"http://localhost:8000/{args.endpoint}"
    else:
        url = f"http://fastapi-service:8000/{args.endpoint}"

    try:
        response = requests.post(
            url,
            data={"model_path": model_path, "data_path": data_path},
        )
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"An error occurred: {e}")
    else:
        response = response.json()
        print(response)


if __name__ == "__main__":
    begin = time.time()
    MODEL_PATH = os.environ.get("MODEL_PATH", "artifacts/rf.pkl")
    if args.endpoint == "predict":
        api_request(MODEL_PATH, "data/test.csv")
    elif args.endpoint == "train":
        api_request(MODEL_PATH, "data/train.csv")
    else:
        raise ValueError("Invalid endpoint. Must be 'predict' or 'train'")

    print("Time taken:", round(time.time() - begin, 2), "seconds")
