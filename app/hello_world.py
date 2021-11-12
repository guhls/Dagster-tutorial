from dagster import job, op

@op
def get_name():
    return "dagster"

@op
def hello(context, name: str):
    context.log.info(f"Hello, {name}!")

@jop
def hello_dagster():
    hello(get_name())