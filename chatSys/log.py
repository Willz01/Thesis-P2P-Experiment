import csv

fields = ['message', 'method', 'score', 'actual', 'runtime(ns)']


def log(msg, method, score, runTime):
    with open("log.csv", 'a') as f:
        writer = csv.writer(f)
        # writer.writerow(fields)

        data = [msg, method, score, "spam/ham", runTime]  # ("spam","ham")
        writer.writerow(data)
# logging.info(f"{msg} | {method} | {score} | {runTime}")
