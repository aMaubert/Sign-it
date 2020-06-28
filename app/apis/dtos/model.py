class ModelDto:

    def __init__(self, type,nb_epochs, image_size, image_format):
        self.type = type
        self.nb_epochs = nb_epochs
        self.image_size = image_size
        self.image_format = image_format

    def serialize(self):
        return {'type': self.type.value, 'nb_epochs' : self.nb_epochs,
                'image_size': self.image_size, 'image_format': self.image_format}

    # @staticmethod
    # def deserialize(json):

    def __repr__(self):
        return f'ModelDto( type : {self.type.value}, nb_epochs : {self.nb_epochs},' \
               f' image_size : {self.image_size}, image_format: {self.image_format})'
