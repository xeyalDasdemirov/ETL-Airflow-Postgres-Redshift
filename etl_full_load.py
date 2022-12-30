from airflow import DAG, settings
 
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.jobs.base_job import BaseJob
from airflow.models import DAG, DagModel, DagRun, ImportError, Log, SlaMiss, RenderedTaskInstanceFields, TaskFail, TaskInstance, TaskReschedule, Variable, XCom
from airflow import DAG
from datetime import datetime
from datetime import timedelta
import os


default_args = {
    'owner': 'aws',
    'depends_on_past': False,
    'start_date': datetime(2019, 2, 20),
    'provide_context': True
}

dag = DAG(
    'etl_full_load', default_args=default_args, schedule_interval=None)



 
def extract_postgres_full_fn(**kwargs):

    import psycopg2
    import csv
    import boto3
    import configparser

    dbname = "postgres_dbname"
    user = "postgres_username"
    password = "postgres_password"
    host = "postgres_host"
    port = "postgres_port"

    conn = psycopg2.connect(
        "dbname=" + dbname
        + " user=" + user
        + " password=" + password
        + " host=" + host,
        port = port)

    m_query = "SELECT * FROM customer;"
    local_filename = "customer.csv"

    m_cursor = conn.cursor()
    m_cursor.execute(m_query)
    results = m_cursor.fetchall()

    with open(local_filename, 'w') as fp:
        csv_w = csv.writer(fp, delimiter='|')
        csv_w.writerows(results)

    fp.close()
    m_cursor.close()
    conn.close()

# # load the aws_boto_credentials values

    access_key = "aws_access_key"
    secret_key = "aws_access_key"
    bucket_name = "your_bucketname"

    s3 = boto3.client(
         's3',
         aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    s3_file = local_filename

    s3.upload_file(
     local_filename,
     bucket_name,
     s3_file)
 
    return "OK"






def load_to_redshift_fn(**kwargs):

    import boto3
    import configparser
    import psycopg2

    r_dbname = "redshift_dbname"
    r_user = "redshift_username"
    r_password = "redshift_password"
    r_host = "redshift_host"
    r_port = "redshift_port"

    # connect to the redshift cluster
    rs_conn = psycopg2.connect(
    "dbname=" + dbname
    + " user=" + user
    + " password=" + password
    + " host=" + host
    + " port=" + port)

    account_id = "aws_account_id"
    iam_role = "redshift_role"
    bucket_name = "your_bucketname"

    # run the COPY command to load the file into Redshift
    file_path = ("s3://"
    + bucket_name
    + "/customer.csv")
    role_string = ("arn:aws:iam::"
    + account_id
    + ":role/" + iam_role)

    sql = "COPY public.customer"
    sql = sql + " from %s "
    sql = sql + " iam_role %s;"

    # create a cursor object and execute the COPY command
    cur = rs_conn.cursor()
    cur.execute(sql,(file_path, role_string))

    # close the cursor and commit the transaction
    cur.close()
    rs_conn.commit()

    # close the connection
    rs_conn.close()

    return "OK"


extract_postgres_full = PythonOperator(
    task_id='extract_postgres_full',
    python_callable=extract_postgres_full_fn,
    dag=dag,
    )

load_to_redshift = PythonOperator(
    task_id='load_to_redshift',
    python_callable=load_to_redshift_fn,
    dag=dag,
    )

extract_postgres_full >> load_to_redshift
 


