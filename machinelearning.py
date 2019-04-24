#https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set_palette('husl')
#matplotlib inline

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

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
