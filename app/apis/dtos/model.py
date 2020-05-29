class ModelDto:

    def __init__(self, type, image_size, image_format):
        self.type = type
        self.image_size = image_size
        self.image_format = image_format

    def serialize(self):
        return {'type': self.type.value, 'image_size': self.image_size,
                'image_format': self.image_format}

    def __repr__(self):
        return f'ModelDto( type : {self.type.value}, image_size : {self.image_size},' \
               f'image_format: {self.image_format})'
