import sys
from airflow import DAG
from airflow.operators.python import PythonOperator


from datetime import datetime,timedelta


sys.path.append("/opt/airflow/weather_api")

from insert_records import main


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 10, 1),
    "retries": 1,
    "catchup": False,
}

with DAG(
    dag_id="weather_api_orchestrator",
    description="Orchestrator for Weather API DAGs",
    tags=["weather_api", "orchestrator"],
    schedule=timedelta(minutes=5),
    default_args=default_args,
) as dag:


    ingest_records_task = PythonOperator(
        task_id="ingest_weather_data",
        python_callable=main,
        dag=dag
    )

    ingest_records_task