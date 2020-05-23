from flask import Response, request
from flask_restplus import Namespace, Resource
# import numpy as np
# from app.model.load import Loader as ModelLoader
# from app.model.type import Type as ModelType
# from app.dataset.loader import Loader as ImageLoader
# from PIL import Image
# import matplotlib.pyplot as plt


predict_namespace = Namespace('predict', description='predict operations')


# model_loader = ModelLoader('/Users/allan/Documents/ESGI/4AL/deep-learning/project/sign-it/models',
#                                    ModelType.LinearModel)
# model = model_loader.load()
# class_names = ['danger','obligation','prohibition']
# image_loader = ImageLoader(class_names, 'RGB',(64, 64))
#
# x_test, y_test = image_loader.load_test()
# # image = Image.open('dataset/test/danger/A1a_27.jpg')
# # x_data_test = np.array(image) / 255
# prediction = model.predict(x_test)
#
# print(f'prediction = {prediction[0]}')
#
# def plot_image( predictions_array, true_label,img):
#   plt.grid(False)
#   plt.xticks([])
#   plt.yticks([])
#
#   plt.imshow(img, cmap=plt.cm.binary)
#
#   predicted_label = np.argmax(predictions_array)
#   if predicted_label == true_label:
#     color = 'blue'
#   else:
#     color = 'red'
#
#   plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
#                                 100 * np.max(predictions_array),
#                                 class_names[true_label]),
#                                 color=color)
# plt.figure(figsize=(6,3))
# plt.subplot(1,2,1)
# plot_image( prediction[0], test_labels, test_images)

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
