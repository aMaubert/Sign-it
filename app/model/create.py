from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Concatenate, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.activations import sigmoid, tanh, relu
from tensorflow.keras.losses import mean_squared_error
from tensorflow.keras import Input, Model

from app.model.type import Type as ModelType


def create_model(model_type: ModelType, image_size: tuple):
    if model_type == ModelType.LinearModel:
        return create_linear_model()
    elif model_type == ModelType.MLPModel:
        return create_mlp_model()
    elif model_type == ModelType.CNNModel:
        return create_convolutional_neural_network_model()
    elif model_type == ModelType.DenseResidualNN:
        return create_dense_residual_neural_network_model(image_size=image_size)
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


def create_convolutional_neural_network_model():
    model = Sequential()

    model.add(Conv2D(4, (3, 3), padding='same', activation=relu))
    model.add(MaxPool2D((2, 2)))

    model.add(Conv2D(8, (3, 3), padding='same', activation=relu))
    model.add(MaxPool2D((2, 2)))

    model.add(Conv2D(16, (3, 3), padding='same', activation=relu))
    # model.add(MaxPool2D((2, 2)))

    model.add(Flatten())
    model.add(Dense(64, activation=tanh))
    model.add(Dense(3, activation=sigmoid))
    model.compile(optimizer=SGD(), loss=mean_squared_error,
                  metrics=['accuracy'])
    return model


def create_dense_residual_neural_network_model(image_size):
    input_tensor = Input((image_size[0], image_size[1], 3))

    previous_tensor = Flatten()(input_tensor)

    next_tensor = Dense(64, activation=relu)(previous_tensor)

    previous_tensor = Concatenate()([previous_tensor, next_tensor])

    next_tensor = Dense(64, activation=relu)(previous_tensor)

    previous_tensor = Concatenate()([previous_tensor, next_tensor])

    next_tensor = Dense(64, activation=relu)(previous_tensor)

    previous_tensor = Concatenate()([previous_tensor, next_tensor])

    next_tensor = Dense(64, activation=tanh)(previous_tensor)
    next_tensor = Dense(3, activation=sigmoid)(next_tensor)

    model = Model(input_tensor, next_tensor)

    model.compile(optimizer=SGD(), loss=mean_squared_error,
                  metrics=['accuracy'])
    return model
