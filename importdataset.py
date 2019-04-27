#Using pandas to view the complete table from a CSV file and then printing the data out in one output.
import pandas as pd
data = pd.read_csv('iris_csv.csv')
data.head()
data.info()
data.describe()
data['class'].value_counts()

print (data)
#Adapted from Tutorials Point Processing CSV Data source accessed at: https://www.tutorialspoint.com/python/python_processing_csv_data.htm

print(iris.shape)

print(iris.columns)

print(iris["class"].value_counts())

#Learning how to import CSV files and export each column separately for analysis.
#adapted from: https://www.programiz.com/python-programming/reading-csv-filesimport csv
#how to open the dataset
#with open('iris_csv.csv', 'r') as csvFile:
#    reader = csv.reader(csvFile)
#    for row in reader:
#        print(row)
#csvFile.close()

#Testing the ouput of single column outputs using programs adapted frm programiz
x = int(input("Sepal Length, Width are 0, 1. Petal Length, Width are 2, 3. Please input the row for single output: "))
import csv

csv.register_dialect('myDialect',
delimiter = ',',
quoting=csv.QUOTE_ALL,
skipinitialspace=True)

with open('iris_csv.csv', 'r') as f:
    reader = csv.reader(f, dialect='myDialect')
    for row in reader:
        print(row[x])
#Giving an input to research to dissect each variable separately, be it Sepal Length, Sepal Width, Petal Length and Petal Width.
#Allowing the user input 0, 1, 2, 3  for each respective row in the data set.