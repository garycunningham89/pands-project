Gary Cunningham - GMIT - G00376467.
Programming and Scripting Final Project - Submission on 28/04.19
    Project Structure
    1. Introduction
    2. Analysis
    3. Results
    4. Conclusion
    5. Appendices


1. INTRODUCTION
Ronald Aylmer Fisher's Iris data set has been consulted in a vast range of articles and disciplines as noticeable during initial research. Ronald Fisher, himself, was an English statistician firstly, with intrinsic ties to the studies of genetics, eugenics and biology as a whole who compiled the Iris Data Set as per this study (Yates and Mather, 1963). His studies have given him the affectionate title of "Father of Statistics" by some and he believed his various studies allowed greater ties between mathematics and biology as statistics, especially, are useful while trying to explain the various phenomena of science (Yates and Mather, 1963). His own 1936 study titled "The use of multiple measurements in taxonomic problems" portrayed data on three different Iris flower species;- Iris Setosa, Iris Virginica and Iris Versicolor. The data compiled comprised of four features of each species, i.e. sepal length, sepal width, petal length and petal width. The total flowers contained in the data set were 150, split into 50 of each of the three species. All of the attribute information was measured in cm. The data set characteristics are summarized in the following list (Fisher, 1936, adapted from the UCI Machine Learning Repository, Iris data set):

~ Classes: 3 - Species - Setosa, Virginica, Veriscolor.
~ No of Inputs: 150 - 50 of each class above.
~ Number of Attributes: 4 - Sepal Length, Sepal Width, Petal Length, Petal Width.
~ Attribute Measurement: cm.
~ Analysis Type: Multivariate

The multivariate analysis type utilized by Fisher allows a range of measurement techniques on this data set as there are more than one variable and those variables are correlated (Olkin and Sampson, 2001). The intention of this project is to firstly, upload the data set, compile various calculations (using the Python programming language) of various variables within the data set and summarize the results with the aid of statistics, tables and diagrams, where required, to attempt to explain its usefulness and its ties to machine learning and data analysis overall. The following lists i) and ii) are some keywords and the files as part of this projects respectively.

i) Keywords:
* ROW - data inputs. In this data set it is the measurements compiled by Fisher for 3 classes of 50 each.
* VARIABLE - same as above.
* ATTRIBUTES - the attributes are the specifications themselves, i.e. Setosa, Virginica, Versicolor.
* CLASSES - same as above.
* Dataset - in this case it is the Fisher dataset which is imported in the script from the iris_csv csv file also attached.
* MACHINE LEARNING - allows "computers the ability to learn without being explicitly programmed" (Athur Samuel). Allows processing of BIG DATA.
* DATA ANALYSIS - is the inspection and modelling of data to discover information and conclusions which may aid the process of decision making.
* DATA MINING - is the examination of existing databases in order to produce new information.
* MULTIVARIATE ANALYSIS: two or more forms of variables for analysis.
* UNIVARIATE ANALYSIS: one variable for analysis.
* SEPAL: leaf-like part of the flower which encloses the petals and bud for protection.
* PETAL: the parts of the flower which define its shape and are leaf-like.

ii) Project File Names and Description:
+ README.md - core file for project with content of project contained or described and includes observations and reference list.
+ iris_csv.csv - csv file containing the Iris dataset, the core component of this project.
+ importdataset.py - Python script file for importing the csv file above and outputting it in total or in sections for analysis.
+ statisticaldataanalysis.py - Python script file for using the Iris dataset for outputting statistics such as maximum, minimum, etc. to see if they can explain the relations the data within Fishers dataset.
+ graphicaldataanalysis.py - Python script file for outputting the analysis of the Iris dataset in various visual graphs in attempt to explain and summarise it.


2. ANALYSIS

The research allowed consultations of various studies to aptly gain an understanding of Fisher his Iris data set and the importance in it as a tool for analysis. There are vast articles citing the Iris data set but I first went back to Fisher's initial 1936 study to gain an understanding of what he was trying to portray. The importance of the man himself was researched in Yates and Mather(1963) biography of him and then, with a basis to work upon, multiple articles and analysis were consulted to understand its importance. Use of this data set can allow experiences with machine learning, data mining and data analysis as a whole.

The analysis allowed use of learnings from lecture content as part of the course and with further self directed learning from Python.org, w3schools.com and other websites for improvement of programming and scripting such as programiz, tutorialspoint and stackoverflow as shown in the reference list below. The iris data set was imported firstly from the UC Irvine Machine Learning Repisotory and attempts were made to manipulate the data set using Python by creating outputs of the columns, rows, etc. and testing the max, min, mean, etc. This was a preliminary testing to try and gain an understanding of the data set while various scripts learned from previous. There were various other studies consulted such as Kaggle, Dickerson, etc. as contained below to view their approach to such a study. My own approach was as follows:

a) Gain an understanding of Fisher, his Iris Data Set and its importance.
b) Extract and test the data set using Python to see the outputs and attempt to further understand why this data set is so popular.
c) Use Python to manipulate the data set for outputting various analysis using programs to output data, tables, graphs, etc.
d) Use my own outputs to attempt explain Fishers Iris Data Set and its findings as accurately as possible.
e) Conclude these outputs with an explanation as to why Fishers Iris Data Set is so important and prevalent for data analysis now.

The primary resources for data analysis of the Iris dataset are pyhton programming language through Anaconda, Visual Studio Code, Python.org tutorials and w3schools tutorials with packages such as pandas, seaborn, matplotlib and numpy utilized alongside various other compositions regarding the same. The Scikit Learn package were witnessed on various sources but the use has been limited for this project but will be considered at a later date.

The first intended outputs used in the Python code was to input the iris_csv file and ouput it on python to show its 

were the statistical data extracted from the data set as a numeric analytical tool. The mode mean, min, max and range of sizes of each variable contained within the data set were compiled and the following was the outputs of the codes as contained in the script ..... 

TABLE OF OUTPUTS.

3. RESULTS

The next analysis was intended to by a more in depth look at the Iris d utilizing various graphs and outputs using the pandas, seabork, matplotlib etc. as mentioned above. The graphical analysis of the dataset allows for a better understanding as the visual aspect allows the reader gain an understanding of the differences in the variables and why this is important or interesting.

The chronological python script outputs are..........

4. SUMMARY AND CONCLUSION
The dataset was tested through various means while gaining understanding through many of the online sources mentioned in the reference. The finally with a consistent assessment of the dataset was portrayed in a combined python code, titled Irisfinalproject.py. The primary data analysed was .............

5. APPENDICES

PRIMARY ISSUES: 

- Researching accurate components for all aspects of the project.
- Correctly inputting and learning of the Python programming language used for analysis.
- Time management and accuracy of outputs.
- FutureWarning Error with graph outputs in graphicaldataanalysis.py file. Could not accurate resolution but contributors on StackOverflow have stated similar output error messages. Thankfully it did not affect the flow of the graphs and it seems to be a software issue regarding the packages imported for the outputs used on the machine.

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
16. Kaggle (2019) Iris d - Exploratory Data Analysis.
Accessed online at: https://www.kaggle.com/lalitharajesh/iris-dataset-exploratory-data-analysis
17. Kaggle (2019) Machine Learning with Iris d.
Accessed online at: https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
18. Sci-kit Learn (2019) The Iris d.
Accessed online at: https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
19. Taylor, J. (2011) Stats 202: Data Mining. Stanford Univeristy.
Accessed online at: http://statweb.stanford.edu/~jtaylo/courses/stats202/visualization.html
20. Dong, N. (2019) RPubs: Introduction 1 - Iris d.
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