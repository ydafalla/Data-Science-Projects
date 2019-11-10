
World Wide Products Inc
==============================

Time Series Project


## Introduction:
The project is about building one or more forecasting models to determine the demand for a particular product using other columns as features. The dataset contains historical product demand for a manufacturing company with footprints globally. The company provieds thousands of products within dozens of product categories. 

The data was obatined from the following link:

https://www.kaggle.com/felixzhao/productdemandforecasting

The data contains one csv file "Historical Product Demand.csv".

## Approach:

### 1. Gradient Boosting
The basic approach is to use linear regression in order to predict the scores using other column features.
The columns used for building the linear regression model are:
1. spi1
2. spi2 
3. prob1 
4. prob2 
5. importance1
6. importance2
7. proj_score1
8. proj_score2
9. off_team1
10. off_team2
The mean absolute error, mean square error and the root squared error was calculated for the linear regression model.

### 2.Fbprophet
The basic approach is to use a random forest model in order to predict the scores using other column features.
The columns used for building the linear regression model are:
1. spi1
2. spi2 
3. prob1 
4. prob2 
5. importance1
6. importance2
7. proj_score1
8. proj_score2
9. off_team1
10. off_team2
The accuaracy of the model was calculated



## Discussion:
A linear regression model was built. The model predicts the scores of teams competing in a soccer game. 
For each score the Mean Absolute Error, Mean Squared Error and the Root Mean Squared Error was calculated.
The linear regression is used for predicting of continuous values and not discrete values so it might be problematic if used to predict the scores which are considered discrete values.
For this reason i decided to use one other models the random forest. It may be more appropriately used for predicting categorical data.



