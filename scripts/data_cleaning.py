import pandas as pd

#Load the dataset
file_path = '/Users/parsabahrami/Customer Churn Model/data/data.csv'

data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure.
print("Initial data preview:\n", data.head())

# Check for any missing values in the dataset columns.
print("Missing Values:\n", data.isnull().sum())

# Fill missing values using appropriate strategies for each column
# 'Geography' is a categorical column, so fill missing values with the most frequent value (mode).
data['Geography'].fillna(data['Geography'].mode()[0], inplace=True)

# 'Age' is a numerical column, so fill missing values with the median to minimize the effect of outliers.
data['Age'].fillna(data['Age'].median(), inplace=True)

# 'HasCrCard' and 'IsActiveMember' are binary columns (0 or 1), so fill missing values with the mode.
data['HasCrCard'].fillna(data['HasCrCard'].mode()[0], inplace=True)
data['IsActiveMember'].fillna(data['IsActiveMember'].mode()[0], inplace=True)

# Convert 'HasCrCard' and 'IsActiveMember' to integer type
# Since these columns are binary (0 or 1), it's best to convert them to integers.
data['HasCrCard'] = data['HasCrCard'].astype(int)
data['IsActiveMember'] = data['IsActiveMember'].astype(int)

# Verify that there are no more missing values
# After cleaning, confirm that there are no more missing values in the dataset.
print("Missing Values after cleaning:\n", data.isnull().sum())

# Print the data types of all columns to ensure they're appropriate for the model.
print("\nColumn Data Types:\n", data.dtypes)

# We'll use the Interquartile Range (IQR) method to cap outliers in numerical columns.
def cap_outliers(df, column):
    """
    This function caps outliers in the specified column using the IQR method.
    Any value below Q1 - 1.5 * IQR or above Q3 + 1.5 * IQR is capped.
    """
    Q1 = df[column].quantile(0.25)  # First quartile (25th percentile)
    Q3 = df[column].quantile(0.75)  # Third quartile (75th percentile)
    IQR = Q3 - Q1                   # Interquartile Range
    lower_bound = Q1 - 1.5 * IQR     # Lower bound for outliers
    upper_bound = Q3 + 1.5 * IQR     # Upper bound for outliers
    # Cap the values outside of this range
    df[column] = df[column].clip(lower_bound, upper_bound)

# Cap outliers in the 'Age', 'CreditScore', and 'Balance' columns using the cap_outliers function.
cap_outliers(data, 'Age')
cap_outliers(data, 'CreditScore')
cap_outliers(data, 'Balance')

# Check summary statistics for the numerical columns after handling outliers.
print("\nSummary statistics after handling outliers:\n", data[['Age', 'CreditScore', 'Balance']].describe())


# The 'RowNumber', 'CustomerId', and 'Surname' columns are unnecessary for the prediction model, so remove them.
data_cleaned = data.drop(columns=['RowNumber', 'CustomerId', 'Surname'])

# Display the first few rows of the cleaned dataset to ensure everything is in order.
print("\nData preview after removing unnecessary columns:\n", data_cleaned.head())

# Save the cleaned dataset as a new CSV file for further use in the modelling process.
cleaned_file_path = '/Users/parsabahrami/Customer Churn Model/data/cleaned_data.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

# Confirmation message that the data cleaning is complete
print(f'\nData cleaning complete. Cleaned file saved at {cleaned_file_path}')
