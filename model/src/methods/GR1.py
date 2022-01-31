import numpy as np
from .algorithms.LSTM import model

def method(x_train: np.array, x_test: np.array, y_train: np.array, y_test: np.array, x: np.array, y: np.array) -> None:
    model(x_train, x_test, y_train, y_test, x, y)