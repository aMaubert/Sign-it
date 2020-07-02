import os
from json import JSONEncoder
from flask_restplus import Namespace, Resource
from flask import Response, request

from app.apis.dtos.model import ModelDto
from app.model.load import Loader as ModelLoader
from app.config import Config
from app.model.type import Type as ModelType
from app.image.format import Format as ImageFormat
from app.dataset.loader import Loader as DatasetLoader
from app.model.trainer import Trainer as ModelTrainer
from app.model.save import Saver as ModelSaver
from app.model.stats import Stats

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

    def post(self):
        print(request.json)

        image_format = request.json['image_format']
        image_size = request.json['image_size']
        model_type = request.json['type']
        nb_epochs = request.json['nb_epochs']

        image_size = tuple([ int(each_size) for each_size in image_size])
        image_format = ImageFormat.from_str(image_format)
        model_type = ModelType(model_type)

        if image_size is None or image_format is None or model_type is None or nb_epochs is None:
            return 400

        dataset_loader = DatasetLoader(config.categories, image_format, image_size)
        (x_train, y_train), (x_test, y_test) = dataset_loader.load_dataset()

        # Load existing model
        trainer = ModelTrainer(x_train, y_train, x_test, y_test,
                               model_type, config.model_training_batch_size,
                               nb_epochs)
        model, logs = trainer.training(image_size)

        print("Confusion Train Matrix After Training")
        stats = Stats(model, x_train, y_train, x_test, y_test, logs)
        stats.show_accuracy()
        stats.show_graph_accuracy()
        stats.show_graph_losses()

        model_saver = ModelSaver(model=model, models_directory=config.models_directory,
                            model_type=model_type, nb_epochs=nb_epochs,
                            image_size=image_size, image_format=image_format)
        model_saver.save()
        return Response(status=201)

@models_namespace.route('/types')
class ModelTypes(Resource):

    def get(self):
        models = [ ModelDto(type=eachModelType, nb_epochs=0, image_format=ImageFormat.RGB.name, image_size=(64,64)).serialize() for eachModelType in list(ModelType) ]
        return Response(json_encoder.encode(models), status=200, headers=headers)