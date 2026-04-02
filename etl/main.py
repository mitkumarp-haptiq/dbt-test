# use prefect to run the etl pipeline
from prefect import flow, task
from extract import extract_data
from load import load_data

@task
def extract_task():
    return extract_data()

@task
def load_task(data):
    load_data(data)

@flow
def etl_pipeline():
    data = extract_task()
    load_task(data)