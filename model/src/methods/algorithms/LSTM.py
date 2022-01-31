import matplotlib.pyplot as plt
import numpy as np
from keras import backend as K
from keras.models import Model, Sequential
from matplotlib.pyplot import figure
from sklearn.metrics import (mean_absolute_percentage_error,
                             mean_squared_error, r2_score)
from tensorflow.keras.optimizers import (SGD, Adadelta, Adagrad, Adam, Adamax,
                                         Ftrl, Nadam, RMSprop)
from tensorflow.python.keras.layers import (GRU, LSTM, BatchNormalization,
                                            Bidirectional, Dense, Dropout,
                                            Input)


def coeff_determination(y_true, y_pred):
    SS_res =  K.sum(K.square( y_true-y_pred ))
    SS_tot = K.sum(K.square( y_true - K.mean(y_true) ) )
    return ( 1 - SS_res/(SS_tot + K.epsilon()) )

def model(x_train: np.array, x_test: np.array, y_train: np.array, y_test: np.array, x: np.array, y: np.array) -> None:
    model = Sequential()

    model.add(LSTM(64, return_sequences=True, activation='tanh', input_shape=(x_train.shape[1], x_train.shape[2])))
    model.add(Dropout(0.20))

    model.add(LSTM(64, return_sequences=False, activation='tanh'))
    model.add(Dropout(0.20))

    model.add(Dense(10, activation='tanh'))
    model.add(Dense(10, activation='tanh'))
    model.add(Dense(1))

    model.compile(loss='mse', optimizer=Adam(learning_rate=0.005), metrics=[coeff_determination, 'MAPE'])
    model.fit(x_train, y_train, epochs=100, batch_size=1200, shuffle=True, validation_data=(x_test, y_test), verbose=1)
    
    pred = model.predict(x)[:-1]
    resp = y[1:]
    y = y[:-1]

    print(f'R2   {r2_score(pred, y)}')
    print(f'MSE  {mean_squared_error(pred, y)}')
    print(f'MAPE {mean_absolute_percentage_error(pred, y)}')
    figure(figsize=(23, 6), dpi=80)

    plt.plot(y)
    plt.plot(range(y.shape[0]), pred, color='red')
    for i, target, prediction in zip(range(y.shape[0]), y, pred):
        plt.plot([i, i], [target, prediction], label = "pred", linewidth=1, color='tomato')

    plt.show()
