# GiniInABottle
## Project Group 6

Charlie Comeau, Anubhav Agarwal, Yeojin Chang, Amy Liu, and Cecilia Liu
Spring 2021 CS 4641 Intro to Machine Learning: Semester-long Project

## Introduction

With the rise of COVID-19, income inequality across the world is being illuminated through healthcare disparities in number of cases, treatment availability, vaccine distribution, and more.1 

The Gini Coefficient, which ranges from 0 (perfect equality) to 1 (perfect inequality), measures a country's income inequality by plotting the cumulative percentiles of its population against its cumulative income, as visualized by the Lorenz curve; the index can be determined by comparison to the 45 degree line of perfect income equality.2 

##  Problem Statement
The goal of this study is to understand how different statistics indicating a country's well-being can relate to or predict the country's income inequality, as measured by the Gini Coefficient. 


## Unsupervised Methods 

Using different economic and demographics data as our features we can first explore our data from an unsupervised perspective. 

* Clustering: We can use clustering algorithms (K-Means, GMM, Hierarchical or DBSCAN), to group together countries with similar features. 
* Dimensionality Reduction: Since we expect to make use of many different economic and demographic features in our model, it would make sense to use dimensionality reduction or feature importance techniques to determine which of our features are the most relevant. We expect lots of different economic statistics we analyze in our model to be correlated to one another, as such techniques like PCA would allow us to reduce our dimensions to components that capture the most variance in our data. 

We believe dimensionality reduction will reduce complexity and improve the results of clustering. After running clustering algorithms, we might expect countries in organizations like the EU or OPEC to form clusters. 



## Supervised Methods 
Our general idea is to develop a prediction model that would output our predicted Gini coefficient for a specific country in a specific year, given other parameters like happiness scores or mortality ratios. We would focus both on factors that are dependent on income, as well as those that are not directly dependent, and find correlations between the weights of these factors and the prediction accuracy.

We would also use multiple supervised learning models and elaborate on their performances with this specific task. The models we will be using include: 
* Linear Regression
* K-Nearest Neighbors
* Neural Networks

Due to the limited data points available and the high dimension of data, we expect the K-Nearest Neighbors to perform the most poorly. We expect Linear Regression to perform the best because most of the parameters we will be using would likely be closely related to the Gini coefficient.


## Discussion
Challenges we may encounter include acquiring sufficient data as well as successfully identifying the best features in the datasets. We hope to address the former concern by extrapolating when necessary and taking a time plot of countries’ data over a 10-30 year period to maximize data input; for the latter issue, we plan on delving into methods like SKLEARN python and PCA for dimension reduction. The conclusions of our research could have implications for predictions of income equality from both expected (i.e. legislative influence, economic freedom)3 and unexpected (i.e. happiness, COVID case count) factors.





## References
* “Coronavirus vs. Inequality.” UNDP, feature.undp.org/coronavirus-vs-inequality/.
* “Income Inequality - OECD Data.” TheOECD, data.oecd.org/inequality/income-inequality.htm. 
* Kuznets, Simon. "Economic growth and income inequality." The American economic review 45.1 (1955): 1-28.
* Dutt, Pushan, and Ilia Tsetlin. "Income Distribution and Economic Development: Insights from Machine Learning." Wiley Online Library. INSEAD (Institut Européen D'Administration Des Affaires) Singapore, 11 May 2020. Web.
* Cabrera, Analiz, and Sindhu Srinath. "Predicting Inequality in the United States: A Machine Learning Exploration." Medium. The Startup, 13 Nov. 2020. Web. 01 Mar. 2021.


