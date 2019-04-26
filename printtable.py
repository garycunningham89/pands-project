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