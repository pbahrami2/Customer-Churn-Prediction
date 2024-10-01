# Churn Prediction Model Project

## Project Overview

This project focuses on developing a predictive model to forecast customer churn based on historical data. The primary objective is to build an accurate model that can identify customers who are likely to churn, using machine learning techniques. The model is included in my personal data analyst portfolio to showcase my technical skills and ability to work with predictive analytics.

## Dataset

The dataset used in this project was sourced from Kaggle and focuses on customer churn prediction. The dataset contains various features related to customer demographics, account information, and activity, which are used to predict whether a customer will churn.

### Original Dataset Features:

The original dataset contains the following features:

- **Customer ID**: A unique identifier for each customer.
- **Surname**: The customer's surname or last name.
- **Credit Score**: A numerical value representing the customer's credit score.
- **Geography**: The country where the customer resides (France, Spain, or Germany).
- **Gender**: The customer's gender (Male or Female).
- **Age**: The customer's age.
- **Tenure**: The number of years the customer has been with the bank.
- **Balance**: The customer's account balance.
- **NumOfProducts**: The number of bank products the customer uses (e.g., savings account, credit card).
- **HasCrCard**: Whether the customer has a credit card (1 = yes, 0 = no).
- **IsActiveMember**: Whether the customer is an active member (1 = yes, 0 = no).
- **EstimatedSalary**: The estimated salary of the customer.
- **Exited**: Whether the customer has churned (1 = yes, 0 = no).

### Featured Dataset Columns:

- **CreditScore**: A numerical value representing the customer's credit score.
- **Age**: The customer's age.
- **Tenure**: The number of years the customer has been with the bank.
- **Balance**: The customer's account balance.
- **NumOfProducts**: The number of bank products the customer uses.
- **HasCrCard**: Whether the customer has a credit card (1 = yes, 0 = no).
- **IsActiveMember**: Whether the customer is an active member (1 = yes, 0 = no).
- **EstimatedSalary**: The estimated salary of the customer.
- **Exited**: Whether the customer has churned (1 = yes, 0 = no).
- **Geography_Germany**: A binary indicator (1 = the customer resides in Germany, 0 = otherwise).
- **Geography_Spain**: A binary indicator (1 = the customer resides in Spain, 0 = otherwise).
- **Gender_Male**: A binary indicator (1 = Male, 0 = Female).
- **Age_Tenure**: A new feature created by multiplying the age and tenure of the customer.
- **Balance_Products**: A new feature created by multiplying the balance and number of products the customer holds.

### Target Variable:

- **Exited**: This column is the target variable, where 1 indicates the customer has churned and 0 indicates the customer has not churned.

### License:

The dataset is free to use for educational purposes and personal projects.

### Dataset Source:

Kaggle: Customer Churn Dataset  
[Link to dataset](https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction)

## Project Files

- **EDA.ipynb**: Exploratory Data Analysis - Contains initial analysis and visualizations to understand the data.
- **features.ipynb**: Feature Engineering - Includes transformations, scaling, and handling of categorical features.
- **modelling.ipynb**: Model Training and Hyperparameter Tuning - Contains code to train multiple machine learning models, hyper-tuning, and final model selection.
- **data_cleaning.py**: Python script used to clean and preprocess the data.

## Models Used

1. **Logistic Regression**
2. **Random Forest (Hyper-tuned)**
3. **K-Nearest Neighbors (Hyper-tuned)**
4. **XGBoost (Final Model, Hyper-tuned)**
5. **Neural Network (MLP)**

The models were compared based on accuracy, precision, recall, and F1-score.

### Final Model: XGBoost

- **Best Parameters**: `{'n_estimators': 100, 'max_depth': 5, 'learning_rate': 0.1, 'subsample': 1, 'colsample_bytree': 0.8}`
- **Cross-Validation Accuracy**: 86.24%
- **Cross-Validation F1-Score (Class 1 - Churn)**: 58.38%

### Model Performance Metrics

The XGBoost model outperformed other models and showed a good balance of precision, recall, and F1-score. Cross-validation was used to assess model generalization.

- **Accuracy**: 86%
- **Precision (Class 1 - Churn)**: 76%
- **Recall (Class 1 - Churn)**: 47%
- **F1-Score (Class 1 - Churn)**: 58%
