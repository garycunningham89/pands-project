#Gary Cunningham - GMIT - G00376467.
#Programming and Scripting Final Project - Submission on 28/04.19
import pandas as pd
#Using Pandas to view the complete table from a CSV file and then printing the data out in one output.
data = pd.read_csv('iris_csv.csv')
#Using pandas to get some info on the table firstly.
print(data) # shows entire data set. 
print(data.head()) #shows first 5 rows of the data set.
print(data.tail()) #shows last 5 rows of the dataset.
print(data.describe()) #gives a statisticcal summary of the dataset.
print(data.shape) #tells amounts of rows and columns in format: (rows, columns)
print(data.columns) #gives output of the columns headers and the 'dtype'.
print(data["class"].value_counts()) #separates the column class and gives output of each as well as the dtype as int64.
#Adapted from Tutorials Point Processing CSV Data source accessed at: https://www.tutorialspoint.com/python/python_processing_csv_data.htm
#Adapted from class content and Pandas website for the purpose of this project.

#Testing and Learning how to import CSV files and export each column separately for analysis.
#adapted from: https://www.programiz.com/python-programming/reading-csv-filesimport csv
#how to open the dataset
#with open('iris_csv.csv', 'r') as csvFile:
#    reader = csv.reader(csvFile)
#    for row in reader:
#        print(row)
#csvFile.close()

#Testing the ouput of single column outputs using programs adapted frm programiz
#from statistics import mean, median, mode, stdev
#x = int(input("Sepal Length, Width are 0, 1. Petal Length, Width are 2, 3. Please input the row for single output: "))
#import csv
#csv.register_dialect('myDialect',
#delimiter = ',',
#quoting=csv.QUOTE_ALL,
#skipinitialspace=True)
#with open('iris_csv.csv', 'r') as f:
 #   reader = csv.reader(f, dialect='myDialect')
  #  for row in reader:
   #     print(row[x])
#Giving an input to research to dissect each variable separately, be it Sepal Length, Sepal Width, Petal Length and Petal Width.
#Allowing the user input 0, 1, 2, 3  for each respective row in the data set.