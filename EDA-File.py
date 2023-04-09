# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Previewing Dataset
df = pd.read_csv('supermarket_sales.csv')
df.head(10)

#To check all column headers data types

df.columns   
df.dtypes

# Type casting date format to a correct format
df['Date'] = pd.to_datetime(df['Date'])

# Setting Date as Index`
df.set_index('Date',inplace = True)
df.head()

# Dataset summary statistics
df.describe()

# Checking for Duplicates
df.duplicated()

# Checking for Missing/Null
df.isna().sum()
sns.heatmap(df.isnull(),cbar = False) # Heatmap to check null/missing values

# Checking distribution for Rating 
sns.distplot(df['Rating'])
plt.axvline(x = np.mean(df['Rating']), c = 'red' ,ls ='--', label = 'mean')
plt.axvline(x = np.percentile(df['Rating'],25), c = 'green', ls ='--', label = '25-75th percentile')
plt.axvline(x = np.percentile(df['Rating'],75), c = 'green', ls ='--', label = '--')
plt.legend()

# Histogram for individual categorical value
df.hist(figsize = (10,10))

# Aggregate sales for each Supermarket branch
sns.countplot(df['Branch'])
df['Branch'].value_counts()

# Checking Popular payment methods
sns.countplot(df['Payment'])
df['Payment'].value_counts()

# Relationship between gross income and customer rating
sns.regplot(df['Rating'],df['gross income'])

# Relationship between Branch and customer rating
sns.boxplot(x = df['Branch'],y = df['gross income'])

# Correlation matrix for each categorical value
np.round(df.corr(),2)

sns.heatmap(np.round(df.corr(),2),annot = True) # Heatmap for Correlation 
