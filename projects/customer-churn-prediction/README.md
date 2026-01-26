# Customer Churn Prediction

## Problem Statement
The objective of this project is to predict whether a customer will churn
based on demographic and usage-related features.

## Dataset
- Type: Binary classification dataset
- Features: Age, Monthly Charges, Tenure
- Target: Churn (0 = No, 1 = Yes)

## Approach
- Data inspection and class balance analysis
- Feature scaling
- Model training using:
  - Logistic Regression
  - Decision Tree Classifier
  - Random Forest Classifier
- Model evaluation using Precision, Recall, and F1-score
- Cross-validation and hyperparameter tuning

## Results
Logistic Regression provided a stable baseline, while Random Forest
performed better by capturing non-linear patterns in the data.

## Key Learnings
- Why accuracy is not sufficient for imbalanced datasets
- Importance of Precision, Recall, and F1-score
- Bias–Variance tradeoff in classification models
- Model comparison based on evaluation metrics

