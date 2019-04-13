import pandas as pd
#https://www.tutorialspoint.com/python/python_processing_csv_data.htm
data = pd.read_csv('iris_csv.csv')

from statistics import mean, median, mode, stdev

avg_value = mean(data[0:150]['petalwidth'])
median_value = median(data[0:150]['petalwidth'])
mode_value = mode(data[0:150]['petalwidth'])
std_dev = stdev(data[0:150]['petalwidth'])
max_value = max(data[0:150]['petalwidth'])
min_value = min(data[0:150]['petalwidth'])
print(std_dev)
print(avg_value)
print(median_value)
print(mode_value)
print(max_value)
print(min_value)

#RANGE
#print([min(data[0:150]['petalwidth']),max(data[0:150]['petalwidth'])])
#print([min(data[0:150]['petallength']),max(data[0:150]['petallength'])])
#print([min(data[0:150]['sepalwidth']),max(data[0:150]['sepalwidth'])])
#print([min(data[0:150]['sepalwidth']),max(data[0:150]['sepalwidth'])])
