import csv
#https://www.programiz.com/python-programming/reading-csv-files
csv.register_dialect('myDialect',
delimiter = ',',
quoting=csv.QUOTE_ALL,
skipinitialspace=True)

with open('iris_csv.csv', 'r') as f:
    reader = csv.reader(f, dialect='myDialect')
    for row in reader:
        print(row[1])