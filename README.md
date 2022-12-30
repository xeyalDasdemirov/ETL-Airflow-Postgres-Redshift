# ETL-Airflow-Postgres-Redshift
ETL process with Airflow from Postgres to Redshift

I will describe how we can load data from Postgres to Redhsift using Amazon Managed Airflow 

1. Firstly, we need to create RDS Postgres DB and restore sample database. I restored sample DB from https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/

2. Create Amazon MWAA usng following this link: https://catalog.us-east-1.prod.workshops.aws/workshops/795e88bb-17e2-498f-82d1-2104f4824168/en-US/workshop-2-2-2/setup/mwaa

3. Create Redshift cluster https://catalog.us-east-1.prod.workshops.aws/workshops/795e88bb-17e2-498f-82d1-2104f4824168/en-US/workshop-2-2-2/setup/redshift

4. I prepared 2 dag files: etl_full_load.py and etl_incremental_load.py. And I added to my S3 Dag folder.


<img width="1511" alt="1" src="https://user-images.githubusercontent.com/28351206/210112499-3a968391-ffda-4d62-8715-6073444312f8.png">


<img width="1511" alt="2" src="https://user-images.githubusercontent.com/28351206/210112519-77203f5d-2219-42d0-9301-b16db6e9082b.png">
