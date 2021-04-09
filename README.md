# GiniInABottle
## Project Group 6

Charlie Comeau, Anubhav Agarwal, Yeojin Chang, Amy Liu, and Cecilia Liu

Spring 2021 CS 4641 Intro to Machine Learning: Semester-long Project

## Introduction

With the rise of COVID-19, income inequality across the world is being illuminated through healthcare disparities in number of cases, treatment availability, vaccine distribution, and more.&#x00B9;

The Gini Coefficient, which ranges from 0 (perfect equality) to 1 (perfect inequality), measures a country's income inequality by plotting the cumulative percentiles of its population against its cumulative income, as visualized by the Lorenz curve; the index can be determined by comparison to the 45 degree line of perfect income equality.&#x00B2; 

![화면 캡처 2021-03-02 231757](https://user-images.githubusercontent.com/44009995/109751978-912aec00-7bad-11eb-9526-3545116a3191.png)

##  Problem Statement
The goal of this study is to understand how different statistics indicating a country's well-being can relate to or predict the country's income inequality, as measured by the Gini Coefficient. 


## Unsupervised Methods 

Using different economic and demographics data as our features we can first explore our data from an unsupervised perspective. 

* Clustering: 

After PCA, we used Density-based spatial clustering of applications with noise (DBSCAN) to group together countries with similar features.

First, the optimal number of epsilon was determined by calculating the nearest n points for each point and plotting to see where the greatest change occurs (elbow method). Epsilon was determined to be approximately 5000, as visualized in the graph below. 

<img width="544" alt="Screen Shot 2021-04-08 at 8 16 43 PM" src="https://user-images.githubusercontent.com/66150928/114111211-7253ff80-98a7-11eb-9b15-212238fdf457.png">

Then, we ran DBSCAN with an epsilon value of 5000 and min samples = 2 to get approximately 21 clusters, 29 noise points, and a silhouette coefficient (SC) of 0.316. This SC is not great, as it implies the clusters are not very dense nor well-separated. While DBSCAN is great at handling noise and clusters of different shapes and sizes, it is extremely sensitive to hyperparameters. For the next report, we may improve clustering results by further fine tuning the epsilon and min samples parameters.

<img width="495" alt="Screen Shot 2021-04-08 at 8 16 49 PM" src="https://user-images.githubusercontent.com/66150928/114111231-826bdf00-98a7-11eb-8334-d573b428a262.png">


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
Challenges we may encounter include acquiring sufficient data as well as successfully identifying the best features in the datasets. We hope to address the former concern by extrapolating when necessary and taking a time plot of countries’ data over a 10-30 year period to maximize data input; for the latter issue, we plan on delving into methods like SKLEARN python and PCA for dimension reduction. The conclusions of our research could have implications for predictions of income equality from both expected (i.e. legislative influence, economic freedom)&#x00B3; and unexpected (i.e. happiness, COVID case count) factors.


## References
  1. “Coronavirus vs. Inequality.” UNDP, feature.undp.org/coronavirus-vs-inequality/.
  2. “Income Inequality - OECD Data.” TheOECD, data.oecd.org/inequality/income-inequality.htm. 
  3. Kuznets, Simon. "Economic growth and income inequality." The American economic review 45.1 (1955): 1-28.
  4. Dutt, Pushan, and Ilia Tsetlin. "Income Distribution and Economic Development: Insights from Machine Learning." Wiley Online Library. INSEAD (Institut Européen D'Administration Des Affaires) Singapore, 11 May 2020. Web.
  5. Cabrera, Analiz, and Sindhu Srinath. "Predicting Inequality in the United States: A Machine Learning Exploration." Medium. The Startup, 13 Nov. 2020. Web. 01 Mar. 2021.

## Appendix

### Relation to Current Events
With the rise of COVID-19, income inequality across the world is being illuminated through healthcare disparities in number of cases, treatment availability, vaccine distribution, and more. According to the United Nations Development Programme, "The virus is ruthlessly exposing the gaps between the haves and the have nots, both within and between countries." In this study, we hope to discover significant factors that correlate to a country's Gini coefficient, including those related to the COVID-19 pandemic.

### Previous Research
In the greater scope of income inequality and economic development, the Gini Coefficient has been used as one factor to help predict economic growth <sup>4</sup>, however we have found only one other source that attempted to predict a state’s Gini Coefficient like us. In a model created by Cabrera and Srinath <sup>5</sup>, they tried to use “demographics, race, education, and federal & state spend[ing] in education” to predict whether a state or county’s Gini Coefficient is above or below the national median. Pulling the majority of their data from US Federal Government sources like the US Census, their goal was to better understand how and why America’s domestic features made its Gini Coefficient significantly higher than that of the other G7 countries (0.47 to 0.33), and they found that race features were the most successful at predicting income inequality, specifically the proportion of the black and white population alone in a Random Forest Classifier yielded an accuracy of 96% on determining whether a region was above or below the median national Gini Coefficient.

About using the Gini Coefficient to predict economic growth in Dutt and Tsetlin’s work at the INSEAD Singapore Business school, the authors found that the fraction of the population living in poverty was much more accurate in predicting economic growth measures such as “schooling, institutional quality, and per capita income” than the Gini Coefficient. They noted that the poverty measures are influenced by those in the bottom economic ring of society, whereas the Gini coefficient is equally influenced by both sides of the economic spectrum, and recommended on focusing on alleviating poverty at the bottom over addressing a country’s income inequality as a policy approach for increasing economic development.

These literature reviews are important because while the Gini Coefficient provides a wealth of information on a country’s economic condition, they do not provide the whole picture and as a result, our group would like to note our results does not claim to offer a perfect solution to this complex issue.

### Expected Results from Supervised Methods

* Linear Regression: attempt to find a direct relationship between these parameters and the Gini coefficient. However, this would not be able to capture complex or non-linear relationships 
* K-Nearest Neighbors: attempt to find similarities between instances using measures such as Euclidean distance and Hamming distance. However, this is extremely expensive and might perform poorly with a large number of parameters and not enough instances.
* Neural Networks: attempts to capture complex relationships without extensive effort on feature engineering. However, it might be prone to overfitting, especially since our dataset is small.



