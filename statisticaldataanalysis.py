#The following templates for statistic analysis adapted from python.org tutorials were 
#used as a basis for analysis and adapted for use with the Iris Dataset.
#from statistics import mean, median, mode, stdev
#avg_value = mean(InputList)
#median_value = median(InputList)
#mode_value = mode(InputList)
#std_dev = stdev(InputList)
#max_value = max(InputList)
#min_value = min(InputList)
#Input list is predefined and the print function outputs each of the above as seen below.

import pandas as pd
#Utilizing the csv file used from the Tutorials point website at: https://www.tutorialspoint.com/python/python_processing_csv_data.htm
data = pd.read_csv('iris_csv.csv')
#Allowing reading of the CSV file.
pw ='petalwidth'
pl = 'petallength'
sw = 'sepalwidth'
sl = 'sepallength'
#Shortening the names of each column for easier code. 
from statistics import mean, median, mode, stdev
avg_value1 = mean(data[0:150][pw])
avg_value2 = mean(data[0:150][pl])
avg_value3 = mean(data[0:150][sw])
avg_value4 = mean(data[0:150][sl])
print(avg_value1, avg_value2, avg_value3, avg_value4)
#Finding the average value of each variable in the data set.
median_value1 = median(data[0:150][pw])
median_value2 = median(data[0:150][pl])
median_value3 = median(data[0:150][sw])
median_value4 = median(data[0:150][sl])
print(median_value1, median_value2, median_value3, median_value4)
#Finding the median value of each variable in the data set.
mode_value1 = mode(data[0:150][pw])
mode_value2 = mode(data[0:150][pl])
mode_value3 = mode(data[0:150][sw])
mode_value4 = mode(data[0:150][sl])
print(mode_value1, mode_value2, mode_value3, mode_value4)
#Finding the mode value of each variable in the data set.
std_dev1 = stdev(data[0:150][pw])
std_dev2 = stdev(data[0:150][pl])
std_dev3 = stdev(data[0:150][sw])
std_dev4 = stdev(data[0:150][sl])
print(std_dev1, std_dev2, std_dev3, std_dev4)
#Using the data to the standard deviation of each row in the data set.
max_value1 = max(data[0:150][pw])
max_value2 = max(data[0:150][pl])
max_value3 = max(data[0:150][sw])
max_value4 = max(data[0:150][sl])
print(max_value1,max_value2, max_value3, median_value4)
#Finding the max value of each row in the data set.
min_value1 = min(data[0:150][pw])
min_value2 = min(data[0:150][pl])
min_value3 = min(data[0:150][sw])
min_value4 = min(data[0:150][sl])
print(min_value1, min_value2, min_value3, min_value4)
#Finding the min value of each row in the data set.

print([min(data[0:150][pw]),max(data[0:150][pw])])
print([min(data[0:150][pl]),max(data[0:150][pl])])
print([min(data[0:150][sw]),max(data[0:150][sw])])
print([min(data[0:150][sl]),max(data[0:150][sl])])
#Finding the range of sizes of each row in the data set.