import pandas as pd

# Read the data from the file datset.xlsx
df = pd.read_csv("./dataset.csv")

# Print Number of missing values in each column
missing_values = df.isnull().sum()
print(missing_values)

# Drop Description column
df_dropped = df.drop(columns=['Description'])

# Print Number of missing values in each column after removing non-numeric columns
print("\nMissing values in the dataframe after dropping Description column:")
missing_values = df_dropped.isnull().sum()
print(missing_values)

# Impute missing values in the CustomerId with mean
df_dropped['CustomerID'] = df_dropped['CustomerID'].fillna(df['CustomerID'].mean())

# Print Number of missing values in each column after imputing CustomerID column
print("\nMissing values in the dataframe after imputing CustomerID column:")
missing_values = df_dropped.isnull().sum()
print(missing_values)

# Print the number of duplicate rows in the dataframe
duplicate_rows = df_dropped.duplicated().sum()
print("\nNumber of duplicate rows in the dataframe:", duplicate_rows)

# Remove duplicate rows from the dataframe
df_dropped_duplicates = df_dropped.drop_duplicates()

# Print the number of duplicate rows in the dataframe after removing duplicates
duplicate_rows = df_dropped_duplicates.duplicated().sum()
print("\nNumber of duplicate rows in the dataframe after removing duplicates:", duplicate_rows)

# Remove non-numeric columns
df_dropped_duplicates_numeric_only = df_dropped.select_dtypes(include=['float64', 'int64'])

# Detect and print the outliers in the dataframe
Q1 = df_dropped_duplicates_numeric_only.quantile(0.25)
Q3 = df_dropped_duplicates_numeric_only.quantile(0.75)
IQR = Q3 - Q1
outliers = ((df_dropped_duplicates_numeric_only < (Q1 - 1.5 * IQR)) | (df_dropped_duplicates_numeric_only > (Q3 + 1.5 * IQR))).sum()
print("\nOutliers in the dataframe:")
print(outliers)

# Remove the outliers from the dataframe
df_no_outliers = df_dropped_duplicates_numeric_only[~((df_dropped_duplicates_numeric_only < (Q1 - 1.5 * IQR)) | (df_dropped_duplicates_numeric_only > (Q3 + 1.5 * IQR))).any(axis=1)]

# Print the shape of the dataframe after removing outliers
print("\nShape of the dataframe after removing outliers:", df_no_outliers.shape)

# Generate summary statistics of the dataframe
summary_statistics = df_no_outliers.describe()
print("\nSummary statistics of the dataframe:")
print(summary_statistics)

# Plot histogram for numerical features and bar plot for categorical features
import matplotlib.pyplot as plt

# # Plot bar plot for categorical features
# categorical_columns = df.select_dtypes(include=['object']).columns
# for column in categorical_columns:
#     df[column].value_counts().plot(kind='bar')
#     plt.title(column)
#     plt.show()
    
# Plot histogram for numerical features
df_no_outliers.hist()
plt.show()