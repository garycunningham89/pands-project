Gary Cunningham - G00376467.
Programming and Scripting Final Project - Submission on 28/04.19
The following lists i) and ii) are some keywords and the files as part of this projects respectively.
i) Keywords:
* ROWS, VARIABLES - data inputs. In this data set it is the measurements compiled by Fisher for 3 classes of 50 each.
* ATTRIBUTES, CLASSES - the attributes are the specifications themselves, i.e. Setosa, Virginica, Versicolor.
* DATASET - in this case it is the Fisher dataset which is imported in the script from the iris_csv csv file also attached.
* MACHINE LEARNING - allows "computers the ability to learn without being explicitly programmed" (Athur Samuel). Allows processing of BIG DATA.
* DATA ANALYSIS - is the inspection and modelling of data to discover information and conclusions which may aid the process of decision making.
* DATA MINING - is the examination of existing databases in order to produce new information.
* MULTIVARIATE ANALYSIS: two or more forms of variables for analysis.
* UNIVARIATE ANALYSIS: one variable for analysis.
* SEPAL: leaf-like part of the flower which encloses the petals and bud for protection.
* PETAL: the parts of the flower which define its shape and are leaf-like.
* MEAN: the average of a set of numbers.
* STANDARD DEVIATION: the variance from the mean. It can be a low or high variance depending on the distribution of differences from the mean.
* HISTOGRAM: a bar chart type graph showing distribution of inputs.
* SCATTER, DISTPLOT, VIOLIN, PAIRPLOT: graphs showing the attributes for analysis.

ii) Project File Names and Description:

+ README.md - core file for project with content of project contained or described and includes observations and reference list.
+ iris_csv.csv - csv file containing the Iris dataset, the core component of this project.
+ importdataset.py - Python script file for importing the csv file above and outputting it in total or in sections for analysis.
+ univariatedataanalysis.py - Python script file for using the Iris dataset for outputting statistics such as maximum, minimum, etc. to see if they can explain the relations the data within Fishers dataset.
+ multivariatedataanalysis.py - Python script file for outputting the analysis of the Iris dataset in various visual graphs in attempt to explain and summarise it.
+ Other attachments are listed in Appendices section at end of ReadMe. 
Within each .py file there are notes on inputs denoted with "#" so as not to be included in the python script but to attempt to explain the process and the reasoning behind it for the reader.

Project ReadMe Structure
1. Introduction
2. Analysis
3. Results
4. Conclusion
5. Appendices

1. INTRODUCTION
Ronald Aylmer Fisher's Iris data set has been consulted in a vast range of articles and disciplines as noticeable during initial research. Ronald Fisher, himself, was an English statistician firstly, with intrinsic ties to the studies of genetics, eugenics and biology as a whole who compiled the Iris Data Set as per this study (Yates and Mather, 1963). His studies have given him the affectionate title of "Father of Statistics" by some and he believed his various studies allowed greater ties between mathematics and biology as statistics, especially, are useful while trying to explain the various phenomena of science (Yates and Mather, 1963). His own 1936 study titled "The use of multiple measurements in taxonomic problems" portrayed data on three different Iris flower species;- Iris Setosa, Iris Virginica and Iris Versicolor. The data compiled comprised of four features of each species, i.e. sepal length, sepal width, petal length and petal width. The total flowers contained in the data set were 150, split into 50 of each of the three species. All of the attribute information was measured in cm. The data set characteristics are summarized in the following list (Fisher, 1936, adapted from the UCI Machine Learning Repository, Iris data set):

* Classes: 3 - Species - Setosa, Virginica, Veriscolor.
* No of Inputs: 150 - 50 of each class above.
* Number of Attributes: 4 - Sepal Length, Sepal Width, Petal Length, Petal Width.
* Attribute Measurement: cm.
* Analysis Type: Multivariate

The multivariate analysis type utilized by Fisher allows a range of measurement techniques on this data set as there are more than one variable and those variables are correlated (Olkin and Sampson, 2001). The intention of this project is to firstly, upload the data set, compile various calculations (using the Python programming language) of various variables within the data set and summarize the results with the aid of statistics, tables and diagrams, where required, to attempt to explain its usefulness and its ties to machine learning and data analysis overall.

2. ANALYSIS

The research allowed consultations of various studies to aptly gain an understanding of Fisher his Iris data set and the importance in it as a tool for analysis. There are vast articles citing the Iris data set but I first went back to Fisher's initial 1936 study to gain an understanding of what he was trying to portray. The importance of the man himself was researched in Yates and Mather(1963) biography of him and then, with a basis to work upon, multiple articles and analysis were consulted to understand its importance. Use of this data set can allow experiences with machine learning, data mining and data analysis as a whole.

The analysis allowed use of learnings from lecture content as part of the course and with further self directed learning from Python.org, w3schools.com and other websites for improvement of programming and scripting such as programiz, tutorialspoint and stackoverflow as shown in the reference list below. The iris data set was imported firstly from the UC Irvine Machine Learning Repisotory and attempts were made to manipulate the data set using Python by creating outputs of the columns, rows, etc. and testing the max, min, mean, etc. This was a preliminary testing to try and gain an understanding of the data set while various scripts learned from previous. There were various other studies consulted such as Kaggle, Dickerson, etc. as contained below to view their approach to such a study. My own approach was as follows:

a) Gain an understanding of Fisher, his Iris Data Set and its importance.
b) Extract and test the data set using Python to see the outputs and attempt to further understand why this data set is so popular.
c) Use Python to manipulate the data set for outputting various analysis using programs to output data, tables, graphs, etc.
dataset) Use my own outputs to attempt explain Fishers Iris Data Set and its findings as accurately as possible.
e) Conclude these outputs with an explanation as to why Fishers Iris Data Set is so important and prevalent for data analysis now.

The primary resources for data analysis of the Iris dataset are pyhton programming language through Anaconda, Visual Studio Code, Python.org tutorials and w3schools tutorials with packages such as pandas, seaborn, matplotlib and numpy utilized alongside various other compositions regarding the same. The Scikit Learn package were witnessed on various sources but the use has been limited for this project but will be considered at a later date.

The first intended outputs used in the Python code was to input the iris_csv file and ouput it on python to show some of aspects of the file itself. Using the python file importdataset.py, after importing the file and naming it "data", the following commands were used and they include a small explanation of their intended outputs alongside them;
+ print(data) -shows entire data set. 
+ print(data.head()) - shows first 5 rows of the data set.
+ print(data.tail()) - shows last 5 rows of the dataset.
+ print(data.describe()) -gives a statistical summary of the dataset.
+ print(data.shape) - tells amounts of rows and columns in format: (rows, columns)
+ print(data.columns) - gives output of the columns headers and the 'dtype'.
+ print(data["class"].value_counts()) - separates the column class and gives output of each as well as the dtype as int64.

As well as these commands, there are a few other attempts, such as opening the file and outputting single columns, which were tested for learning purposes throughout the course of the project and are now marked with # so as to not be apart of the output itself. This file, importdataset.py in general only allows for summarising the data set as an introduction for the more emphasised files within hereafter. The command print(data.describe()) is arguably the most useful from this output as it grants the following output which will be discussed hereafter;
+       sepallength  sepalwidth  petallength  petalwidth
+ count   150.000000  150.000000   150.000000  150.000000
+ mean      5.843333    3.054000     3.758667    1.198667
+ std       0.828066    0.433594     1.764420    0.763161
+ min       4.300000    2.000000     1.000000    0.100000
+ max       7.900000    4.400000     6.900000    2.500000

The second file used in the project was the univariatedataanalysis.py file which was used to extract the csv file from from the data set and use Python code as a numeric analytical tool for explaining the dataset. The above table shows the count, mean, std(standard deviation), min and max the attributes within the dataset (less the 25, 50 and 75 percent readings which were removed for this insert). The sepallength, sepalwidth, petallength and petalwidth figures shown show a univariate analysis of the Fisher dataset, where there is no second varibale used in the analysis. Viewing the outputs above as well as the separation of each variable in the python file anivariatedataanalysis.py and the matplotlib generated histogram.png, which is as part of this project, the following was observed;

a) The range of sepal lengths sizes in cm is 4.30-7.90, with a standard deviation of 0.828066 from the mean 5.843333. Viewing the histogram one can see that the count for sepal length is not too widely distributed among the count of 150 indicating the sepal length would not be a good indicator for variance amongst flower species in the Iris data set.
b) The range of sepal widths sizes in cm is 2.00-4.40, with a standard deviation of 0.433594 from the mean 3.054. Viewing the histogram one can see that the count for sepal width is narrowly distributed among the count of 150 as most of the count are focused of the center of graph near the mean indicating the sepal width would be a difficult indicator for variance amongst flower species in the Iris data set.
c) The range of petal lengths sizes in cm is 1.0-6.90, with a standard deviation of 1.764420 from the mean 3.758667. Viewing the histogram one can see that the count for petal length is widely distributed among the count of 150 indicating that petal length would be great indicator for variance amongst flower species in the Iris data set.
dataset) The range of petal widths sizes in cm is 0.10-2.50, with a standard deviation of 0.763161 from the mean 1.198667. Viewing the histogram one can see that the count for petal width is widely distributed among the count of 150 indicating the petal width would be a good indicator for variance amongst flower species in the Iris data set.

The other script included in univariatedataanalysis.py shown in the outputted scatterplotpetal.png and scatterplotsepal.png files in this file show similar observations. The graph plots both aspects, i.e. width and length, of both the petal and sepal data on the same graph. The scatterplot petal shows a wider ranging graph with the data must more identifiable and separable from each other showing variance amongst each flower studied. Alternatively, the scatter plot graph on sepal, does showed variance but not to the same extent and the differences are not as easily identifiable and separable as the length and width for the petal data. There were various tests done in the univariatedataanalysis.py file for other statistics, mode, median and so on and they are contained preceded by a # in the file itself.

The third python file used in the project was the multivariatedataanalysis.py file which allowed the greatest amount of analysis with respect to the Fisher Iris data set. The data was again imported using pandas and various others such as seaborn, matplotlib and numpy. The previous paragraph showed a univariate analysis using the petal lengths and widths and the sepal lengths and widths to distinguish the various data but this file intends to increase the range of identifier capabilities by analysing the same factors but separating them into the 3 Iris classes as part of Fishers study, Setosa, Versicolor and Virginica. The first section of the python file outputs a combined graph of all 4 attributes which is saved in the file as plotclasses.png. These are combined output of distribution plots and colour coordinated scatter plots similar to those witnessed in the univariateanalysis.py file above. The colour coordination denotes the 3 classes, Setosa, Versicolor and Virginica. The plotclasses.png is useful for overview data analysis but requires further dissection to see the intrinsic differences between the 3 classes with regards sepal length, sepal width, petal length and petal width.

The scatterplotclassespetal.png and the scatterplotclassessepal.png which are generated from the second part of the python code contained within multivariatedataanalysis.py are the same as the scatterplotpetal.png and scatterplotsepal.png as seen previously except the data is now colour coordinated to distinguish which class each input is assigned to. The code for this is as follows, with some explanations attached;
* sns.set_style("whitegrid") 
* sns.FacetGrid(iris, hue = "class", height=4).map(plt.scatter, "sepallength", "sepalwidth").add_legend()
* plt.show() #Using seaborn as sns to graph the "class" and sepal length and sepal width.
* sns.set_style("whitegrid")
* sns.FacetGrid(iris, hue = "class", height=4).map(plt.scatter, "petallength", "petalwidth").add_legend()
* plt.show() #Using seaborn as sns to graph the "class" and petal length and petal width.

The package seaborn was used for these graphs which show the data within the graph in three colours blue, orange and green denoting setosa, versicolor and virginica respectively. As witnessed with the graphs earlier the inputs for tne petal length and width and much more dipersed than that of the sepal width and length. Within the scatterplotclassespetal.png we see a distinct gap in sizes amongst the species and now the colour coordination and legend within the analysis inform that the setosa is visibly smaller in length and width and is contained in the bottom right quartile of the graph separated from the other two classes versicolor and virginica. Similarly while reviewing the scatter plot on sepal length and width in the scatterplotclassessepal.png file, with the class colour differentials we can maintain that the sizes are not as distinct but the Iris setosa sepal width and length data inputs are visible in the top left hand side of the graph separated from the other classes of the irises, showing that the setosa species from the dataset is linearally separable from the versicolor and virginica. What is more noticeable as a defining feature of different classes within the same species is that versicolor and virginica are not easily separable in the scatterplot for sepal width vs length but there is some definition of separation in the petal length and width between them with virginica having the longest and widest petals and the farthest deviation from the mean.

To further analyse the data for Fisher Iris data set there were other graphical analyses compiled within the multivaraitedataanalysis.py file within this project. It was decided to further divide the four attribute into sepal length, sepal width, petal length and petal with pyhton coding to analyse differential features of each in graphical form with colour coding allowing for identification of the different classes within Fishers data set, setosa, virginica and versicolor. The graph style chosen with the help of the matplotlib and seaborn tutorials, class content and some of the various resources mentioned in the reference list, was both a single ditribution graph for each attribute and a single violinplot for each also. The files are all saved in this project as png files and they show each attribute in separate graphs with the data for each class collour coordinated to show differences. The code was used with the Seaborn and Matplotlib packages and it allowed graph both the distribution plots as follows:
Distribution Plot code: 
* sns.set_style("whitegrid") #setting the style as whitegrid as seen in tutorials.
* sns.FacetGrid(iris, hue = "class", height=4).map(sns.distplot, "ATTRIBUTE").add_legend())
* plt.show() #using matplotlib function plt.show() to output and add_legend() to distinguish classes.

* sns.violinplot(y='class', x='ATTRIBUTE', data=iris, inner='quartile') #using data = iris for the imported CSV file.
* plt.show() # Using plt.show() to output graph.

The ATTRIBUTE word in both it changeable to output with petal length/width or sepal length/width.

All graphs showed similar outcomes to the scatter plot graphs above highlighting the difference in both the petal and sepal, for their separate characteristics, length and width, as identifiers in species differentials as Iris flowers. These differentials among the 150 strong data set are then added to a multivariate analysis type where a sub division of class of Iris species is added to identify or analyses differences from the data inputted. Some of the results of the analysis will be discussed in the next section.

3. RESULTS

The results section is going to be split similar to the file naming as in univariate analysis and multivariate analysis. Within each the species, Iris, and the data Fisher composed will be assessed to see its importance in defining the speices and its usefulness in data analysis. 
The univariate aspect deals with the fact there are is one varible for study and that is the size attribute. This is subdivided into length and width of both the flowers petal and sepal and all data was recorded. Upon undertaking the research it was clear with the help of statistics and graphs that the length and width of the petal and sepal could allow data become useful in identifying differences among a species or a system or anything that has a defining feature or defining features which can be traced and tracked for analysis. The following were the results or observations of the univariate analysis:
* The sepal length
* The sepal width
* The petal length
* The petal width

In the pairplotpetal we can see that petal length is much varied in all 150 data inputs and that these are further distinguished by class. The iris setosa has much smaller petal than the versicolor and virginica and can be easily identified. The differences in the versicolor and virginica are also visible on the graph but not with the same definition. 

The next analysis was intended to by a more in depth look at the Iris dataset utilizing various graphs and outputs using the pandas, seabork, matplotlib etc. as mentioned above. The graphical analysis of the dataset allows for a better understanding as the visual aspect allows the reader gain an understanding of the differences in the variables and why this is important or interesting.
* The sepal length
* The sepal width
* The petal length
* The petal width

Unavariate analysis - which is best for describing differences in variance
Multivatiat data analysis
#########Observations - Using sepal - can distinguish setosa flowers. Versicolor and Virginica not easily distinguished. 
#########using petal is the same but versicolor and virginica are slightly more linearly separable than sepal.
##################petal length and width are best identifiers of types of flowers. setosa very different. others some overlap.
##########univariate analysis. pl > pw > sl > sw going by graphs

4. SUMMARY AND CONCLUSION

The python programming language and the various aspects of its capabilities allowed a more accurate study of this dataset than merely looking at the data in its original form. Data analysis of the data set showed that with manipulation of various aspects of a studied thing or species as the case may be, changes or differences are easily identifiable and separable from each other. Allowing for this data analysis through statistics in a living being through his Iris data set, it is easily understood why Fisher was highly regarded in his field for statistics and why he is still being widely used today. The Iris species was an analyzable species in a time when many were not monitoring similar attributes and it can be used a basis or a test case for greater monitoring of data for learning or as a database for mining for many new data analysts.
5. APPENDICES

GRAPH (.png) FILES: 
1. histogram.png
2. scatterplotpetal.png
3. scatterplotsepal.png
4. plotclasses.png
5. scatterplotclassespetal.png
6. scatterplotclassessepal.png
7. pairplotpetallength.png
8. pairplotpetalwidth.png
9. pairplotsepallength.png
10. pairplotsepalwidth.png
11. violinplotpetallength.png
12. violinplotpetalwidth.png
13. violinplotsepallength.png
14. violinplotsepalwidth.png

PRIMARY ISSUES: 

- Researching accurate components for all aspects of the project.
- Correctly inputting and learning of the Python programming language used for analysis.
- Learning, testing and editing code and readme file continuously while rememebering to add sources for newly learned material.
- Time management and accuracy of outputs.
- FutureWarning Error with graph outputs in multivariatedataanalysis.py file as follows:

* C:\Users\Owner\Anaconda3\lib\site-packages\scipy\stats\stats.py:1713: FutureWarning: Using a non-tuple sequence for multidimensional indexing is deprecated; use `arr[tuple(seq)]` instead of `arr[seq]`. In the future this will be interpreted as an array index, `arr[np.array(seq)]`, which will result either in an error or a different result.
* return np.add.reduce(sorted[indexer] * weights, axis=axis) / sumval.
Could not find an accurate resolution but contributors on StackOverflow have stated similar output error messages. Thankfully it did not affect the flow of the graphs and it seems to be a software issue regarding the packages imported for the outputs used on the machine.

REFERENCE LIST:

Class Content, Background Reading and Python Learning Tutorials were prelimary references supplemented by the following list of references;
1.	Python Software Foundation.
Accessed online at: https://www.python.org/
2.	w3Schools.com Tutorials.
Accessed online at: https://www.w3schools.com
3. Python by Programiz Tutorials.
Accessed online at: https://www.programiz.com/
4. Pandas: Python Data Analysis Library.
Accessed online at: https://pandas.pydata.org.
5. NumPy.
Accessed online at: http://www.numpy.org
6. Stack Overflow - Various queries for comparison and improving code output.
Accessed online at: https://stackoverflow.com
7. Matplotlib Tutorials.
Accessed online at: https://matplotlib.org/tutorials/index.html
8. Wikipedia: Introduction to Fisher's Iris Data Set.
Accessed online at: https://en.wikipedia.org/wiki/Iris_flower_data_set
9. Fisher, R. A. (1936) The use of multiple measurements in taxonomic problems. The Annals of Eugenics (1935-1954).
Accessed online at: https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x
10.	UC Irvine Machine Learning Repository: Iris data set.
Accessed online at: https://archive.ics.uci.edu/ml/machine-learning-databases/iris/
11. Datahub (2019) Machine Learning: Iris.
Accessed online at: https://datahub.io/machine-learning/iris
12. Yates, F. and Mather, K. (1963) Biographical Memoirs: Ronald Alymer Fisher, 1890-1962. Royal Society Publishing
Accessed online at: https://royalsocietypublishing.org/doi/pdf/10.1098/rsbm.1963.0006
13. Olkin, I. and Sampson, A. R. (2001) Multivariate Analysis: Overview, in International Encyclopedia of the Social & Behavioral Sciences.
Accessed online at: https://www.sciencedirect.com/topics/medicine-and-dentistry/multivariate-analysis
14. Excel File showing Iris Data Set for comparison (2019)
Accessed online at: : https://www.saedsayad.com/datasets/Iris.xls
15. Dickerson, K. (2016) Fisher's Irises.
Accessed online at: https://rstudio-pubs-static.s3.amazonaws.com/205883_b658730c12d14aa6996fe2f6c612c65f.html
16. Kaggle (2019) Iris dataset - Exploratory Data Analysis.
Accessed online at: https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis
17. Kaggle (2019) Machine Learning with Iris dataset.
Accessed online at: https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
18. Sci-kit Learn (2019) The Iris dataset.
Accessed online at: https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
19. Taylor, J. (2011) Stats 202: Data Mining. Stanford Univeristy.
Accessed online at: http://statweb.stanford.edu/~jtaylo/courses/stats202/visualization.html
20. Dong, N. (2019) RPubs: Introduction 1 - Iris dataset.
Accessed online at: https://rpubs.com/nandong/imlp-ch1-iris - Introduction to Iris Data set by rPubs.
21. Tutorialspoint (2019) AI with Python – Supervised Learning: Classification.
Accessed online at: https://www.tutorialspoint.com/artificial_intelligence_with_python/artificial_intelligence_with_python_supervised_learning_classification.html
22. Tutorialspoint (2019) Python - Correlation.
Accessed online at: https://www.tutorialspoint.com/python/python_correlation.html
23. Stack Exchange (2019)
Accessed online at: https://stats.stackexchange.com/questions/74776/what-aspects-of-the-iris-data-set-make-it-so-successful-as-an-example-teaching
24. Programiz (2019) Reading CSV Files in Python
Accessed online at: https://www.programiz.com/python-programming/reading-csv-files
25. Michalski, R. S., Carbonell, J. G. and Mitchel, T. M. (2014) Machine Learning: An Artificial Intelligence Approach, Volume 1.