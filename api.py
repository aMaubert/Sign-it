from flask import Flask
from flask_restplus import Api
from app.apis.predict import predict_namespace
from app.apis.models import models_namespace
app = Flask(__name__)

api = Api(app, version='1.0', title='Sign-It API',
          description='a Flask based API for the Sign-It Application')

api.add_namespace(predict_namespace)
api.add_namespace(models_namespace)

if __name__ == '__main__':
    app.run(port=8080)
