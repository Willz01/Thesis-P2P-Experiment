import csv

fields = ['message', 'method', 'score', 'runtime(ms)']


def log(msg, method, score, runTime):
    with open("../logger/log.csv", 'a') as f:
        writer = csv.writer(f)
        # writer.writerow(fields)

        data = [msg, method, score, runTime]
        writer.writerow(data)
    # logging.info(f"{msg} | {method} | {score} | {runTime}")
