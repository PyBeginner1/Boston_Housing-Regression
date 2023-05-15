import pandas as pd
import numpy as np
import sys
from flask import Flask, request, render_template
import os

from src.exception import CustomException
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

ROOT_DIR = os.getcwd()
PREPROCESSOR_DIR = 'artifact\data_transformation'
MODEL_DIR = 'artifact\model_trainer'
preprocessor = 'preprocessor_object.pkl'
model = 'model.pkl'

PREPROCESSOR_PATH = os.path.join(ROOT_DIR, PREPROCESSOR_DIR, preprocessor)
MODEL_PATH = os.path.join(ROOT_DIR, MODEL_DIR, model)

application = Flask(__name__)
app = application


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict_api():
    try:
        if request.method=='GET':
            return render_template('home.html')
        else:
            data=CustomData(
                        CRIM=request.form.get('crim'),
                        ZN=request.form.get('zn'),
                        INDUS=request.form.get('indus'),
                        CHAS=request.form.get('chas'),
                        NOX=request.form.get('nox'),
                        RM=request.form.get('rm'),
                        AGE=request.form.get('age'),
                        DIS=request.form.get('dis'),
                        RAD=request.form.get('rad'),
                        TAX=request.form.get('tax'),
                        PTRATIO=request.form.get('ptratio'),
                        B=request.form.get('b'),
                        LSTAT=request.form.get('lstat')
            )
            
            df=data.get_data_as_dataframe()
            predict_pipeline=PredictPipeline(model_path = MODEL_PATH, preprocessor_path = PREPROCESSOR_PATH)
            final_result=predict_pipeline.prediction(df)
            return render_template('home.html', result=round(final_result[0],3))

    except Exception as e:
        raise CustomException(e,sys)


if __name__=='__main__':
    app.run(debug = True, host = "0.0.0.0")