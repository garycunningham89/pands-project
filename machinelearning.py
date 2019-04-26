#Code sourced from Kaggle's website at: https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Importing the preloaded Anaconda Packages for outputs of the iris_csv.csv file later.
#Learning and understanding of each package from class tutorials and each respective websites tutorials.
#The code above had Sckit Learn package data analysis but at this time these were removed from analysis.
data = pd.read_csv('iris_csv.csv')
data.head()
data.info()
data.describe()
data['class'].value_counts()

tmp = data.drop('sepalwidth', axis=1)
g = sns.pairplot(tmp, hue='class', markers='+')
plt.show()
g = sns.violinplot(y='class', x='sepallength', data=data, inner='quartile')
plt.show()
g = sns.violinplot(y='class', x='sepalwidth', data=data, inner='quartile')
plt.show()
g = sns.violinplot(y='class', x='petallength', data=data, inner='quartile')
plt.show()
g = sns.violinplot(y='class', x='petalwidth', data=data, inner='quartile')
plt.show()

print
