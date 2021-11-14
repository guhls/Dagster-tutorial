# Biblioteca que possibilita a busca de arquivos em um caminho
import requests

# Conseguir manipular dados em arquivos CSV
import csv

from dagster import job, op

@op
def hello_cereal(context):
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    cereals = [row for row in csv.DictReader(lines)]
    context.log.info(f"Found {len(cereals)} cereals")

    return cereals

@job
def hello_cereal_job():
    hello_cereal()

if __name__ == "__main__":
    result = hello_cereal_job.execute_in_process()