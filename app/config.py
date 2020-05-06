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

    def load_config(self):
        self.load_mode()
        self.load_model_type()
        self.load_image_size()
        self.load_image_format()
        self.load_categories()
        self.load_dataset_directory()

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

    def __str__(self):
        return f'Config( mode={self.mode},' \
               f' model_type={self.model_type}'\
               f' image_format={self.image_format},' \
               f' image_size={self.image_size},' \
               f' dataset_directory={self.dataset_directory},' \
               f' categories={self.categories})'
