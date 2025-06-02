import sys
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator

from docker.types import Mount


from datetime import datetime,timedelta


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 10, 1),
    "retries": 1,
    "catchup": False,
}

with DAG(
    dag_id="dbt_orchestrator",
    description="Orchestrator for Weather API DAGs",
    tags=["weather_api", "orchestrator","dbt"],
    schedule=timedelta(minutes=5),
    default_args=default_args,
) as dag:



    dbt_transformations = DockerOperator(
        task_id="dbt_transformations",
        image="ghcr.io/dbt-labs/dbt-postgres:latest",
        command="run",
        working_dir="/usr/app",
        mounts=[
            Mount(
                source="/home/realelvo/Desktop/Projects/weather_data_project/dbt/dbt_proj",
                target="/usr/app",
                type="bind",
            ),
            Mount(
                source="/home/realelvo/Desktop/Projects/weather_data_project/dbt/profiles.yml",
                target="/root/.dbt/profiles.yml",
                type="bind",
            ),
        ],
        network_mode="weather_data_project_my_network",
        docker_url="unix://var/run/docker.sock",
        auto_remove='success'
    )

dbt_transformations
