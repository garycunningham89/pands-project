#Gary Cunningham - GMIT - G00376467.
#Programming and Scripting Final Project - Submission on 28/04.19

import pandas as pd
# using pandas for opening csv file and analysis.
import matplotlib.pyplot as plt
# Using matplotlib for histogram for stats data analysis.
data = pd.read_csv('iris_csv.csv')
#Allowing reading of the CSV file.
sl = 'sepallength'
sw = 'sepalwidth'
pl = 'petallength'
pw = 'petalwidth'
#Abbreviating the headings.
print(data[sl].describe())
print(data[sw].describe())
print(data[pl].describe())
print(data[pw].describe())
#Separating each column using the describe functions.
data.hist()
plt.show()
# Using the data file with matplotlib function for plotting a a histogram.
#Utilizing the csv file used from the Tutorials point website at: https://www.tutorialspoint.com/python/python_processing_csv_data.htm

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
