import dill
import os
import json
import pandas as pd


def predict():
    m = os.listdir('/home/nikita/airflow_hw/data/models')
    filename = f'/home/nikita/airflow_hw/data/models/{m[0]}'
    with open(filename, 'rb') as file:
        model = dill.load(file)
        predictions = list()
        for predict_data in os.listdir('/home/nikita/airflow_hw/data/test'):
            f = open(f'/home/nikita/airflow_hw/data/test/{predict_data}')
            data = json.load(f)
            df = pd.DataFrame([data])
            predictions.append(model.predict(df))
        df_main = pd.DataFrame(predictions, columns=['predictions'])
        df_main.to_csv('/home/nikita/airflow_hw/data/predictions/predictions.csv')


if __name__ == '__main__':
    pass

