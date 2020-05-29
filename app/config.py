import os
from dotenv import load_dotenv, find_dotenv

from app.image.format import Format
from app.mode import Mode
from app.model.type import Type

load_dotenv(find_dotenv())
ENV_VARIABLES = ['']


class Config:

    def __init__(self):
        self.mode = Mode.Training
        self.model_type = Type.LinearModel
        self.image_size = (64, 64)
        self.image_format = 'RGB'
        self.dataset_directory = './dataset'
        self.categories = []
        self.models_directory = './models'

        self.model_training_batch_size = 4
        self.model_training_nb_epoch = 20

    def load_config(self):
        self.load_mode()
        self.load_model_type()
        self.load_image_size()
        self.load_image_format()
        self.load_categories()
        self.load_dataset_directory()
        self.load_models_directory()
        self.load_model_training_nb_epoch()

    def load_mode(self):
        mode = Mode.from_str(os.getenv('MODE'))
        if mode is not None:
            self.mode = mode
        return self

    def load_image_size(self):
        image_size = os.getenv('IMAGE_SIZE')
        image_size = map(int, image_size.split(','))
        if image_size is not None:
            self.image_size = tuple(image_size)
        return self

    def load_image_format(self):
        image_format = Format.from_str(os.getenv('IMAGE_FORMAT'))
        if image_format is not None:
            self.image_format = image_format
        return self

    def load_categories(self):
        categories = os.getenv('CLASS_CATEGORIES').split(',')
        if categories is not None:
            self.categories = categories
        return self

    def load_dataset_directory(self):
        dataset_directory = os.getenv('DATASET_DIRECTORY')
        if dataset_directory is not None:
            self.dataset_directory = dataset_directory
        return self

    def load_model_type(self):
        model_type = Type.from_str(os.getenv('MODEL_TYPE'))
        if model_type is not None:
            self.model_type = model_type
        return self

    def load_models_directory(self):
        print('vnoiqdvipjqepiovbhjipdvjpoqedvbjop')
        models_directory = os.getenv('MODEL_DIRECTORY')
        print(' os.getenv(MODELS_DIRECTORY) : ' + str(models_directory))
        if models_directory is not None:
            if os.path.isdir(models_directory):
                self.models_directory = models_directory
                return None
            current_file_path = str(__file__).replace('\\\\','/')
            os.chdir(os.path.join(current_file_path, '../..'))
            self.models_directory = os.path.join(os.path.curdir, models_directory)
            if(os.path.isdir(self.models_directory)):
                return None
            raise Exception('models directory not found')
        return None

    def load_model_training_nb_epoch(self):
        model_training_nb_epoch = int(os.getenv('TRAINING_NB_EPOCH'))
        if model_training_nb_epoch is not None:
            self.model_training_nb_epoch = model_training_nb_epoch
        return None

    def load_model_training_batch_size(self):
        model_training_batch_size = int(os.getenv('TRAINING_BATCH_SIZE'))
        if model_training_batch_size is not None:
            self.model_training_batch_size = model_training_batch_size
        return None

    def __str__(self):
        return f'Config( mode={self.mode},' \
               f' model_type={self.model_type},' \
               f' image_format={self.image_format},' \
               f' image_size={self.image_size},' \
               f' categories={self.categories},' \
               f' dataset_directory={self.dataset_directory},' \
               f' models_directory={self.models_directory})'




