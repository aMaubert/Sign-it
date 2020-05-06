from app.model.type import Type
from os import path


class Saver:

    def __init__(self, model, models_directory, model_type):
        if not path.exists(models_directory):
            raise Exception(f'model directory doesn\'t exist at {models_directory}')
        self.model = model
        self.model_type = model_type
        self.directory_path = models_directory

    def save(self):
        file_path = f'{self.directory_path}/{Type.to_str(self.model_type)}.keras'
        self.model.save(file_path)
