import os
import airflow

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from irods.session import iRODSSession
from irods.exception import CollectionDoesNotExist


params = {
    'host': '137.120.31.123',
    'port': 1247,
    'user': 'irods',
    'password': 'rods',
    'zone': 'nlmumc',
    'project': 'P000000014',
}


with DAG(dag_id='connect_to_irods',
         start_date=airflow.utils.dates.days_ago(1),
         schedule_interval=None) as dag:

    def _connect():
        session = iRODSSession(
            host=params['host'],
            port=params['port'],
            user=params['user'],
            password=params['password'],
            zone=params['zone'])
        base_url = '/{}/projects/{}'.format(params['zone'], params['project'])
        idx = 1
        while True:
            try:
                collection_path = os.path.join(base_url, 'C{:09d}'.format(idx))
                collection = session.collections.get(collection_path)
                print('Found new collection {}'.format(collection))
            except CollectionDoesNotExist:
                break
            idx += 1

    connect = PythonOperator(task_id='connect',
                             python_callable=_connect)

    notify = BashOperator(task_id='notify',
                          bash_command='echo "connection success"')

    connect >> notify
