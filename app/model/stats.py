from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt


class Stats:

    def __init__(self, model, x_train, y_train, x_test, y_test, logs):
        self.model = model
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.logs = logs

    def show_accuracy(self):
        true_values = np.argmax(self.y_train, axis=1)
        predictions = np.argmax(self.model.predict(self.x_train), axis=1)
        print(confusion_matrix(true_values, predictions))
        print(f'Train Acc : {self.model.evaluate(self.x_train, self.y_train)[1]}')
        print(f'Test Acc : {self.model.evaluate(self.x_test, self.y_test)[1]}')

    def show_graph(self):
        plt.plot(self.logs.history['accuracy'])
        plt.plot(self.logs.history['val_accuracy'])
        plt.show()
