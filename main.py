from PIL import Image

from app.config import Config
from app.dataset.loader import Loader as DatasetLoader
from app.image.format import Format

from app.mode import Mode
from app.model.save import Saver
from app.model.stats import Stats
from app.model.trainer import Trainer as ModelTrainer
from app.model.load import Loader as ModelLoader

import numpy as np

if __name__ == '__main__':
    config = Config()
    config.load_config()

    print(config)

    if config.mode == Mode.Training:
        print('Mode training')
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
                            model_type=config.model_type, image_size=config.image_size,
                            image_format=config.image_format)
        model_saver.save()

    elif config.mode == Mode.Use:
        print('Mode Use')

        dataset_loader = DatasetLoader(config.categories, config.image_format, config.image_size)
        (x_train, y_train), (x_test, y_test) = dataset_loader.load_dataset()

        #Load existing model
        model_loader = ModelLoader(config.models_directory, config.model_type,
                                   image_size=config.image_size, image_format=config.image_format)
        model = model_loader.load()

        stats = Stats(model, x_train, y_train, x_test, y_test, None)
        stats.show_accuracy()

        #Make a prediction
        image = Image.open('./dataset/test/obligation/212.jpg')
        image = image.resize(config.image_size).convert(Format.to_str(config.image_format))
        images_to_predicts = np.array([np.array(image) / 255])
        predictions = model.predict(images_to_predicts)

        print('Result prediction')
        for i in range(len(predictions[0])):
            print(f'{config.categories[i]} : {predictions[0][i] * 100}')

        predictions *= 100
        print(predictions)
        Stats.predict_result(categories=config.categories, predictions=predictions[0])
        Stats.predict_image(image=image, categories=config.categories,
                            predictions=predictions[0])
        Stats.predict_show_all(image=image, categories=config.categories,
                             predictions=predictions[0])