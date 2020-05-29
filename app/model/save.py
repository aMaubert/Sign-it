from app.model.type import Type
from os import path
from app.image.format import Format as ImageFormat


class Saver:

    def __init__(self, model, models_directory, model_type, image_size, image_format):
        if not path.exists(models_directory):
            raise Exception(f'model directory doesn\'t exist at {models_directory}')
        self.model = model
        self.model_type = model_type
        self.directory_path = models_directory
        self.image_size = image_size
        self.image_format = image_format

    def save(self):
        file_path = f'{self.directory_path}/model({Type.to_str(self.model_type)})' \
                    f'_image(size({self.image_size})_format({ImageFormat.to_str(self.image_format)})).keras'
        self.model.save(file_path)
