import pandas as pd
import joblib
from typing import List, Tuple
import functools


class Inference:
    def __init__(self, model_path: str, data_path: str) -> None:
        """
        Initialize the Inference class with the path to the saved model and the data file.

        Parameters:
        - model_path (str): path to the saved model file
        - data_path (str): path to the data file

        """
        self.model_path = model_path
        self.data_path = data_path
        self._cache = {}
        self.required_headers = [
            "id",
            "battery_power",
            "blue",
            "clock_speed",
            "dual_sim",
            "fc",
            "four_g",
            "int_memory",
            "m_dep",
            "mobile_wt",
            "n_cores",
            "pc",
            "px_height",
            "px_width",
            "ram",
            "sc_h",
            "sc_w",
            "talk_time",
            "three_g",
            "touch_screen",
            "wifi",
        ]

    @functools.lru_cache(maxsize=None)
    def predict(self) -> List[Tuple[int, str]]:
        """
        Make predictions on the data and return the results.

        Returns:
        - predictions (List[Tuple[int, str]]): a list of tuples containing the id and predicted label

        """

        # load model
        try:
            model = joblib.load(self.model_path)
        except FileNotFoundError:
            raise ValueError(f"The model path {self.model_path} is not valid.")

        # load data
        try:
            data = pd.read_csv(self.data_path)
        except FileNotFoundError:
            raise ValueError(f"The data path {self.data_path} is not valid.")

        # check if the data file has the correct headers
        headers = data.columns
        if not set(headers).issuperset(self.required_headers):
            missing_headers = list(set(self.required_headers) - set(headers))
            raise ValueError(
                f"The data file is missing required headers: {missing_headers}"
            )

        # Extract the ids column
        ids = data["id"]

        # Remove the id column
        data = data.drop(columns=["id"])

        # Make predictions
        predictions = model.predict(data)

        # Combine the ids and predictions into a list of tuples
        predictions = list(zip(ids, predictions))
        return [(int(i), int(j)) for i, j in predictions]
