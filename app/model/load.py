from os import path
from tensorflow.keras.models import load_model

from app.apis.dtos.model import ModelDto
from app.model.type import Type as ModelType
from app.image.format import Format as ImageFormat


class Loader:
    def __init__(self, models_directory, model_type, nb_epochs, image_size, image_format):
        if not path.exists(models_directory):
            raise Exception(f'models directory not found'
                            f' at {models_directory}')
        self.models_directory = models_directory
        self.model_type = model_type
        self.nb_epochs = nb_epochs
        self.image_size = image_size
        self.image_format = image_format

    def load(self):
        file_name = f'model(type={self.model_type.value},' \
                    f'epochs={self.nb_epochs},' \
                    f'image_size={self.image_size},' \
                    f'image_format={self.image_format.value})' \
                    f'.keras'
        file_path = f'{self.models_directory}/{file_name}'
        if not path.exists(file_path):
            raise Exception(f'model does not exist for : '
                            f'model(type={self.model_type.value},'
                            f'epochs={self.nb_epochs},'
                            f'image_size={self.image_size},'
                            f'image_format={self.image_format.value})')
        return load_model(file_path)

    @staticmethod
    def load_model_dto_from_file_name(file_name: str):
        file_name = file_name.replace(', ', 'x')
        each_properties = file_name.split('(', maxsplit=1)[1].rsplit(')', maxsplit=1)[0].split(',')

        model_type = each_properties[0].split('=')[1]
        nb_epochs = int(each_properties[1].split('=')[1])
        image_size = each_properties[2].split('=')[1]
        image_format = each_properties[3].split('=')[1]

        image_sizes = image_size.split('x')
        width = image_sizes[0].split('(')[1]
        height = image_sizes[1].split(')')[0]
        image_size = (int(width), int(height))

        return ModelDto(type=ModelType(model_type), nb_epochs=nb_epochs,
                        image_size=image_size, image_format=image_format)

    @staticmethod
    def load_model_from_dto(models_directory: str, model_dto: ModelDto):
        file_name = f'model(type={model_dto.type.value},' \
                    f'epochs={model_dto.nb_epochs},' \
                    f'image_size={model_dto.image_size},' \
                    f'image_format={ImageFormat.to_str(model_dto.image_format)})' \
                    f'.keras'
        file_path = f'{models_directory}/{file_name}'
        return load_model(file_path)
