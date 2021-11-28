import numpy as np

from keras.models import Sequential, Model
from tensorflow.python.keras.layers import LSTM, Dense, Dropout, Bidirectional, BatchNormalization, GRU, Input
from tensorflow.keras.optimizers import Adam, SGD, RMSprop, Adadelta, Adagrad, Adamax, Nadam, Ftrl

def LSTM(x_train: np.array, x_test: np.array, y_train: np.array, y_test: np.array) -> None:
    model = Sequential()

    model.add(LSTM(64, return_sequences=True, activation='tanh', input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(Dropout(0.20))

    model.add(LSTM(64, return_sequences=False, activation='tanh'))
    model.add(Dropout(0.20))

    model.add(Dense(12, activation='tanh'))
    model.add(Dense(12, activation='tanh'))
    model.add(Dense(12, activation='tanh'))
    model.add(Dense(12, activation='tanh'))
    model.add(Dense(12, activation='tanh'))
    model.add(Dense(1))

    model.compile(loss='mse', optimizer=Adam(learning_rate=0.005), metrics=['mean_absolute_percentage_error'])
    model.fit(x_train, y_train, epochs=1000, batch_size=1200, shuffle=True, validation_data=(x_test, y_test), verbose=1)

    return model