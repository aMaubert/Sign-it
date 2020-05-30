from enum import Enum


class Type(Enum):
    LinearModel = 'LINEAR'
    MLPModel = 'MLPModel'

    @staticmethod
    def from_str(label):
        print('to format : ' + label)
        if label == 'LinearModel':
            return Type.LinearModel
        elif label == 'MLPModel' :
            return Type.MLPModel
        return None

    @staticmethod
    def to_str(model_type):
        if model_type == Type.LinearModel:
            return 'LinearModel'
        elif model_type == Type.MLPModel:
            return 'MLPModel'
        return None
