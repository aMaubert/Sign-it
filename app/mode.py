from enum import Enum


class Mode(Enum):
    Training = 'TRAINING'
    Use = 'USE'

    @staticmethod
    def from_str(label):
        if label == 'TRAINING':
            return Mode.Training
        elif label == 'USE':
            return Mode.Use
        return None
