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

        print('Training elements')
        true_values = np.argmax(self.y_train, axis=1)
        predictions = np.argmax(self.model.predict(self.x_train), axis=1)
        print(confusion_matrix(true_values, predictions))

        print('Test elements')
        true_values_test = np.argmax(self.y_test, axis=1 )
        predictions_test = np.argmax(self.model.predict(self.x_test), axis=1)
        print(confusion_matrix(true_values_test, predictions_test))

        print(f'Train Acc : {self.model.evaluate(self.x_train, self.y_train)[1]}')
        print(f'Test Acc : {self.model.evaluate(self.x_test, self.y_test)[1]}')

    def show_graph_accuracy(self):
        plt.plot(self.logs.history['accuracy'])
        plt.plot(self.logs.history['val_accuracy'])
        plt.xlabel('Accuracy')
        plt.show()

    def show_graph_losses(self):
        plt.plot(self.logs.history['loss'])
        plt.plot(self.logs.history['val_loss'])
        plt.xlabel('Losses')
        plt.show()

    @staticmethod
    def predict_result(categories, predictions, show=True):
        nb_categories = len(categories)

        for i in range(nb_categories):
            predictions_array = predictions
            plt.grid(False)
            plt.xlabel('categories')
            plt.xticks(range(nb_categories), categories)
            plt.ylabel('%')
            plt.yticks([0,10,20,30,40,50,60,70,80,90, 100])
            plot = plt.bar(range(nb_categories), predictions_array, color="#777777")
            predicted_label = np.argmax(predictions_array)
            plot[predicted_label].set_color('red')
        if show:
            plt.show()

    @staticmethod
    def predict_image(image, categories, predictions, show=True):
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])

        predicted_label = np.argmax(predictions)
        x_label = ''
        for i in range(len(predictions)):
            each_prediction = predictions[i]
            x_label += f'{categories[i]} { each_prediction:0.2f} %\n'
        plt.xlabel(x_label, color='blue')
        plt.imshow(image)

        if show:
            plt.show()

    @staticmethod
    def predict_show_image_by_image(images, categories, predictions):
        predictions *= 100

        num_cols = 1
        num_rows = len(predictions)

        plt.figure(figsize=(2 * 2 * (num_cols + 1), 2 * (num_rows + 2) ))

        for i in range(num_rows):
            plt.subplot(num_rows, 2 * num_cols,2*i+1)
            Stats.predict_image(images[i], categories, predictions[i],
                                show=False)
            plt.subplot(num_rows, 2 * num_cols, 2*i+2)
            Stats.predict_result(categories, predictions[i],
                                 show=False)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def predict_show_all(images, categories, predictions):
        predictions *= 100

        num_cols = len(categories)
        num_rows = int(len(predictions) / num_cols)

        plt.figure(figsize=(2 * 2 * (num_cols + 2), 3 * (num_rows + 1)))
        for i in range(len(predictions)):
            plt.subplot(1, 2 * num_cols, 2 * i + 1)
            Stats.predict_image(images[i], categories, predictions[i],
                                show=False)
            plt.subplot(1, 2 * num_cols , 2 * i + 2)
            Stats.predict_result(categories, predictions[i],
                                 show=False)
        plt.tight_layout()
        plt.show()
