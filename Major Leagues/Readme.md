
Majour Leagues
==============================

Regression Project


## Introduction:
The project is about building a regression model to determine the score of each team in matches using other columns as features.

The data was obatined from the following link:

https://github.com/fivethirtyeight/data/tree/master/soccer-spi

The data are contained in the files spi_global_rankings.csv, spi_global_rankings_intl.csv, spi_matches.csv.

## Approach:

### 1. Linear Regression
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

### 2. Ramdom Forest
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

### 3. Decision tree classifier
The basic approach is to use a decison tree classfier in order to predict the scores using other column features.
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
The accuaracy of the model was calculated.

## Discussion:
A linear regression model was built. The model predicts the scores of teams competing in a soccer game. 
For each score the Mean Absolute Error, Mean Squared Error and the Root Mean Squared Error was calculated.
The linear regression is used for predicting of continuous values and not discrete values so it might be problematic if used to predict the scores which are considered discrete values.
For this reason i decided to use two other models the random forest and the decision tree model. They may be more appropriately used for predicting categorical data.



