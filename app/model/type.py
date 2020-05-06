from enum import Enum


class Type(Enum):
    LinearModel = 'LINEAR'

    @staticmethod
    def from_str(label):
        if label == 'LINEAR':
            return Type.LinearModel
        return None

    @staticmethod
    def to_str(model_type):
        if model_type == Type.LinearModel:
            return 'linear'
        return None
