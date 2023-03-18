from sklearn.preprocessing import StandardScaler
import pandas as pd
import os

from src.logger import logging
from src.utils import save_obj
from src.config.configuration import DataTransformationConfig

train_path = r'Boston_Housing-Regression\artifact\data_ingestion\train.csv'
test_path = r'Boston_Housing-Regression\artifact\data_ingestion\test.csv'

final_train_path = os.path.join(os.path.dirname(os.getcwd()), train_path)
final_test_path = os.path.join(os.path.dirname(os.getcwd()), test_path)


class DataTransformation:
    def __init__(self, config: DataTransformationConfig, train_path, test_path):
        self.config = config
        train_path = train_path
        test_path=test_path

    def initiate_data_transformation(self):
        logging.info('Initiating Data Transformation')
        train_df = pd.read_csv(final_train_path)
        test_df = pd.read_csv(final_test_path)

        scaler = StandardScaler()
        scaled_train_df = pd.DataFrame(scaler.fit_transform(train_df), columns = train_df.columns)
        scaled_test_df = pd.DataFrame(scaler.transform(test_df), columns = test_df.columns)

        os.makedirs(os.path.dirname(self.config.preprocessed_obj_file_path), exist_ok=True)

        save_obj(self.config.preprocessed_obj_file_path, scaled_test_df)

        scaled_train_df.to_csv(self.config.scaled_train_path, index=False, header=True)
        scaled_test_df.to_csv(self.config.scaled_test_path, index=False, header=True)
        logging.info('Train and test set has been preprocessed')

        logging.info('Data Transformation completed')
        logging.info('\n')
        return self.config.scaled_train_path, self.config.scaled_test_path