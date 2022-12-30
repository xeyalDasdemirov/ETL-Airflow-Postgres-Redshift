# ETL-Airflow-Postgres-Redshift
ETL process with Airflow from Postgres to Redshift

I will describe how we can load data from Postgres to Redhsift using Amazon Managed Airflow 

1. Firstly, we need to create RDS Postgres DB and restore sample database. I restored sample DB from https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/

2. Create Amazon MWAA usng following this link: https://catalog.us-east-1.prod.workshops.aws/workshops/795e88bb-17e2-498f-82d1-2104f4824168/en-US/workshop-2-2-2/setup/mwaa

3. Create Redshift cluster https://catalog.us-east-1.prod.workshops.aws/workshops/795e88bb-17e2-498f-82d1-2104f4824168/en-US/workshop-2-2-2/setup/redshift

4. 
