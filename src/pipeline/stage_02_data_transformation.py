import os
import sys

os.environ['PYTHONPATH'] = 'D:\iNeuron\Complete Project\Boston-Regression\Boston_Housing-Regression\src'

from src.config import ConfigurationManager
from src.components.data_transformation import DataTransformation
from src.logger import logging
from src.exception import CustomException


STAGE_NAME = "Data Transformation"

train_path = r'Boston_Housing-Regression\artifact\data_ingestion\train.csv'
test_path = r'Boston_Housing-Regression\artifact\data_ingestion\test.csv'

#final_train_path = os.path.join(os.path.dirname(os.getcwd()), train_path)
#final_test_path = os.path.join(os.path.dirname(os.getcwd()), test_path)

def main():
    try:
        config=ConfigurationManager()
        data_transforamtion_config=config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transforamtion_config, train_path=train_path, test_path=test_path)
        data_transformation.initiate_data_transformation()
    except Exception as e:
        raise CustomException(e,sys)


if __name__=='__main__':
    try:
        logging.info(f"\n{'-'*75}")
        logging.info(f"\n\n>>>>>> {STAGE_NAME} stage started <<<<<<")
        main()
        logging.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise CustomException(e,sys)
