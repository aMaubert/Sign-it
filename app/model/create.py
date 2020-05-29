from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.activations import sigmoid, tanh
from tensorflow.keras.losses import mean_squared_error

from app.model.type import Type as ModelType


def create_model(model_type: ModelType):
    if model_type == ModelType.LinearModel:
        return create_linear_model()
    elif model_type == ModelType.MLPModel:
        return create_mlp_model()
    raise Exception('No model Type found')


def create_linear_model():
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(3, activation=sigmoid))
    model.compile(optimizer=SGD(), loss=mean_squared_error,
                  metrics=['accuracy'])
    return model


def create_mlp_model():
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(256, activation=tanh))
    model.add(Dense(256, activation=tanh))
    model.add(Dense(3, activation=sigmoid))
    model.compile(optimizer=SGD(), loss=mean_squared_error,
                  metrics=['accuracy'])
    return model
