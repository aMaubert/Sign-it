import os
from json import JSONEncoder
from flask_restplus import Namespace, Resource
from flask import Response

from app.model.load import Loader as ModelLoader
from app.config import Config

config = Config()
config.load_config()

json_encoder = JSONEncoder()

models_namespace = Namespace('models', description='models operations')

keras_model_extension = '.keras'
headers = {'content-type' : 'application/json'}


@models_namespace.route('/')
class Models(Resource):

    def get(self):
        models = []
        for file in os.listdir(config.models_directory):
            if file.endswith(keras_model_extension):
                model_dto = ModelLoader.load_model_dto_from_file_name(file_name=file)
                models.append(model_dto.serialize())
        return Response(json_encoder.encode(models), status=200, headers=headers)
