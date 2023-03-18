from src.logger import logging
from src.exception import CustomException
from src.config import ConfigurationManager
from src.components import ModelTrainer

STAGE_NAME = "Model Trainer"

def main():
    config=ConfigurationManager()
    model_trainer_config=config.get_model_trainer_config()
    model_trainer=ModelTrainer(config=model_trainer_config)
    model_trainer.train_model()


if __name__=='__main__':
    try:
        logging.info(f"\n{'-'*75}")
        logging.info(f"\n\n>>>>>> {STAGE_NAME} stage started <<<<<<")
        main()
        logging.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)