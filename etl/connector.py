# connect to postgres database
import psycopg2
import os

def connect_to_postgres():
    return psycopg2.connect(
        host=os.getenv('DBT_POSTGRES_HOST'),
        port=os.getenv('DBT_POSTGRES_PORT'),
        user=os.getenv('DBT_POSTGRES_USER'),
        password=os.getenv('DBT_POSTGRES_PASSWORD'),
        database=os.getenv('DBT_POSTGRES_DATABASE')
    )