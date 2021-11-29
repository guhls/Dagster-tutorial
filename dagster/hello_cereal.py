# Biblioteca que possibilita a busca de arquivos em um caminho
import requests

# Conseguir manipular dados em arquivos CSV
import csv, pandas as pd

from dagster import job, op
from requests.models import Response

response = requests.get("https://docs.dagster.io/assets/cereal.csv")

@op
def hello_cereal(context):
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(cereals)} cereals")

    return cereals

@op
def show_cereals_head(context):
     cereals = pd.read_csv("assets/cereal.csv")
     cereals.head()

@op
def show_cereals_tail(context):
    cereals = pd.read_csv("assets/cereal.csv")
    context.log.info(cereals.tail())


@job
def hello_cereal_job():
    hello_cereal()
    show_cereals_head()
    show_cereals_tail()

if __name__ == "__main__":
    result = hello_cereal_job.execute_in_process()