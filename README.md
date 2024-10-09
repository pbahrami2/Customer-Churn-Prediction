# Customer Churn Prediction Model

## Background and Overview

This project focuses on building a predictive model to forecast customer churn using machine learning techniques. The main objective is to identify customers who are likely to leave a service based on historical data, including demographic, account, and transactional information. This project demonstrates my technical skills in predictive analytics and forms part of my data analyst portfolio.

For technical details on data cleaning, feature engineering, and model training, refer to:
- [Data Cleaning Script](https://github.com/pbahrami2/Customer-Churn-Prediction-Model/blob/main/scripts/data_cleaning.py)
- [Feature Engineering Script](https://github.com/pbahrami2/Customer-Churn-Prediction-Model/blob/main/notebooks/features.ipynb)
- [Model Training and Evaluation](https://github.com/pbahrami2/Customer-Churn-Prediction-Model/blob/main/notebooks/modelling.ipynb)

## Data Structure Overview

The dataset, sourced from Kaggle, contains customer information and behavior that can be used to predict churn. It consists of the following key features:

- **Customer ID**: Unique identifier for each customer.
- **Credit Score**: A numerical representation of the customer’s credit score.
- **Geography**: Country where the customer resides (France, Spain, Germany).
- **Gender**: Customer's gender (Male or Female).
- **Age**: Customer's age.
- **Tenure**: Number of years the customer has been with the bank.
- **Balance**: Account balance of the customer.
- **NumOfProducts**: Number of products the customer uses (e.g., savings, credit card).
- **HasCrCard**: Whether the customer owns a credit card (1 = yes, 0 = no).
- **IsActiveMember**: Whether the customer is an active member (1 = yes, 0 = no).
- **EstimatedSalary**: Customer's estimated salary.
- **Exited**: Target variable indicating churn (1 = churned, 0 = not churned).

### Featured Dataset Columns

New features were created during the feature engineering phase:
- **Geography_Germany**: Binary indicator for customers residing in Germany.
- **Geography_Spain**: Binary indicator for customers residing in Spain.
- **Gender_Male**: Binary indicator for male customers.
- **Age_Tenure**: A new feature created by multiplying the customer’s age and tenure.
- **Balance_Products**: A new feature created by multiplying the balance and number of products the customer holds.

### Target Variable:
- **Exited**: The binary target variable where 1 indicates that the customer churned and 0 indicates that they did not churn.

### Dataset Source:
[Kaggle: Customer Churn Dataset](https://www.kaggle.com/datasets/shubhammeshram579/bank-customer-churn-prediction)

## Executive Summary

The Customer Churn Prediction Model leverages machine learning techniques to predict which customers are likely to churn. The project used feature engineering and hyperparameter tuning to build several models, with the **XGBoost model** achieving the best performance.

Key findings include:
- The XGBoost model achieved an **accuracy of 86%** and a **F1-score of 58%** for the churn class (Class 1).
- **Feature importance** analysis indicated that **Age**, **Tenure**, and **Balance** were strong predictors of customer churn.
- The **final model** can help businesses target high-risk customers and improve retention strategies by providing early warnings of potential churn.

## Insights Deep Dive

### 1. **Customer Demographics and Churn**
- **Metric**: Age, gender, and geography were key indicators of churn.
- **Finding**: Customers in the 40-60 age group, males, and those residing in Germany were more likely to churn.
- **Visualization**: Bar charts showing churn distribution across different demographic groups.

### 2. **Financial Indicators and Churn**
- **Metric**: Balance and number of products held by a customer.
- **Finding**: Customers with higher account balances and fewer products were more likely to churn.
- **Visualization**: Heatmaps and correlation matrices helped visualize relationships between churn and financial variables.

### 3. **Customer Activity and Churn**
- **Metric**: Active membership and credit card ownership.
- **Finding**: Active members with credit cards were less likely to churn.
- **Visualization**: Stacked bar charts highlighting churn behavior based on activity.

## Recommendations

Based on the findings from the churn prediction model, businesses can take action to reduce churn by:
- **Personalized Retention Strategies**: Use the model to target customers who are more likely to churn and offer tailored retention campaigns.
- **Increased Focus on Customer Engagement**: Encourage customer activity by promoting loyalty programs and rewarding frequent product usage.
- **Target High-Risk Groups**: Direct marketing efforts toward higher-risk demographics, such as older customers with lower product engagement.


## Models Used and Performance Metrics

The following models were trained and evaluated on accuracy, precision, recall, and F1-score:

1. **Logistic Regression**
   - **Accuracy**: 83%
   - **Precision (Class 1)**: 67%
   - **Recall (Class 1)**: 29%
   - **F1-Score (Class 1)**: 40%

2. **Random Forest (Hyper-tuned)**
   - **Accuracy**: 87%
   - **Precision (Class 1)**: 76%
   - **Recall (Class 1)**: 48%
   - **F1-Score (Class 1)**: 59%

3. **K-Nearest Neighbors (Hyper-tuned)**
   - **Accuracy**: 84%
   - **Precision (Class 1)**: 70%
   - **Recall (Class 1)**: 36%
   - **F1-Score (Class 1)**: 48%

4. **XGBoost (Final Model, Hyper-tuned)**
   - **Accuracy**: 87%
   - **Precision (Class 1)**: 74%
   - **Recall (Class 1)**: 51%
   - **F1-Score (Class 1)**: 60%

5. **Neural Network (MLP)**
   - **Accuracy**: 86%
   - **Precision (Class 1)**: 70%
   - **Recall (Class 1)**: 52%
   - **F1-Score (Class 1)**: 60%

### Final Model: XGBoost
- **Best Parameters**: `{'n_estimators': 100, 'max_depth': 5, 'learning_rate': 0.1, 'subsample': 1, 'colsample_bytree': 0.8}`
- **Cross-Validation Accuracy**: 86.24%
- **Cross-Validation F1-Score (Class 1 - Churn)**: 58.38%
