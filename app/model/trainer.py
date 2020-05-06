from app.dataset.loader import Loader
from app.model.create import create_model
from app.model.stats import Stats


class Trainer:

    def __init__(self, categories, model_type):
        self.model_type = model_type
        self.dataset_loader = Loader(categories)

    def training(self):
        (x_train, y_train), (x_test, y_test) = self.dataset_loader.load_dataset()
        print(x_train.shape)
        print(y_train.shape)

        print(x_test.shape)
        print(y_test.shape)

        model = create_model(self.model_type)

        print("Confusion Train Matrix After Training")
        stats = Stats(model, x_train, y_train, x_test, y_test, None)
        stats.show_accuracy()

        logs = model.fit(x_train, y_train, batch_size=4, epochs=2, verbose=0, validation_data=(x_test, y_test))

        print("Confusion Train Matrix After Training")
        stats = Stats(model, x_train, y_train, x_test, y_test, logs)
        stats.show_accuracy()

        stats.show_graph()

        # model.save('linear_model_SGD.keras')