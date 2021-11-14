from dagster import job, op

@op
def returnFive():
    return 5

@op
def plusOne(arg):
    return arg + 1

@job
def doStuff():
    plusOne(returnFive())


if __name__ == "__main__":
    result = doStuff.execute_in_process()
