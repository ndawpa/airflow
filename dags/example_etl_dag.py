from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Dummy ETL functions
def extract():
    print("Extracting data...")

def transform():
    print("Transforming data...")

def load():
    print("Loading data...")

# Default args for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='example_etl_dag',
    default_args=default_args,
    description='A simple ETL DAG',
    schedule=timedelta(days=1),
    start_date=datetime(2025, 7, 20),
    catchup=False,
    tags=['example', 'etl'],
) as dag:

    # Define tasks
    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load,
    )

    # Set task dependencies
    extract_task >> transform_task >> load_task
