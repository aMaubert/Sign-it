from os import path
from tensorflow.keras.models import load_model

from app.model.type import Type
from app.image.format import Format as ImageFormat


class Loader:
    def __init__(self, models_directory, model_type, image_size, image_format):
        if not path.exists(models_directory):
            raise Exception(f'models directory not found'
                            f' at {models_directory}')

        self.models_directory = models_directory
        self.model_type=model_type
        self.image_size = image_size
        self.image_format = image_format

    def load(self):
        file_path = f'{self.models_directory}/' \
                    f'{Type.to_str(self.model_type)}.keras'
        file_path = f'{self.models_directory}/model({Type.to_str(self.model_type)})' \
                    f'_image(size({self.image_size})_format({ImageFormat.to_str(self.image_format)})).keras'
        return load_model(file_path)
