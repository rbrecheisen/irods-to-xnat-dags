FROM apache/airflow:2.1.0
ADD requirements.txt /opt/airflow/requirements.txt
WORKDIR /opt/airflow
RUN pip install --no-cache-dir --user -r requirements.txt
