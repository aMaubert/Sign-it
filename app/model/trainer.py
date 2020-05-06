from app.model.create import create_model


class Trainer:

    def __init__(self, x_train, y_train, x_test, y_test,
                 model_type, batch_size, nb_epoch):
        self.model_type = model_type
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.batch_size = batch_size
        self.nb_epoch = nb_epoch

    def training(self):
        print(self.x_train.shape)
        print(self.y_train.shape)

        print(self.x_test.shape)
        print(self.y_test.shape)

        model = create_model(self.model_type)

        logs = model.fit(self.x_train, self.y_train, batch_size=self.batch_size, epochs=self.nb_epoch, verbose=0,
                         validation_data=(self.x_test, self.y_test))

        return model, logs
