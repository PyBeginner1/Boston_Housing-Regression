from src.utils import create_directories, read_yaml
from src.logger import logging
from src.entity.config_entity import DataIngestionConfig, DataTransformationConfig
from src.constants import CONFIG_FILE_PATH, PARMS_FILE_PATH


class ConfigurationManager:
    def __init__(self,
                 config_file_path=CONFIG_FILE_PATH,
                 params_file_path = PARMS_FILE_PATH):
        try:
            self.config = read_yaml(config_file_path)
            self.params = read_yaml(params_file_path)
            create_directories([self.config.artifacts_root])
        except Exception as e:
            raise e


    def get_data_ingestion_config(self):
        try:
            logging.info('Data Ingestion config started.')
            config = self.config.data_ingestion

            root_dir = config.root_dir
            create_directories([root_dir])

            raw_data_path = config.raw_data_path
            train_data_path= config.train_data_path
            test_data_path= config.test_data_path

            data_ingestion_config = DataIngestionConfig(
                root_dir=root_dir,
                raw_data_path=raw_data_path,
                train_data_path=train_data_path,
                test_data_path=test_data_path
            )

            logging.info(f"Data Ingestion config: [{data_ingestion_config}]")
            return data_ingestion_config
        except Exception as e:
            raise e
        
    
    def get_data_transformation_config(self):
        try:
            logging.info('Data Transformation config started.')
            config = self.config.data_transformation

            preprocessed_obj_file_path=config.preprocessed_obj_file_path
            scaled_train = config.scaled_train_path
            scaled_test = config.scaled_test_path

            data_transforamtion_config = DataTransformationConfig(
                preprocessed_obj_file_path=preprocessed_obj_file_path,
                scaled_train_path=scaled_train,
                scaled_test_path=scaled_test
            )

            return data_transforamtion_config
        except Exception as e:
            raise e