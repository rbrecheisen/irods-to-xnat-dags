import airflow

from airflow import DAG
from airflow.operators.bash import BashOperator


bash_cmd = 'curl -o /tmp/launches.json -L \'https://ll.thespacedevs.com/2.0.0/launch/upcoming\''


with DAG(dag_id='rockets',
         start_date=airflow.utils.dates.days_ago(14), schedule_interval=None) as dag:
    download = BashOperator(task_id='download',
                            bash_command=bash_cmd)
    notify = BashOperator(task_id='notify',
                          bash_command='echo \'download ok\'')
    download >> notify
