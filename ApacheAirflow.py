import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# load the dataset
data = pd.read_csv('screentime_analysis.csv')

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# define the data preprocessing function
def preprocess_data():
    file_path = 'screentime_analysis.csv'
    data = pd.read_csv(file_path)

    data['Date'] = pd.to_datetime(data['Date'])
    data['DayOfWeek'] = data['Date'].dt.dayofweek
    data['Month'] = data['Date'].dt.month

    data = data.drop(columns=['Date'])

    data = pd.get_dummies(data, columns=['App'], drop_first=True)

    scaler = MinMaxScaler()
    data[['Notifications', 'Times Opened']] = scaler.fit_transform(data[['Notifications', 'Times Opened']])

    preprocessed_path = 'preprocessed_screentime_analysis.csv'
    data.to_csv(preprocessed_path, index=False)
    print(f"Preprocessed data saved to {preprocessed_path}")

# define the DAG
dag = DAG(
    dag_id='data_preprocessing',
    schedule_interval='@daily',
    start_date=datetime(2025, 1, 1),
    catchup=False,
)

# define the task
preprocess_task = PythonOperator(
    task_id='preprocess',
    python_callable=preprocess_data,
    dag=dag,
)