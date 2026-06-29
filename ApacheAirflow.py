import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# define the data preprocessing function
def preprocess_data():
    import pandas as pd
    from sklearn.preprocessing import MinMaxScaler
    file_path= os.path.join(BASE_DIR, 'Screentime_analysis.csv')
    if not os.path.exist(file_path):
        raise FileNotFoundError(f"Input file not found: {file_path}")
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data['DayOfWeek'] = data['Date'].dt.dayofweek
    data['Month'] = data['Date'].dt.month

    data = data.drop(columns=['Date'])

    data = pd.get_dummies(data, columns=['App'], drop_first=True)

    scaler = MinMaxScaler()
    data[['Notifications', 'Times Opened']] = scaler.fit_transform(data[['Notifications', 'Times Opened']])

  out_path= os.path.join(BASE_DIR, 'preprocessed_data.csv')
  data.to_csv(out_path, index=False)
  print(f"Saved to {out_path}")

# define the DAG
dag = DAG(
    dag_id='data_preprocessing',
    schedule_interval='@daily',
    start_date=datetime(2026, 06, 29),
    catchup=False,
)

# define the task
preprocess_task = PythonOperator(
    task_id='preprocess',
    python_callable=preprocess_data,
    dag=dag,
)
