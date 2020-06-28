import json
import uuid
import os

from PIL import Image
from flask import Response, request
from flask_restplus import Namespace, Resource
from app.config import Config
from app.apis.dtos.model import ModelDto
from app.image.format import Format as ImageFormat, Format
from app.model.load import Loader as ModelLoader
from app.model.type import Type as ModelType
import numpy as np

predict_namespace = Namespace('predict', description='predict operations')

# Here an Example to load a Model from his caracteristics
#
# config = Config()
# config.load_config()
#
# model_dto = ModelDto(type=ModelType.MLPModel, nb_epochs=5, image_size=(64, 64),
#                      image_format=ImageFormat.RGB)
# model = ModelLoader.load_model_from_dto(models_directory=config.models_directory,
#                                 model_dto=model_dto)
# print(model)

config = Config()
config.load_config()


def image_format(image_format):
    if image_format == 'GrayScale' :
        return ImageFormat.GrayScale
    return ImageFormat(image_format)

@predict_namespace.route("/")
class Predict(Resource):

    def post(self):
        """
        :return:
        """
        file_name = str(uuid.uuid4()) + '.jpg'
        f = open(file_name, "wb")
        f.write(request.data)
        f.close()


        model_type = request.args.get('type')
        model_nb_epochs = request.args.get('nb_epochs')
        model_image_size = str(request.args.get('image_size')).replace('(', '').replace(')', '').split(',')
        model_image_format = request.args.get('image_format')

        model_image_size = tuple([int(each_size) for each_size in model_image_size])

        model_dto = ModelDto(type=ModelType(model_type), nb_epochs=model_nb_epochs,
                             image_size=model_image_size, image_format=image_format(model_image_format))
        model = ModelLoader.load_model_from_dto(models_directory=config.models_directory,
                                                model_dto=model_dto)

        image = Image.open(file_name)
        image = image.resize(model_dto.image_size).convert(Format.to_str(model_dto.image_size))

        images_to_predict = [np.array(image) / 255]
        predictions = model.predict(np.array(images_to_predict))
        predictions = [str(eachPrediction * 100) for eachPrediction in predictions[0]]

        response_data = {}
        for i in range(len(config.categories)):
            response_data[config.categories[i]] = predictions[i]

        os.remove(file_name)

        return Response(json.dumps(response_data), status=200, mimetype='application/json')
