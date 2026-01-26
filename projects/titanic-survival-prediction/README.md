# Titanic Survival Prediction

## Problem Statement
The goal of this project is to predict passenger survival on the Titanic
using demographic and travel-related features.

## Dataset
- Source: Kaggle – Titanic: Machine Learning from Disaster
- Type: Binary classification
- Target: Survived (0 = No, 1 = Yes)

## Approach
- Data inspection and handling missing values
- Dropping high-missing columns (Cabin)
- Encoding categorical features using one-hot encoding
- Feature scaling
- Model training using:
  - Logistic Regression
  - Random Forest Classifier
- Model evaluation using Precision, Recall, F1-score
- Cross-validation for reliable performance estimation

## Results
Random Forest outperformed Logistic Regression by capturing non-linear
feature interactions, while Logistic Regression provided a strong baseline.

## Key Learnings
- Handling real-world messy data
- Encoding categorical variables correctly
- Importance of stratified splitting and cross-validation
- Building a complete Kaggle-style ML pipeline

