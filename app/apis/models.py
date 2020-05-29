import os
from json import JSONEncoder
from flask_restplus import Namespace, Resource
from flask import Response

from app.apis.dtos.model import ModelDto
from app.config import Config
from app.model.type import Type as ModelType

config = Config()
config.load_config()

json_encoder = JSONEncoder()

models_namespace = Namespace('models', description='models operations')

keras_model_extension = '.keras'
headers = { 'content-type' : 'application/json'}


def parse_file_name(file: str):
    split = file.split('model(')
    model_split = ''.join(split).split(')', maxsplit=1)

    model_type = model_split[0]

    image_split = ''.join(model_split).split(f'{model_type}_image(')
    image_size_split = ''.join(image_split).split('size(')
    image_size_split = ''.join(image_size_split).split(')', maxsplit=1)
    image_size_split = ''.join(image_size_split).split('_format')

    image_size = image_size_split[0]

    image_format_split = ''.join(image_size_split).split(f'{image_size}(')
    image_format_split = ''.join(image_format_split).split(')')

    image_format = image_format_split[0]

    image_size = ''.join(''.join(image_size.split('(')).split(')')).split(', ')
    image_size = tuple(map(int, image_size))

    return ModelDto(type=ModelType(model_type), image_size=image_size,
                    image_format=image_format)


@models_namespace.route('/')
class Models(Resource):

    def get(self):
        keras_models = []
        for file in os.listdir(config.models_directory):
            if file.endswith(keras_model_extension):
                model_dto = parse_file_name(file=file)
                model_json_format = json_encoder.encode(model_dto.serialize())
                keras_models.append(model_json_format)

        return Response(keras_models, status=200, headers=headers)
