# ETL-Airflow-Postgres-Redshift
ETL process with Airflow from Postgres to Redshift

I will describe how we can load data from Postgres to Redhsift using Amazon Managed Airflow 

1. Firstly, we need to create RDS Postgres DB and restore sample database. I restored sample DB from https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/

2. Create Amazon MWAA usng following this link: https://catalog.us-east-1.prod.workshops.aws/workshops/795e88bb-17e2-498f-82d1-2104f4824168/en-US/workshop-2-2-2/setup/mwaa

3. Create Redshift cluster https://catalog.us-east-1.prod.workshops.aws/workshops/795e88bb-17e2-498f-82d1-2104f4824168/en-US/workshop-2-2-2/setup/redshift

And create customer tabe in the Redshift: 


CREATE TABLE "public"."customer"(customer_id integer NOT NULL encode az64,
                                 store_id    smallint NOT NULL encode az64,
                                 first_name  character varying(45) NOT NULL encode lzo,
                                 last_name   character varying(45) NOT NULL encode lzo,
                                 email       character varying(50) encode lzo,
                                 address_id  smallint NOT NULL encode az64,
                                 activebool  boolean NOT NULL,
                                 create_date date NOT NULL encode az64,
                                 last_update timestamp without time zone encode az64,
                                 active      integer encode az64,
                                 CONSTRAINT customer_pkey PRIMARY KEY(customer_id));
                                 
                                 

4. I prepared 2 dag files: etl_full_load.py and etl_incremental_load.py. And I added to my S3 Dag folder.


<img width="1511" alt="1" src="https://user-images.githubusercontent.com/28351206/210112499-3a968391-ffda-4d62-8715-6073444312f8.png">


<img width="1511" alt="2" src="https://user-images.githubusercontent.com/28351206/210112519-77203f5d-2219-42d0-9301-b16db6e9082b.png">

5. And here is my results: 

<img width="1152" alt="3" src="https://user-images.githubusercontent.com/28351206/210112669-d2a252ba-ada0-4044-9d59-547d1d95d1b0.png">
