from app.config import Config

from app.mode import Mode
from app.model.trainer import Trainer

if __name__ == '__main__':
    config = Config()
    config.load_config()

    print(config)

    if config.mode == Mode.Training:
        print('Mode training')
        trainer = Trainer(config.categories, config.model_type)
        trainer.training()

    elif config.mode == Mode.Use:
        print('Mode Use')
        # Implement Training Model
