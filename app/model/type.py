from enum import Enum


class Type(Enum):
    LinearModel = 'LINEAR'

    @staticmethod
    def from_str(label):
        if label == 'LINEAR':
            return Type.LinearModel
        return None
