import sys
import pandas as pd
import os
from pathlib import Path

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

CURRENT_DIR = os.getcwd()


class PredictPipeline:
    def __init__(self, model_path, preprocessor_path):
        try:
            self.model_path = model_path
            self.preprocessor_path = preprocessor_path
        except Exception as e:
            logging.error(f"Error: {e}")
            raise CustomException(e,sys)

    def prediction(self, features):
        try:
            logging.info('Prediction has begun')
            model=load_object(self.model_path)
            preprocessor=load_object(self.preprocessor_path)
            scaled_data=preprocessor.transform(features)
            prediction=model.predict(scaled_data)
            return prediction
        except Exception as e:
            logging.error(f"Error: {e}")
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,CRIM:int,
                ZN:int,INDUS:int,
                CHAS:int,NOX:int,
                RM:int,AGE:int,
                DIS:int,RAD:int,
                TAX:int,PTRATIO:int,
                B:int,LSTAT:int):
        try:
            logging.info('Data has been received')
            self.CRIM=CRIM
            self.ZN=ZN
            self.INDUS=INDUS
            self.CHAS=CHAS
            self.NOX=NOX
            self.RM=RM
            self.AGE=AGE
            self.DIS=DIS
            self.RAD=RAD
            self.TAX=TAX
            self.PTRATIO=PTRATIO
            self.B=B
            self.LSTAT=LSTAT
        except Exception as e:
            logging.info(e)
            raise e
        
    def get_data_as_dataframe(self):
        try:
            logging.info('Converting the received data into dataframe')
            custom_data_input_dict={
            "CRIM":[self.CRIM],
            "ZN":[self.ZN],
            "INDUS":[self.INDUS],
            "CHAS":[self.CHAS],
            "NOX":[self.NOX],
            "RM":[self.RM],
            "AGE":[self.AGE],
            "DIS":[self.DIS],
            "RAD":[self.RAD],
            "TAX":[self.TAX],
            "PTRATIO":[self.PTRATIO],
            "B":[self.B],
            "LSTAT":[self.LSTAT]
            }
            column_names = [
            "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", 
            "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
        ]
            return pd.DataFrame(custom_data_input_dict,columns=column_names)
        except Exception as e:
            logging.error(f"Failed to convert input data to DataFrame: {e}")
            raise CustomException(e,sys)
                
