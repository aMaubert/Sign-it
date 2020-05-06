from enum import Enum


class Format(Enum):
    RGB = 'RGB'
    GrayScale = ''

    @staticmethod
    def from_str(label):
        if label == 'RGB':
            return Format.RGB
        return None
