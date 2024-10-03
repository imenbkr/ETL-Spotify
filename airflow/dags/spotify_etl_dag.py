from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl_pipeline import etl_pipeline 

def run_etl():
    etl_pipeline()

with DAG(
    'spotify_etl_pipeline',
    default_args={'owner': 'airflow', 'retries': 3},
    description='ETL pipeline for Spotify data',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
) as dag:
    run_etl_task = PythonOperator(
        task_id='run_etl',
        python_callable=run_etl,
    )
