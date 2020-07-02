from enum import Enum


class Format(Enum):
    RGB = 'RGB'
    RGBA = 'RGBA'
    GrayScale = 'L'
    OneBitPixel = '1'
    HeightBitPixelsMappedColor = 'P'
    CMYK = 'CMYK'
    YCbCr = 'YCbCr'
    LAB = 'LAB'
    HSV = 'HSV'
    SignedIntegerPixels = 'I'
    FloatingPointPixels = 'F'

    @staticmethod
    def from_str(label):
        if label == 'RGB':
            return Format.RGB
        elif label == 'RGBA':
            return Format.RGBA
        elif label == 'GrayScale':
            return Format.GrayScale
        elif label == '1':
            return Format.OneBitPixel
        elif label == 'P':
            return Format.HeightBitPixelsMappedColor
        elif label == 'CMYK':
            return Format.CMYK
        elif label == 'YCbCr':
            return Format.YCbCr
        elif label == 'LAB':
            return Format.LAB
        elif label == 'HSV':
            return Format.HSV
        elif label == 'I':
            return Format.SignedIntegerPixels
        elif label == 'F':
            return Format.FloatingPointPixels
        return None

    @staticmethod
    def to_str(image_format):
        if image_format == Format.RGB:
            return 'RGB'
        if image_format == Format.RGBA:
            return 'RGBA'
        elif image_format == Format.GrayScale:
            return 'GrayScale'
        elif image_format == Format.OneBitPixel:
            return '1'
        elif image_format == Format.HeightBitPixelsMappedColor:
            return 'P'
        elif image_format == Format.CMYK:
            return 'CMYK'
        elif image_format == Format.YCbCr:
            return 'YCbCr'
        elif image_format == Format.LAB:
            return 'LAB'
        elif image_format == Format.HSV:
            return 'HSV'
        elif image_format == Format.SignedIntegerPixels:
            return 'I'
        elif image_format == Format.FloatingPointPixels:
            return 'F'
        return None

