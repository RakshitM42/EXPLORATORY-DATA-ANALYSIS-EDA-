# EXPLORATORY-DATA-ANALYSIS (EDA) – Supermarket Retail Chain

### About Dataset
The growth of supermarkets in most populated cities are increasing and market competitions are also high. The dataset is one of the historical sales of supermarket company which has recorded in 3 different branches for 3 months data.

The dataset used for this project :- https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales

EDA for a superstore data in different locations and analyzing their respective profits , customer feedback and ratings


### Data Dictionary

   **Invoice id:** Computer generated sales slip invoice identification number.
   
   **Branch:** Branch of supercenter (3 branches are available identified by A, B and C).
   
   **City:** Location of supercenters.

   **Customer type:** Type of customers, recorded by Members for customers using member card and Normal for without member card.

   **Gender**: Gender type of customer

   **Product line:** General item categorization groups - Electronic accessories, Fashion accessories, Food and beverages, Health and beauty, Home and lifestyle,
                     Sports and travel

   **Unit price:** Price of each product in USD

   **Quantity:** Number of products purchased by customer

   **Tax:** 5% tax fee for customer buying

   **Total:** Total price including tax

   **Date:** Date of purchase (Record available from January 2019 to March 2019)

   **Time:** Purchase time (10am to 9pm)

   **Payment:** Payment used by customer for purchase (3 methods are available Cash, Credit card and E-wallet)

   **COGS:** Cost of goods sold

   **Gross margin percentage:** Gross margin percentage                                                                                                                 

   **Gross income:** Gross income              

   **Rating:** Customer stratification rating on their overall shopping experience (On a scale of 1 to 10)
   
## _1 - Initial Data Exploration_
### 1.1 Importing Libraries
**Seaborn –** Data visualization library        
**Pandas –** Data manipulation library        
**NumPy -** scientific computing library      
**Matplotlib** – Data visualization library     
 
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

```
### 1.2 Importing & Previewing Dataset
```
df = pd.read_csv('supermarket_sales.csv')
df.head(10)
```
<img src="https://user-images.githubusercontent.com/102774633/230661228-31757942-71ca-4067-ad88-5441a4c42728.png" width="900" height="300">

To check all column headers

```
df.columns                                                                                              `
```


**Index**(['Invoice ID', 'Branch', 'City', 'Customer type', 'Gender',
       'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Total', 'Date',
       'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income',
       'Rating'],
      dtype='object')            
      
To check data types for each column header      
```
df.dtypes
```
**Invoice ID**    -                  object      
**Branch**  -                        object      
**City**  -                          object       
**Customer type**    -               object      
**Gender**    -                      object      
**Product line**     -               object       
**Unit price**      -                float64     
**Quantity**    -                    float64     
**Tax 5%**       -                   float64     
**Total**        -                   float64     
**Date**        -                    object     
**Time**         -                   object     
**Payment**      -                   object     
**cogs**         -                   float64     
**gross margin percentage**   -      float64
**gross income**    -                float64     
**Rating**        -                  float64    
**dtype**:   object      

Here, the data type for **Date** is "float64", which has to be correctly formatted in **datetime** format.

#### To Convert Data Type for **Date**
```
df['Date'] = pd.to_datetime(df['Date'])
```
```
df.dtypes
```
**Invoice ID**    -                  object      
**Branch**  -                        object      
**City**  -                          object       
**Customer type**    -               object      
**Gender**    -                      object      
**Product line**     -               object       
**Unit price**      -                float64     
**Quantity**    -                    float64     
**Tax 5%**       -                   float64     
**Total**        -                   float64     
**Date**        -                    datetime64[ns]     
**Time**         -                   object                           
**Payment**      -                   object                        
**cogs**         -                   float64                      
**gross margin percentage**   -      float64            
**gross income**    -                float64                                    
**Rating**        -                  float64                                                
**dtype**:   object                                 

The date format time has been converted to **datetime**  
### 1.3 To set Date as Index
````
df.set_index('Date',inplace = True)
df.head()
````
<img src="https://user-images.githubusercontent.com/102774633/230660903-d4d4d2f4-378a-4756-acb3-1e270ede5271.png" width="900" height="300">

### 1.4 To Check summary statistics

```
df.describe()
```
<img src="https://user-images.githubusercontent.com/102774633/230661441-3c08a519-236c-4029-b05b-2fe4ad582bb7.png" width="900" height="300">

## _2 - Univariate Analysis_
### **2.1 To check distribution of customer Ratings**
```
sns.distplot(df['Rating'])
plt.axvline(x = np.mean(df['Rating']), c = 'red' ,ls ='--', label = 'mean')
plt.axvline(x = np.percentile(df['Rating'],25), c = 'green', ls ='--', label = '25-75th percentile')
plt.axvline(x = np.percentile(df['Rating'],75), c = 'green', ls ='--', label = '--')
plt.legend()
```
<img src="https://user-images.githubusercontent.com/102774633/230661556-b5f8e3f4-6584-447a-8122-4689aa349f6c.png" width="500" height="300">     

The customer rating distribution is somewhat uniform in distribution and the plot is not skewed towards either end.

### **2.2 To Plot histograms for indvidual categorical value**

```
df.hist(figsize = (10,10))
```

<img src="https://user-images.githubusercontent.com/102774633/230661736-5f0bff5a-7872-477a-9917-ca0f910e65b7.png" width="700" height="500">      



#### Highlights -

Tax, Gross income, COGS and Total histogram is right skewed with the distribution.
Gross Margin plot shows a single line that implies, gross margin is constant throughout

### **2.3 To check Aggregate sales for each branch** 


 ```
 sns.countplot(df['Branch'])
 ```
 
<img src="https://user-images.githubusercontent.com/102774633/230661558-185eccfe-fa0a-40d4-89a3-7ab027dd18a5.png" width="500" height="300">     

 ```
 df['Branch'].value_counts()
 
 ```
A      340                                                                                                                                                             
B      332                                                                                                                                                             
C      328                                                                                                                                                             

**Highlights** -                                                        
Branch **A** has the highest aggregate sales among all other branches

### **2.4 To Check Most popular payment methods being used**

```
sns.countplot(df['Payment'])
```
<img src="https://user-images.githubusercontent.com/102774633/230661560-51f62675-f029-4c27-ab41-8ea2a754b99d.png" width="500" height="300">    

To Find the value of each payment method

```
df['Payment'].value_counts()

```
Ewallet  -             345                                                                                                                                                                                             
Cash     -             344                                                                                                                                                                                                   
Credit card   -        311                                                                                                                                                                                             
Name: Payment, dtype: int64                                                                                                                                        

**Highlight** -                                          
Ewallet is the most popular mode of payment 

## _3 - Bivariate Analysis_

### **3.1 To Check relationship between gross income and customer rating**

```
sns.regplot(df['Rating'],df['gross income'])
```

<img src="https://user-images.githubusercontent.com/102774633/230692504-74b84ba8-a076-4cd4-bfbe-e786da8e148c.png" width="500" height="300">           

 **Highlight** -                                                                                                                                             
The trendline on the scatterplot plot is **flat** therefore, no relationship exists between gross income and customer rating

**3.2 To Check relationship between Branch and customer rating**

```
sns.boxplot(x = df['Branch'],y = df['gross income'])
```

<img src="https://user-images.githubusercontent.com/102774633/230692566-8c1eed59-4f6b-47fc-ab0a-d851e6b39733.png" width="500" height="300">           

**Highlight** -                                                                                                                                  
The boxplot graph between Branch and customer rating doesn't show any positive relationship.

## _4 - Duplicates Rows and Missing Values_
### **4.1 Duplicates**
#### To Check for duplicates in dataset
```
df.duplicated()
```
Date                                                                                                                                                                   
2019-01-05    False                                                                                                                                                   
2019-03-08    False                                                                                                                                                   
2019-03-03    False                                                                                                                                                   
2019-01-27    False                                                                                                                                                   
2019-02-08    False                                                                                                                                                   
              ...                                                                                                                                                     
2019-01-29    False                                                                                                                                                   
2019-03-02    False                                                                                                                                                   
2019-02-09    False                                                                                                                                                   
2019-02-22    False                                                                                                                                                   
2019-02-18    False                                                                                                                                                      Length: 1000, dtype: bool    
#### No Duplicates were found in the dataset

### **4.2 Missing/Null values**
#### To Check for Missing/Null in dataset

```
df.isna().sum()
```

Invoice ID    -             0                                                                                                                                        
Branch  -                   0                                                                                                                                        
City     -                  0                                                                                                                                        
Customer type    -          0                                                                                                                                        
Gender            -         0                                                                                                                                        
Product line       -        0                                                                                                                                        
Unit price          -       0                                                                                                                                        
Quantity             -      0                                                                                                                                        
Tax 5%                -     0                                                                                                                                        
Total                  -    0                                                                                                                                        
Time                    -   0                                                                                                                                        
Payment                  -  0                                                                                                                                        
cogs                      - 0                                                                                                                                        
gross margin percentage  -  0                                                                                                                                        
gross income     -          0                                                                                                                                        
Rating                  -   0                                                                                                                                        
dtype: int64                                                                                                                                        

#### Heatmap can also be used to check large datasets
```
sns.heatmap(df.isnull(),cbar = False)
```
<img src="https://user-images.githubusercontent.com/102774633/230696586-34bb22e4-3c6c-46f4-af2b-7d41211966d6.png" width="700" height="300">

#### No Null/Missing values were found in the dataset.

# _**5 - Correlation Analysis**_
### **5.1 To check the correlation between all the catogrical variables in the data set with correlation matrx**
```
np.round(df.corr(),2)
```
<img src="https://user-images.githubusercontent.com/102774633/230692624-59f766a1-f622-4247-8c8c-a2dbaee9ac75.png" width="900" height="300">

### **5.2 To check the correlation between all the catogrical variables in the data set with correlation Heatmap**
```
sns.heatmap(np.round(df.corr(),2),annot = True)
```
<img src="https://user-images.githubusercontent.com/102774633/230692670-c8e6139c-4777-42de-9034-f0137e6103e8.png" width="700" height="500">

