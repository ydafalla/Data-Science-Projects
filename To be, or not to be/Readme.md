
To be, or not to be
==============================

Classification


## Introduction:
The project is about building one or more classification models to determine the player using the other columns as features. The dataset contains all of Shakespeare's plays.The player is going to be classified based on the play, ActSceneLine and the PlayerLine.

The data was obatined from the following link:

https://www.kaggle.com/kingburrito666/shakespeare-plays

The data contains one csv file "Shakespaeare_data.csv".

## Approach:

### 1. Feature Engineering
The basic approach is to use TF-IDF vectorization to get the frequency of the words in the playerline. TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. It is often used as a weighting factor in searches of information retrieval, text mining, and user modeling. 


### 2. Modeling
Three different models were implemented that resulted in the following accuracies:

#### Decision Tree Classification
Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression. Decision trees learn from data to approximate a sine curve with a set of if-then-else decision rules.

Accuracy of Decision Tree classifier on test set: 0.74

#### K-nearest Neighbour Classifier
The k-nearest neighbors (KNN) algorithm is a simple, easy-to-implement supervised machine learning algorithm that can be used to solve both classification and regression problems. The KNN algorithm assumes that similar things exist in close proximity. In other words, similar things are near to each other.

Accuracy of K-NN classifier on test set: 0.65

#### Naive Bayes Classifier
Naive Bayes classifiers are a collection of classification algorithms based on Bayes’ Theorem. It is not a single algorithm but a family of algorithms where all of them share a common principle, i.e. every pair of features being classified is independent of each other.

Accuracy of Naive bayes classifier on test set: 0.65


## Conclusion:

We converted the PlayerLine into different Vectors using TFIDF vectorization and used play, ActSceneLine and the PlayerLine columns to classify the players.

We were getting more accuracy when using the classifier model Decision tree compared to k-nearest neighbour and anive bayes classifiers.

Accuracy of Decision Tree classifier on test set: 0.74

Accuracy of K-NN classifier on test set: 0.65

Accuracy of Naive bayes classifier on test set: 0.65

