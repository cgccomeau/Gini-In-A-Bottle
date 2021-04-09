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

## Data Collection

Our data for Gini coefficients comes from gapminder.org, “an independent Swedish foundation with no political, religious or economic affiliations.” It consists of 138 unique countries, and data entries for each country ranging from year 2006 to 2016. Its corresponding features aside from the Gini index include democracy index, GDP per capita, percentage of GDP in investment sector, and percentage of GDP in taxation sector. However, this data only covers the basic statistics of the country on the economics side. We wanted to explore more relations of the Gini index in each country with other factors such as education, population, demographics, etc. Thus, we combined this dataset with other datasets from ourworldindata.org, an organization which provides “research and data to make progress against the world’s largest problems”, compiling data from many sources as specialized institutes (like the Peace Research Institute Oslo (PRIO)), research articles( like ’Inequality Among World Citizens: 1820-1992’ in the American Economic Review), and international institutions or statistical agencies (like the OECD, the World Bank, and UN institutions). We gathered data that most closely delineates the countries we are investigating, extending the features collected and examined.

We gathered as many features as we could for the 138 unique countries from gapminder.org. However, not all countries had data available for basic features, such as Income Per Person, so we needed to remove 4 countries from the list. Our finalized list of features includes the following:

* Income Per Person
* Tax Share Of GDP
* Investment Share of GDP
* Total fertility (live births per woman)
* Deaths From Self Harm (%)
* Life satisfaction in Cantril Ladder (World Happiness Report)
* Life Expectancy
* Unemployment Total (% of total labor force)
* Pupil-teacher ratio in primary education
* Real GDP per capita in 2011US$
* Population density (people per sq. km of land area)
* Agriculture value added per worker. 
 
To keep our dataset consistent, we normalized all numbers indicating prices or numbers to 2010 US Dollars. 

Among these, the “Pupil-teacher ratio in primary education” had empty values for 319 data entries. We wanted to use a feature input method to fill in the holes with guesses based on data collected for other countries and years. The result of this method will be compared with another dataset where we removed the feature “Pupil-teacher ratio in primary education”, so that all data entries in dataset2 are filled. 

After experimenting the dataset on the year 2011, which has the most data entries available, using our models, we decided that 134 unique data entries was not sufficient for machine learning methods using 12 features. We expanded the dataset by using (country, year) tuples as keys instead of solely using country. This approach stretched the dataset from 134 entries to 924, potentially increasing the statistical soundness of the results we provide.

One possible drawback from this approach is that we would have inconsistent amounts of data values for each country. I.e. one country might have all years from 2006 to 2016, while another might only have year 2011 and 2012. 



#### Data Visualization:

Before beginning any machine learning algorithms with all features, we wanted to visualize the data between each feature and see how well each individual feature did at predicting the Gini coefficient. In order to do so, we used Seaborn to run a 2-D linear regression between each feature and the Gini coefficient and visualize the results. The images below are those results, with its corresponding correlation coefficient and line of best fit attached.

![agriculture](https://user-images.githubusercontent.com/46789718/114112586-aa107680-98aa-11eb-8ddc-35b52b98e736.png)
![deaths](https://user-images.githubusercontent.com/46789718/114112588-ab41a380-98aa-11eb-9447-7350a1fb5481.png)
![incomeperperson](https://user-images.githubusercontent.com/46789718/114112589-ab41a380-98aa-11eb-9aac-afd7181670be.png)
![investmentshareofgdp](https://user-images.githubusercontent.com/46789718/114112590-ab41a380-98aa-11eb-87d0-f372aeb5bb87.png)
![lifeexpectancy](https://user-images.githubusercontent.com/46789718/114112591-abda3a00-98aa-11eb-979d-d4c30aff947c.png)
![popdensity](https://user-images.githubusercontent.com/46789718/114112592-abda3a00-98aa-11eb-9404-7e4e06d416be.png)
![realgdppercapita](https://user-images.githubusercontent.com/46789718/114112593-abda3a00-98aa-11eb-9b3f-b2bc59c77156.png)
![taxshareofgdp](https://user-images.githubusercontent.com/46789718/114112594-abda3a00-98aa-11eb-8cc4-320ad36fe1cd.png)
![totalfertility](https://user-images.githubusercontent.com/46789718/114112595-abda3a00-98aa-11eb-9ae1-a474b3efe2cb.png)
![unemployment](https://user-images.githubusercontent.com/46789718/114112596-ac72d080-98aa-11eb-84e1-5fcc37501552.png)
![worldhappiness](https://user-images.githubusercontent.com/46789718/114112597-ac72d080-98aa-11eb-9d76-dfa785d7c11e.png)

A couple things worth pointing out is that Life expectancy, Real GDP per capita, and Income per Person had the 3 strongest correlations, in that order (r = -0.372, -0.336, -0.315). On the other hand, population density, unemployment, and Investment share of GDP had the 3 weakest correlations, in that order (r = 0.0089, -0.0459, 0.0718).

One cool thing to observe is that over our 11 year observation period, income inequality has been decreasing at a rate of approximately 0.215 points per year!

![year](https://user-images.githubusercontent.com/46789718/114112599-ac72d080-98aa-11eb-98c2-4dd0accf7b47.png)



## Unsupervised Methods and Results 

Using different economic and demographics data as our features we can first explore our data from an unsupervised perspective. 

### PCA for Dimensionality Reduction

Since we expect to make use of many different economic and demographic features in our model, it would make sense to use dimensionality reduction or feature importance techniques to determine which of our features are the most relevant. We expect lots of different economic statistics we analyze in our model to be correlated to one another, as such techniques like PCA would allow us to reduce our dimensions to components that capture the most variance in our data.

When running PCA for dimensionality reduction the first step was to run PCA retaining our original number of features (11). This allowed us to see how much each of our new principal components contributed to the explained variance of our data. 

![variance](https://user-images.githubusercontent.com/47800990/114112812-260abe80-98ab-11eb-8317-c0e1792cc024.png)

It’s clear to see that the first two components account for almost all the variance in our data. In fact, the first component accounted for 78.6% of our variance while the first two components contained 99.6% of our variance. Including more principal components beyond that point would give us very little additional information but would increase complexity of our models. Therefore, we chose to transform our data onto the first two components. Below is our original 900 data points projected onto our new principal axes. 

![pca](https://user-images.githubusercontent.com/47800990/114113283-44bd8500-98ac-11eb-9b63-9b4e27190d68.png)

### Clustering

After PCA, we used Density-based spatial clustering of applications with noise (DBSCAN) to group together countries with similar features.

First, the optimal number of epsilon was determined by calculating the nearest n points for each point and plotting to see where the greatest change occurs (elbow method). Epsilon was determined to be approximately 5000, as visualized in the graph below. 

<img width="544" alt="Screen Shot 2021-04-08 at 8 16 43 PM" src="https://user-images.githubusercontent.com/66150928/114111211-7253ff80-98a7-11eb-9b15-212238fdf457.png">

Then, we ran DBSCAN with an epsilon value of 5000 and min samples = 2 to get approximately 21 clusters, 29 noise points, and a silhouette coefficient (SC) of 0.316. This SC is not great, as it implies the clusters are not very dense nor well-separated. While DBSCAN is great at handling noise and clusters of different shapes and sizes, it is extremely sensitive to hyperparameters. For the next report, we may improve clustering results by further fine tuning the epsilon and min samples parameters.

<img width="495" alt="Screen Shot 2021-04-08 at 8 16 49 PM" src="https://user-images.githubusercontent.com/66150928/114111231-826bdf00-98a7-11eb-8334-d573b428a262.png">





## Supervised Methods and Results 
Our general idea is to develop a prediction model that would output our predicted Gini coefficient for a specific country in a specific year, given other parameters like happiness scores or mortality ratios. We would focus both on factors that are dependent on income, as well as those that are not directly dependent, and find correlations between the weights of these factors and the prediction accuracy.

We would also use multiple supervised learning models and elaborate on their performances with this specific task. The models we will be using include: 
* Linear Regression
* K-Nearest Neighbors
* Neural Networks

Due to the limited data points available and the high dimension of data, we expect the K-Nearest Neighbors to perform the most poorly. We expect Linear Regression to perform the best because most of the parameters we will be using would likely be closely related to the Gini coefficient.

* Test/Train Split:

After using the pandas library to convert our CSV data into an operable dataframe, we realized that for the two supervised learning methods, we needed to split our data into a testing and training set. Since each row of our data can be uniquely represented by a tuple of the country and year, we realized if we did a random train/test split on the entire dataset, there is a chance that one year could be disproportionately placed in either the training or testing set. So to compensate, we first divided all our data by year, used sklearn to do a randomized 85/15% test/train split on each year, then concatenated all the individual test/train splits from each year back into its own single set.

### Neural Networks

One of the supervised learning methods we implemented was a neural network. We used the sklearn.neural_network.MLPRegressor class within the sci-kit learn library in Python in order to create this model. Before performing the regression, the x data was scaled to proportion to yield better results. After trying different combinations of parameters within the class, it became apparent that the success of the model depended greatly on which parameters were used. In order to take a more systematic approach, the following combinations of parameters were tested using a series of nested for-loops:
alpha: [0.0001, 0.001, 0.01]
activation functions: ["identity", "logistic", "tanh", "relu"]
solver : ["lbfgs", "sgd"]
hidden layers: [1, 2, 3]
learning rates: ["constant", "invscaling", "adaptive"] when solver = "sgd"
maximum iterations: 5000

For each iteration, we used three different metrics to evaluate whether the model created yielded good results -- R^2 score, Mean Absolute Error (MAE), and Mean Squared Error (MSE). Though it is easiest to identify success solely based on the R^2 value, it has a tendency to appear higher when there are more parameters. In the context of the problem, this would mean iterations in which models had more hidden layers would tend to have a higher R^2 score. To mitigate this fault, we measured the MAE and MSE and found the parameters where the values of these metrics were minimized. 

The following is the first few rows of the table containing the different combination of parameters used at each iteration and their average R^2, MAE, and MSE values after 5 iterations.

![화면 캡처 2021-04-08 203318](https://user-images.githubusercontent.com/44009995/114112113-ab8d6f00-98a9-11eb-987f-c97318b83a5b.png)

R^2 was maximized while MAE and MSE were minimized when alpha was equal to 0.0001, the logistic activation function was used, and there were three hidden layers -- the R^2 value was 0.485195, the mean absolute error was 4.34889, and the mean squared error was 36.0523

![image](https://user-images.githubusercontent.com/44009995/114112212-eee7dd80-98a9-11eb-978b-fd1d19328c4f.png)



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



