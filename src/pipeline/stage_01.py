from src.components.data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager
from src.logger import logging


STAGE_NAME = "Data Ingestion"

def main():
    try:
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        component=DataIngestion(config=data_ingestion_config)
        train, test = component.initiate_data_ingestion()
    except Exception as e:
        logging.info(f'Error: {e}')
        raise e
    

if __name__ == "__main__":
    try:
        logging.info(f"\n{'-'*75}")
        logging.info(f"\n\n>>>>>> {STAGE_NAME} stage started <<<<<<")
        main()
        logging.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e
