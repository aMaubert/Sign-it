from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.activations import sigmoid
from tensorflow.keras.losses import mean_squared_error

from app.model.type import Type


def create_model(model_type: Type):
    if model_type == Type.LinearModel:
        return create_linear_model()
    raise Exception('No model Type found')


def create_linear_model():
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(3, activation=sigmoid))
    model.compile(optimizer=SGD(), loss=mean_squared_error, metrics=['accuracy'])
    return model
