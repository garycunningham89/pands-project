#Gary Cunningham - GMIT - G00376467.
#Programming and Scripting Final Project - Submission on 28/04.19
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#Importing the preloaded Anaconda Packages for outputs of the iris_csv.csv file later.
#Learning and understanding of each package from class tutorials and each respective websites tutorials.
#The code also had Sckit Learn package data analysis capabilities but at this time these were removed from analysis.
iris = pd.read_csv('iris_csv.csv')
#Importing iris_csv using Pandas.
sns.set_style("whitegrid") #setting the style as whitegrid as seen in tutorials
sns.FacetGrid(iris, hue = "class", height=4).map(plt.scatter, "sepallength", "sepalwidth").add_legend()
plt.show() #Using seaborn as sns to graph the "class" and sepal length and sepal width.
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue = "class", height=4).map(plt.scatter, "petallength", "petalwidth").add_legend()
plt.show() #Using seaborn as sns to graph the "class" and petal length and petal width. 
#Using the identifier, hue = class, setting the height and plotting a scatter with sns.
#Adding legends of the classes on both graphs using add_legend() for easier identification.

#########Observations - Using sepal - can distinguish setosa flowers. Versicolor and Virginica not easily distinguished. 
#########using petal is the same but versicolor and virginica are slightly more linearly separable than sepal.
#pairplot
sns.set_style("whitegrid")
sns.pairplot(iris, hue= "class", height=4)
plt.show()
##################petal length and width are best identifiers of types of flowers. setosa very different. others some overlap.
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue = "class", height=4).map(sns.distplot, "petallength").add_legend()
plt.show()
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue = "class", height=4).map(sns.distplot, "petalwidth").add_legend()
plt.show()
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue = "class", height=4).map(sns.distplot, "sepallength").add_legend()
plt.show()
sns.set_style("whitegrid")
sns.FacetGrid(iris, hue = "class", height=4).map(sns.distplot, "sepalwidth").add_legend()
plt.show()

##########univariate analysis. pl > pw > sl > sw going by graphs

#violin
g = sns.violinplot(y='class', x='sepallength', data=iris, inner='quartile')
plt.show()
g = sns.violinplot(y='class', x='sepalwidth', data=iris, inner='quartile')
plt.show()
g = sns.violinplot(y='class', x='petallength', data=iris, inner='quartile')
plt.show()
g = sns.violinplot(y='class', x='petalwidth', data=iris, inner='quartile')
plt.show()
print

#Utilizing the csv file used from the Tutorials point website at: https://www.tutorialspoint.com/python/python_processing_csv_data.htm
#Code sourced from Kaggle's website at: https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset