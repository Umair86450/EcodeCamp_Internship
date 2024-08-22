# Titanic Survival Prediction

## Project Overview

The prediction of survival for passengers in the Titanic is a problem attempted using machine learning, which means taking features from this dataset and making a prediction of survival. This report tries to emphasis the methodology and its implementation in this research work, along with results.

## Objectives

**Predict Survival**: Build a model which can, based on the characteristics, predict whether a passenger survived or not.
**Feature Analysis**: Clearly identify and analyze which features have the most impact on survival rates.
**Model Evaluation**: Train various Machine learning models and find their accuracy.

## Dataset

In this project, we will be using the Titanic dataset provided by Kaggle. The different features involved in this dataset are the following:-

- `PassengerId`: It is the unique identifier for every passenger.
- `Pclass`: Class of ticket (1,2, or 3).
- `Name`: Name of the passenger.
- `Sex`: Sex of the passenger
- `Age`: Age of the passenger.
- `SibSp`: Number of siblings/spouses aboard.
- `Parch`: Number of parents/ children aboard.
- `Ticket`: Ticket number.
- `Fare`: Fare paid for the ticket.
- `Embarked`: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton).
- `Survived`: Whether the passenger survived (0 = No; 1 = Yes).

## Methodology

1. **Data Preprocessing**:
- Handle missing values.
- Convert categorical variables to numerical values.
- If required, normalize and scale features.

2. **Feature Engineering**:
- Creation of new features from the existing features like family size
- Encoding of categorical features

3. **Model Selection**:

   Train several models: Logistic Regression, Decision Trees, Random Forest
Compare models based on performance metric or model performance metrics: accuracy, precision, recall, F1 score.


4. **Model Evaluation**:

   Check for overfitting using cross-validation to ensure the model's robustness.
Measure the performance of the models on a validation set, then choose the best among the models.


5. **Deployment:**
- Design a web interface that allows users to feed in their data and obtain predictions.
- As the user inputs, make a prediction using the trained model.

## Results


- **Best Model:** The Random Forest classifier achieved the highest accuracy.
- **Feature Importance:** Key features influencing survival rates include Pclass, Sex, and Age.

## Conclusion

The Titanic Survival Prediction project then becomes quite effective in using machine learning to predict survival based on passenger characteristics. Among these, the random forest model was found most effective in making accurate predictions, and analysis for feature importance gives very useful insights into the factors that influence survival rates.

