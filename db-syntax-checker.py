import csv


def check_syntax(file):
    with open(file, encoding="utf-8"):
        csv_reader = csv.reader(file, delimiter=",")
        num_cols = len(csv_reader[0])

        for row in csv_reader:
            if len(row) != num_cols:
                return "error"

        return "no error"
