
Majour Leagues
==============================

Regression Project


## Introduction:
The project is about building a regression model to determine the score of each team in matches using other columns as features.

The data was obatined from the following link:

https://github.com/fivethirtyeight/data/tree/master/soccer-spi

The data are contained in the files spi_global_rankings.csv, spi_global_rankings_intl.csv, spi_matches.csv.

## Approach:
Exploratory data analysis and feature engineering were first performed before building two regression models. The regression models built were linear regression and random forest.

### 1. Linear Regression
The basic approach is to use linear regression in order to predict the scores using other column features.
The columns used for building the linear regression model are: (spi1, spi2, prob1 , prob2 , importance1, importance2, proj_score1, proj_score2, off_team1, off_team2)

The mean absolute error, mean square error and the root squared error was calculated for the linear regression model.
![Score1 Actual vs Predicted](Pictures/score1.png)
![Score2 Actual vs Predicted](Pictures/score2.png)

### 2. Ramdom Forest
The basic approach is to use a random forest model in order to predict the scores using other column features.
The columns used for building the linear regression model are: (spi1, spi2, prob1 , prob2 , importance1, importance2, proj_score1, proj_score2, off_team1, off_team2)
The accuaracy of the model was calculated and was around 33%.



## Discussion:
A linear regression model was built. The model predicts the scores of teams competing in a soccer game. 
For each score the Mean Absolute Error, Mean Squared Error and the Root Mean Squared Error was calculated.
The accuracy of the random forest model was calculated.


