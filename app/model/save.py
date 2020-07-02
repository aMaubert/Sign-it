from os import path


class Saver:

    def __init__(self, model, models_directory,
                 model_type, nb_epochs, image_size, image_format):
        if not path.exists(models_directory):
            raise Exception(f'model directory doesn\'t exist at {models_directory}')
        if image_format is None:
            raise Exception(f'image_format is None')
        self.model = model
        self.model_type = model_type
        self.directory_path = models_directory
        self.image_size = image_size
        self.image_format = image_format
        self.nb_epochs = nb_epochs

    def save(self):
        file_path = f'{self.directory_path}/' \
                    f'model(type={self.model_type.name},epochs={self.nb_epochs},' \
                    f'image_size={self.image_size},image_format={self.image_format.name})' \
                    f'.keras'
        self.model.save(file_path)
