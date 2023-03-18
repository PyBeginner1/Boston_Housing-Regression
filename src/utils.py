from pathlib import Path
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
import os
import sys
import dill
import numpy as np

from src.logger import logging
from src.exception import CustomException

from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logging.info(e)
        raise CustomException(e,sys)
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")


@ensure_annotations
def save_obj(file_path, obj):
    try:
        with open(file_path,'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        logging.info(e)
        raise CustomException(e,sys)
    
@ensure_annotations
def eval_metrics(real, predicted):
    try:
        mae = mean_absolute_error(real, predicted)
        rmse = np.sqrt(mean_squared_error(real, predicted))
        r2 = r2_score(real, predicted)
        return mae, rmse, r2
    except Exception as e:
        logging.info(e)
        raise CustomException(e,sys)


