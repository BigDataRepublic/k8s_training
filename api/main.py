from fastapi import FastAPI, HTTPException, Form
from api.predict import Inference
from api.train import Trainer, Model
import psycopg2

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
    # Connect to the database
    conn = psycopg2.connect(
        host="postgres-service",
        port="5432",
        dbname="database",
        user="user",
        password="password",
    )

    # Create a cursor
    cursor = conn.cursor()

    # Insert the predictions into the database
    for id, label in predictions:
        cursor.execute(
            "INSERT INTO predictions (id, label) VALUES (%s, %s)", (id, label)
        )

    # Commit the changes
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return predictions


@app.post("/train")
def api_train(model_path: str = Form(...), data_path: str = Form(...)):
    """
    Endpoint for training the model

    Parameters:
    - model_path (str): path to the saved model file
    - data_path (str): path to the data file
    """
    try:
        model = Trainer(data_path).train()
        Model(model).save(model_path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="An error occurred during the training process. Please check the data paths and try again.",
        )
    return {"message": "Model trained and saved successfully in!"}
