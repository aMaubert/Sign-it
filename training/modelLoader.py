from app.model.type import Type


class ModelLoader:

    def __init__(self, model_type=Type.LinearModel):
        self.model_type = model_type
