from src.logger import logging
from src.exception import CustomException
from src.utils import eval_metrics, save_obj

import pandas as pd
from pathlib import Path


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class ModelTrainer:
    def __init__(self, config=ModelTrainerConfig):
        self.config=config

    def train_model(self):
        try:
            logging.info('Model Trainer Initiated')

            scaled_train_df = pd.read_csv(Path('artifact/data_transformation/scaled_train.csv'))
            scaled_test_df=pd.read_csv(Path('artifact/data_transformation/scaled_test.csv'))

            logging.info('Initiating Train test split')
            X_train = scaled_train_df.drop('MEDV', axis=1)
            y_train = scaled_train_df['MEDV']
            X_test = scaled_test_df.drop('MEDV', axis=1)
            y_test = scaled_test_df['MEDV']

            model = LinearRegression()
            model.fit(X_train, y_train) 
            logging.info('Model has been trained')

            trained_model_path = self.config.trained_model_path
            os.makedirs(os.path.dirname(trained_model_path), exist_ok=True)
            save_obj(trained_model_path,model)

            prediction = model.predict(X_test)

            mae, rmse, r2 = eval_metrics(y_test, prediction)

            logging.info(f"Linear Regression MAE: [{mae}], RMSE: [{rmse}], R2 Score: [{r2}]")
            return mae, rmse, r2
        except Exception as e:
            raise CustomException(e,sys)