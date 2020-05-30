from flask import Response, request
from flask_restplus import Namespace, Resource

from app.apis.dtos.model import ModelDto
from app.config import Config
from app.image.format import Format as ImageFormat
from app.model.load import Loader as ModelLoader
from app.model.type import Type as ModelType

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

@predict_namespace.route("/")
class Predict(Resource):

    def post(self):
        """
        :return:
        """
        f = open("test.jpg", "wb")
        f.write(request.data)
        f.close()
        return Response('Ok', status=200, mimetype='application/json')
