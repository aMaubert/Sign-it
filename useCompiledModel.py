from tensorflow.keras.models import load_model

from app.dataset.loader import Loader

if __name__ == '__main__':
    categories = ['danger', 'obligation', 'prohibition']
    dataset_loader = Loader(categories)
    (x_train, y_train), (x_test, y_test) = dataset_loader.load_dataset()

    model = load_model('linear_model_SGD.keras')
    print(f'Train Acc : {model.evaluate(x_train, y_train)[1]}')
    print(f'Test Acc : {model.evaluate(x_test, y_test)[1]}')
