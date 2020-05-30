from PIL import Image

from datetime import datetime

from app.config import Config
from app.dataset.loader import Loader as DatasetLoader
from app.image.format import Format

from app.mode import Mode
from app.model.save import Saver
from app.model.stats import Stats
from app.model.trainer import Trainer as ModelTrainer
from app.model.load import Loader as ModelLoader

import numpy as np


def launch_training(config):
    dataset_loader = DatasetLoader(config.categories, config.image_format, config.image_size)
    (x_train, y_train), (x_test, y_test) = dataset_loader.load_dataset()

    trainer = ModelTrainer(x_train, y_train, x_test, y_test,
                           config.model_type, config.model_training_batch_size,
                           config.model_training_nb_epoch)
    model, logs = trainer.training()

    print("Confusion Train Matrix After Training")
    stats = Stats(model, x_train, y_train, x_test, y_test, logs)
    stats.show_accuracy()
    stats.show_graph_accuracy()
    stats.show_graph_losses()

    model_saver = Saver(model=model, models_directory=config.models_directory,
                        model_type=config.model_type, nb_epochs=config.model_training_nb_epoch,
                        image_size=config.image_size, image_format=config.image_format)
    model_saver.save()


def launch_prediction(config):
    dataset_loader = DatasetLoader(config.categories, config.image_format, config.image_size)
    (x_train, y_train), (x_test, y_test) = dataset_loader.load_dataset()

    # Load existing model
    model_loader = ModelLoader(config.models_directory, model_type=config.model_type,
                               nb_epochs=config.model_training_nb_epoch,
                               image_size=config.image_size, image_format=config.image_format)
    model = model_loader.load()

    stats = Stats(model, x_train, y_train, x_test, y_test, None)
    stats.show_accuracy()

    # ==== Make a predictions ====
    images = []
    images_to_predicts = []

    image = Image.open('./dataset/test/danger/A1a_27.jpg')
    image = image.resize(config.image_size).convert(Format.to_str(config.image_format))
    images.append(image)
    images_to_predicts.append(np.array(image) / 255)

    image = Image.open('./dataset/test/obligation/212.jpg')
    image = image.resize(config.image_size).convert(Format.to_str(config.image_format))
    images.append(image)
    images_to_predicts.append(np.array(image) / 255)

    image = Image.open('./dataset/test/prohibition/b2c-7.jpg')
    image = image.resize(config.image_size).convert(Format.to_str(config.image_format))
    images.append(image)
    images_to_predicts.append(np.array(image) / 255)

    predictions = model.predict(np.array(images_to_predicts))

    print('Result prediction')
    print(predictions)
    # Stats.predict_show_all(images=images, categories=config.categories,
    #                          predictions=predictions)
    Stats.predict_show_image_by_image(images=images, categories=config.categories,
                                      predictions=predictions)


if __name__ == '__main__':
    start = datetime.now()

    start_time = start.strftime("%H:%M:%S")

    config = Config()
    config.load_config()

    print(config)

    if config.mode == Mode.Training:
        print('Mode training')
        launch_training(config=config)

    elif config.mode == Mode.Use:
        print('Mode Use')
        launch_prediction(config=config)

    finish = datetime.now()
    finish_time = finish.strftime("%H:%M:%S")

    print("Start Time =", start_time)
    print("finish Time =", finish_time)
    print(start - finish)
