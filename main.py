from app.config import Config
from app.dataset.loader import Loader

from app.mode import Mode
from app.model.save import Saver
from app.model.stats import Stats
from app.model.trainer import Trainer
from app.model.load import Loader as ModelLoader

if __name__ == '__main__':
    config = Config()
    config.load_config()

    print(config)

    if config.mode == Mode.Training:
        print('Mode training')
        dataset_loader = Loader(config.categories, config.image_format, config.image_size)
        (x_train, y_train), (x_test, y_test) = dataset_loader.load_dataset()

        trainer = Trainer(x_train, y_train, x_test, y_test,
                          config.model_type, config.model_training_batch_size,
                          config.model_training_nb_epoch)
        model, logs = trainer.training()

        print("Confusion Train Matrix After Training")
        stats = Stats(model, x_train, y_train, x_test, y_test, logs)
        stats.show_accuracy()

        stats.show_graph()

        model_saver = Saver(model, config.models_directory, config.model_type)
        model_saver.save()

    elif config.mode == Mode.Use:
        print('Mode Use')

        dataset_loader = Loader(config.categories, config.image_format, config.image_size)
        (x_train, y_train), (x_test, y_test) = dataset_loader.load_dataset()

        #Load existing model
        model_loader = ModelLoader(config.models_directory, config.model_type)
        model = model_loader.load()

        stats = Stats(model, x_train, y_train, x_test, y_test, None)
        stats.show_accuracy()
