# GiniInABottle
## Project Group 6

Charlie Comeau, Anubhav Agarwal, Yeojin Chang, Amy Liu, and Cecilia Liu

Spring 2021 CS 4641 Intro to Machine Learning: Semester-long Project

## Introduction - Yeojin

With the rise of COVID-19, income inequality across the world is being illuminated through healthcare disparities in number of cases, treatment availability, vaccine distribution, and more.&#x00B9;

The Gini Coefficient, which ranges from 0 (perfect equality) to 1 (perfect inequality), measures a country's income inequality by plotting the cumulative percentiles of its population against its cumulative income, as visualized by the Lorenz curve; the index can be determined by comparison to the 45 degree line of perfect income equality.&#x00B2; 

![화면 캡처 2021-03-02 231757](https://user-images.githubusercontent.com/44009995/109751978-912aec00-7bad-11eb-9526-3545116a3191.png)

##  Problem Statement - Yeojin
The goal of this study is to understand how different statistics indicating a country's well-being can relate to or predict the country's income inequality, as measured by the Gini Coefficient. 

## Data Collection - Jing Xi

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


#### Data Visualization - Charlie:

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

After visualizing our data, it should be easier to see that not all of our features are linearly correlated that well (if at all), thus as a group prediction, we are not expecting terribly high results from applying Linear Regression as is.

## Unsupervised Methods and Results - Amy & Anubhav

Using different economic and demographics data as our features we can first explore our data from an unsupervised perspective. 

### PCA for Dimensionality Reduction - Anubhav:

Since we expect to make use of many different economic and demographic features in our model, it would make sense to use dimensionality reduction or feature importance techniques to determine which of our features are the most relevant. We expect lots of different economic statistics we analyze in our model to be correlated to one another, as such techniques like PCA would allow us to reduce our dimensions to components that capture the most variance in our data.

When running PCA for dimensionality reduction the first step was to run PCA retaining our original number of features (11). This allowed us to see how much each of our new principal components contributed to the explained variance of our data. 

![variance](https://user-images.githubusercontent.com/47800990/114112812-260abe80-98ab-11eb-8317-c0e1792cc024.png)

It’s clear to see that the first two components account for almost all the variance in our data. In fact, the first component accounted for 78.6% of our variance while the first two components contained 99.6% of our variance. Including more principal components beyond that point would give us very little additional information but would increase complexity of our models. Therefore, we chose to transform our data onto the first two components. Below is our original 900 data points projected onto our new principal axes. 

![pca](https://user-images.githubusercontent.com/47800990/114113283-44bd8500-98ac-11eb-9b63-9b4e27190d68.png)

#### Feature Importance - Anubhav:

To determine which features were the most important we can analyze the magnitudes of the corresponding feature in the eigenvectors. For the first principal component features (income per person),  (Agriculture value added per worker) and (Real GDP per Capita) were by far the most prevalent in the eigenvectors and thus, were the most important.. These features were also the most important in our second principal components. However population density also seemed to be of a little importance in the second component. 

![feature_imp_1](https://user-images.githubusercontent.com/47800990/116319727-06b5d180-a785-11eb-8b49-347b9e9cb286.png)

![feature_imp_2](https://user-images.githubusercontent.com/47800990/116319730-074e6800-a785-11eb-9e30-fe76587cadd1.png)
### Clustering - Amy, Anubhav:

After PCA, we used Density-based spatial clustering of applications with noise (DBSCAN) to group together countries with similar features.

First, the optimal number of epsilon was determined by calculating the nearest n points for each point and plotting to see where the greatest change occurs (elbow method). Epsilon was determined to be approximately 5000, as visualized in the graph below. 

<img width="544" alt="Screen Shot 2021-04-08 at 8 16 43 PM" src="https://user-images.githubusercontent.com/66150928/114111211-7253ff80-98a7-11eb-9b15-212238fdf457.png">

Then, we ran DBSCAN with an epsilon value of 5000 and min samples = 3 to get approximately 15 clusters, 41 noise points, and a silhouette coefficient (SC) of 0.302. This SC is not great, as it implies the clusters are not very dense nor well-separated. While DBSCAN is great at handling noise and clusters of different shapes and sizes, it is extremely sensitive to hyperparameters. 

<img width="416" alt="Screen Shot 2021-04-26 at 9 35 00 PM" src="https://user-images.githubusercontent.com/66150928/116264058-f8959000-a747-11eb-9048-114261e8a430.png">

When analyzing the results, it is evident that cluster 0 (red) is the biggest cluster with ⅔ of our data (683 data points), including many Eastern European countries, African countries, and China and India. These countries typically have lower income per capita, which aligns with that feature being our most significant in our PCA analysis. After dropping duplicates, 93 countries are labelled as being in cluster 0. PArt of the reason we believe clsuter 0 is so expansive is due to the "chaining effect" of the DBSCAN algorithm. 

We see 16 countries in cluster 1, composed mostly of “Western” nations, including the United States, Canada, European nations like Austria, UK, France, Germany, Italy, Spain, in addition to Australia. These countries share similar economies and social structures. The subsequent clusters had very few countries--typically between 1 and 3--even though the min points parameter was set at 3 because we had several data points for countries that had data from more than 1 year. Likewise, some countries were placed in more than 1 cluster due to data points from more than 1 year. 

Below is a list of countries that comprise cluster 1 - we highlited this cluster due to the similarity of the countries present. Going forward in our algorithms we might expect these contries to have a similar Gini Coefficient. 

![cluster_1](https://user-images.githubusercontent.com/47800990/116320857-061e3a80-a787-11eb-8cf8-4df23cd5f183.png)

## Supervised Methods and Results - Charlie & Yeojin
Our general idea is to develop a prediction model that would output our predicted Gini coefficient for a specific country in a specific year, given other parameters like happiness scores or mortality ratios. We would focus both on factors that are dependent on income, as well as those that are not directly dependent, and find correlations between the weights of these factors and the prediction accuracy.

We would also use multiple supervised learning models and elaborate on their performances with this specific task. The models we will be using include: 
* Linear Regression
* Neural Networks

Due to the non-linear relationship between the features and Gini Coefficient, we expect Linear Regression to perform the most poorly. We expect Neural Networks to perform the best because its non-linear activation function will be able to capture the non-linear relationship between the features and Gini coefficient. We will also run each model twice -- once on the original dataset and once on the PCA transformed set. We are expecting that the dimensionality reduction due to PCA will make the PCA transformed data to have higher results.

* Test/Train Split - Charlie:

After using the pandas library to convert our CSV data into an operable dataframe, we realized that for the two supervised learning methods, we needed to split our data into a testing and training set. Since each row of our data can be uniquely represented by a tuple of the country and year, we realized if we did a random train/test split on the entire dataset, there is a chance that one year could be disproportionately placed in either the training or testing set. So to compensate, we first divided all our data by year, used sklearn to do a randomized 85/15% test/train split on each year, then concatenated all the individual test/train splits from each year back into its own single set.

### Linear Regression - Charlie

Now that we’ve split and visualized our data, we are ready to run Linear Regression on all features! Using sklearn’s LinearRegression class, we are able to fit our model with the training data, test it against the test data, and create all the accompanying analysis. Here are all the coefficients from our model’s calculated line of best fit. Note the scales of each variable are different (such as a change in 10 doesn’t mean much for Income per Person ($10), however it is a massive difference for Average Life Expectancy (10 years)), so not much insight can be intuitively gleaned from the coefficients.

![Screenshot 2021-04-08 205720](https://user-images.githubusercontent.com/46789718/114113630-1db38300-98ad-11eb-8a9b-699f3ec82ef3.jpg)

From before, since our features were not linearly related very well to the Gini Coefficient, so as expected, our model’s correlation coefficient values aren’t the highest, clocking in at 0.231 for training and 0.22 for testing.

Further, we ran Linear Regression again but on the PCA data. Contrary to expectations, the results were actually worse.

![linregpostpca](https://user-images.githubusercontent.com/46789718/116278788-d7876c00-a754-11eb-9de8-93b111a429c9.jpg)

The correlation coefficient value dropped about 0.14 points to 0.096 for training and dropped 0.057 points to 0.163 for testing.

The nice thing about the testing and training values being consistently low is that overfitting has not occurred here! As a result, we conclude that the features in our dataset and the Gini Coefficient are not strongly linearly correlated and we must now turn to more sophisticated machine learning algorithms than linear regression to capture this relationship.

### Neural Networks - Yeojin

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

Further, we tested the results of the Neural Network algorithm with the data after a PCA transformation, using the methods of parameter tuning. Despite expectations that the PCA transformed data would perform better, the maximum R^2 value was 0.204735, the lowest mean absolute error was 5.446, and the lowest mean squared error was 49.4484. These results were produced when alpha was equal to 0.0001, the logistic activation function was used, and there were three hidden layers -- this was consistent with the results when the algorithm was performed on the original dataset.

![화면 캡처 2021-04-26 205953](https://user-images.githubusercontent.com/44009995/116169284-669f7000-a6d2-11eb-807d-594f6873f02c.png)

We speculate that the PCA transformed data performed inferior to the original data because the inner workings of the Neural Network algorithm somehow conflicted with how PCA transformed the original data. However, it was interesting to find that the same parameters worked the best in both datasets.

## Discussion - Charlie, Amy 

A significant challenge we encountered initially was acquiring sufficient data and cleaning available data. To avoid having empty cells in our dataset, we selected one year which had the most data entries available, but we decided 134 unique data entries was still not sufficient for machine learning methods using 12 features. Thus, we addressed this issue by expanding the dataset by using (country, year) tuples as keys instead of solely using country, stretching the dataset from 134 entries to 924. To further increase our dataset, we aim to look at incorporating data from other years as well and using feature imputation to fill in missing cells; however, there are concerns that there may be too much missing data for this to be successful.
 
From the data visualization and linear regression, it is quite clear that our dataset features and Gini Coefficient are not strongly linearly correlated, therefore further analysis into this problem will require an algorithm with a strong non-linear component to adequately capture this true relationship.
 
After running unsupervised methods (PCA, DBSCAN), and supervised methods (neural network, linear regression), we obtained relatively low confidence scores, as indicated by a silhouette coefficient of 0.302 (DBSCAN) and low correlation coefficients of about 0.5 for the neural network and about 0.2 for linear regression. In the future, we will have to focus on optimization of parameters as well as data refinement to get better results. With more conclusive results, we can state with more confidence the features that are more highly correlated to Gini coefficient prediction. 

## Conclusions - Charlie, Amy

When predicting the Gini coefficient for countries around the world, the most important features we determined were income per person, agriculture value added per worker, and real GDP per capita. Countries of similar affluence and geographical locations tended to form clusters, indicating similar trends of Gini coefficient prediction. In reality, the causes of income inequality is a complex political and socio-economic issue that relies on much more than just 12 features, thus in order to further explore this question, future work should account for a larger range of features that would also increase the computational complexity of such a project. However, with the ever-growing abundance of data, we envision machine learning to become an even more powerful and successful tool to predict economic trends such as income inequality across the globe. 



## References - Charlie
  1. “Coronavirus vs. Inequality.” UNDP, feature.undp.org/coronavirus-vs-inequality/.
  2. “Income Inequality - OECD Data.” TheOECD, data.oecd.org/inequality/income-inequality.htm. 
  3. Kuznets, Simon. "Economic growth and income inequality." The American economic review 45.1 (1955): 1-28.
  4. Dutt, Pushan, and Ilia Tsetlin. "Income Distribution and Economic Development: Insights from Machine Learning." Wiley Online Library. INSEAD (Institut Européen D'Administration Des Affaires) Singapore, 11 May 2020. Web.
  5. Cabrera, Analiz, and Sindhu Srinath. "Predicting Inequality in the United States: A Machine Learning Exploration." Medium. The Startup, 13 Nov. 2020. Web. 01 Mar. 2021.

## Appendix

### Relation to Current Events - Yeojin
With the rise of COVID-19, income inequality across the world is being illuminated through healthcare disparities in number of cases, treatment availability, vaccine distribution, and more. According to the United Nations Development Programme, "The virus is ruthlessly exposing the gaps between the haves and the have nots, both within and between countries." In this study, we hope to discover significant factors that correlate to a country's Gini coefficient, including those related to the COVID-19 pandemic.

### Previous Research - Charlie
In the greater scope of income inequality and economic development, the Gini Coefficient has been used as one factor to help predict economic growth <sup>4</sup>, however we have found only one other source that attempted to predict a state’s Gini Coefficient like us. In a model created by Cabrera and Srinath <sup>5</sup>, they tried to use “demographics, race, education, and federal & state spend[ing] in education” to predict whether a state or county’s Gini Coefficient is above or below the national median. Pulling the majority of their data from US Federal Government sources like the US Census, their goal was to better understand how and why America’s domestic features made its Gini Coefficient significantly higher than that of the other G7 countries (0.47 to 0.33), and they found that race features were the most successful at predicting income inequality, specifically the proportion of the black and white population alone in a Random Forest Classifier yielded an accuracy of 96% on determining whether a region was above or below the median national Gini Coefficient.

About using the Gini Coefficient to predict economic growth in Dutt and Tsetlin’s work at the INSEAD Singapore Business school, the authors found that the fraction of the population living in poverty was much more accurate in predicting economic growth measures such as “schooling, institutional quality, and per capita income” than the Gini Coefficient. They noted that the poverty measures are influenced by those in the bottom economic ring of society, whereas the Gini coefficient is equally influenced by both sides of the economic spectrum, and recommended on focusing on alleviating poverty at the bottom over addressing a country’s income inequality as a policy approach for increasing economic development.

These literature reviews are important because while the Gini Coefficient provides a wealth of information on a country’s economic condition, they do not provide the whole picture and as a result, our group would like to note our results does not claim to offer a perfect solution to this complex issue.

### Expected Results from Supervised Methods - Jing Xi

* Linear Regression: attempt to find a direct relationship between these parameters and the Gini coefficient. However, this would not be able to capture complex or non-linear relationships 
* Neural Networks: attempts to capture complex relationships without extensive effort on feature engineering. However, it might be prone to overfitting, especially since our dataset is small.
