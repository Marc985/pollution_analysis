from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from extract.pollution_extraction import los_angeles_pollution, tokyo_pollution, antananarivo_pollution, nairobi_pollution, lima_pollution
from transform.transform import clean_and_transform_data
from load.load_data import load_data_to_database

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


dag = DAG(
    'pollution_data_etl',
    default_args=default_args,
    description='Un DAG pour extraire, transformer et charger les données de pollution pour plusieurs villes',
    schedule_interval=timedelta(days=1), 
)

los_angeles_task = PythonOperator(
    task_id='los_angeles_pollution',
    python_callable=los_angeles_pollution,
    dag=dag,
)

tokyo_task = PythonOperator(
    task_id='tokyo_pollution',
    python_callable=tokyo_pollution,
    dag=dag,
)

antananarivo_task = PythonOperator(
    task_id='antananarivo_pollution',
    python_callable=antananarivo_pollution,
    dag=dag,
)

nairobi_task = PythonOperator(
    task_id='nairobi_pollution',
    python_callable=nairobi_pollution,
    dag=dag,
)

lima_task = PythonOperator(
    task_id='lima_pollution',
    python_callable=lima_pollution,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform_data',
    python_callable=clean_and_transform_data,
    dag=dag,
)
load_task=PythonOperator(
    task_id='load_data',
    python_callable=load_data_to_database,
    dag=dag,
)

[los_angeles_task ,tokyo_task, antananarivo_task, nairobi_task , lima_task] >> transform_task >> load_task
