import pandas as pd
import numpy as np
import sys
from flask import Flask, request, render_template

from src.exception import CustomException
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)


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
            print(df)
            predict_pipeline=PredictPipeline()
            final_result=predict_pipeline.prediction(df)
            print(final_result)
            return render_template('home.html', result=round(final_result[0],3))

    except Exception as e:
        raise CustomException(e,sys)


if __name__=='__main__':
    app.run(host="0.0.0.0")