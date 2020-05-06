from os import path
from tensorflow.keras.models import load_model

from app.model.type import Type


class Loader:
    def __init__(self, models_directory, model_type):
        if not path.exists(models_directory):
            raise Exception(f'models directory not found'
                            f' at {models_directory}')

        self.models_directory = models_directory
        self.model_type=model_type

    def load(self):
        file_path = f'{self.models_directory}/' \
                    f'{Type.to_str(self.model_type)}.keras'
        return load_model(file_path)
