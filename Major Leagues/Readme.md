
Majour Leagues
==============================

Regression Project


## Introduction:
The project is about building a regression model to determine the score of each team in matches using other columns as features.

The data was obatined from the following link:

https://github.com/fivethirtyeight/data/tree/master/soccer-spi

The data are contained in the files spi_global_rankings.csv, spi_global_rankings_intl.csv, spi_matches.csv.

## Approach:
The basic approach is to use linear regression in order to predict the scores using other column features.
The columns used for building the linear regression model are:
1. spi1
2. spi2 
3. prob1 
4. prob2 
5. importance1
6. importance2
7. off_x

## Discussion:
A linear regression model was built. The model predicts the scores of teams competing in a soccer game. 
For each score the Mean Absolute Error, Mean Squared Error and the Root Mean Squared Error was calculated.
