from dataclasses import dataclass
from pathlib import Path
import os

from src.logger import logging
from src.utils import create_directories
from src.entity import DataIngestionConfig
from src.config.configuration import ConfigurationManager

import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split


'''@dataclass(frozen=True)
class DataIngestionConfig:
  root_dir: str = 'artifact/data_ingestion'
  raw_data_path: str = 'artifact/data_ingestion/raw.csv'
  train_data_path: str = 'artifact/data_ingestion/train.csv'
  test_data_path: str = 'artifact/data_ingestion/test.csv'''

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion started')
        try:
            create_directories([self.config.root_dir])

            df = fetch_openml(name='boston')
            X, y = df.data, df.target
            
            new_df= pd.concat([X,y], axis=1)
            new_df.to_csv(self.config.raw_data_path, index=False, header=True)
            logging.info(f'Raw data stored at: [{self.config.raw_data_path}]')

            logging.info('Train and Test split initiated.')
            train, test = train_test_split(new_df, test_size=0.2, random_state=1)

            train.to_csv(self.config.train_data_path, index=False, header=True)
            test.to_csv(self.config.test_data_path, index=False, header=True)

            logging.info('Data Ingestion completed')
            logging.info('\n')
            return self.config.train_data_path, self.config.test_data_path
        except Exception as e:
            logging.info(f'Error: {e}')
            raise e
        

