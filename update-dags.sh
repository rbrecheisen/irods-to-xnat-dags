#!/bin/bash

echo "Copying updated DAGs..."
docker cp dags irods-to-xnat-dags_airflow-webserver_1:/opt/airflow
