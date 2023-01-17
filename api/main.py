from fastapi import FastAPI, HTTPException, Form
from api.predict import Inference

app = FastAPI()


@app.get("/")
def read_root():
    """
    A simple endpoint to check if the API is running.
    """
    return {"message": "API is up and running!"}


@app.post("/predict")
def api_predict(model_path: str = Form(...), data_path: str = Form(...)):
    """
    Endpoint for making predictions.

    Parameters:
    - model_path (str): path to the saved model file
    - data_path (str): path to the data file

    Returns:
    - predictions (List[Tuple[int, str]]): a list of tuples containing the id and predicted label
    """
    try:
        predictions = Inference(model_path, data_path).predict()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="An error occurred during the prediction process. Please check the model and data paths and try again.",
        )
    return predictions
