from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.activations import sigmoid
from tensorflow.keras.losses import mean_squared_error
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

from datasetLoader import DatasetLoader


def create_linear_model():
    model = Sequential()
    model.add(Flatten())
    model.add(Dense(3, activation=sigmoid))
    model.compile(optimizer=SGD(), loss=mean_squared_error, metrics=['accuracy'])
    return model


if __name__ == '__main__':
    categories = ['danger', 'obligation', 'prohibition']
    dataset_loader = DatasetLoader(categories)
    (x_train, y_train), (x_test, y_test) = dataset_loader.load_dataset()
    print(x_train.shape)
    print(y_train.shape)

    print(x_test.shape)
    print(y_test.shape)

    # model = create_linear_model()
    model = create_linear_model()
    logs = model.fit(x_train, y_train, batch_size=4, epochs=500, verbose=1, validation_data=(x_test, y_test))

    true_values = np.argmax(y_train, axis=1)
    predictions = np.argmax(model.predict(x_train), axis=1)

    print("Confusion Train Matrix After Training")
    print(confusion_matrix(true_values, predictions))
    print(f'Train Acc : {model.evaluate(x_train, y_train)[1]}')
    print(f'Test Acc : {model.evaluate(x_test, y_test)[1]}')

    plt.plot(logs.history['accuracy'])
    plt.plot(logs.history['val_accuracy'])
    plt.show()

    plt.plot(logs.history['loss'])
    plt.plot(logs.history['val_loss'])
    plt.show()
    #model.save('linear_model_SGD.keras')

