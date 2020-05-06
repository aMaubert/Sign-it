import os
import numpy as np
from PIL import Image

from app.image.format import Format


class Loader:

    def __init__(self, categories, convert_format=Format.RGB, image_size=(64, 64)):
        self.train_directory = './dataset/train'
        self.test_directory = './dataset/test'
        self.convert_format = Format.to_str(convert_format)
        self.image_size = image_size
        self.categories = categories

    def load_dataset(self):

        x_train, y_train = self.load_training()
        x_test, y_test = self.load_test()
        return (x_train, y_train), (x_test, y_test)

    def load_training(self):
        x_images = []
        y_trains = []
        index_category = 0

        for category in self.categories:
            y_training = [0, 0, 0]
            y_training[index_category] = 1
            for file in os.listdir(f'{self.train_directory}/{category}'):
                image = Image.open(f'{self.train_directory}/{category}/{file}')
                image = image.resize(self.image_size).convert(self.convert_format)
                x_images.append(np.array(image) / 255)
                y_trains.append(y_training)
            index_category += 1

        x_train = np.array(x_images)
        y_train = np.array(y_trains)
        return x_train, y_train

    def load_test(self):
        x_images_test = []
        y_tests = []

        index_category = 0
        for category in self.categories:
            y_training = [0, 0, 0]
            y_training[index_category] = 1
            for file in os.listdir(f'{self.test_directory}/{category}'):
                image = Image.open(f'{self.test_directory}/{category}/{file}')
                image = image.resize(self.image_size).convert(self.convert_format)
                x_images_test.append(np.array(image) / 255)
                y_tests.append(y_training)
            index_category += 1

        x_test = np.array(x_images_test)
        y_test = np.array(y_tests)
        return x_test, y_test
