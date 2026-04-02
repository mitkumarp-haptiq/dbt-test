# connect to postgres database
import os
from pathlib import Path

import psycopg2
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")


def connect_to_postgres():
    return psycopg2.connect(
        host=os.getenv('DBT_POSTGRES_HOST'),
        port=os.getenv('DBT_POSTGRES_PORT'),
        user=os.getenv('DBT_POSTGRES_USER'),
        password=os.getenv('DBT_POSTGRES_PASSWORD'),
        database=os.getenv('DBT_POSTGRES_DATABASE')
    )