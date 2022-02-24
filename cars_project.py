# -*- coding: utf-8 -*-
"""Cars Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Jgl-KEb7JFsAq1TCd16b28M_OsZWngqL

### **MACHINE LEARNING PROJECT**

**BY:**


**ATIQUE KONDVILKAR**

Importing Modules
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from scipy import stats
import pylab as pl
# %matplotlib inline

"""Reading CSV File"""

cars = pd.read_csv("/content/car data.csv")
cars

"""Checking For Null Values"""

cars.isnull().sum()

cars.info()

cars["Car_Name"].value_counts()

cars['car_age']= 2021-cars['Year']
cars

"""Using Box Plot & Finding Outlier"""

#Finding Outlier for first 150
plt.figure(figsize=(7,8))
sns.boxplot(data=cars.head(150),x="Selling_Price",y="Car_Name")
plt.grid()
plt.show()

# We found an outlier in corolla altis
cars[(cars["Car_Name"]=="corolla altis")&(cars["Selling_Price"]>12)]

# Found an outlier in ciaz
cars[(cars["Car_Name"]=="ciaz")&(cars["Selling_Price"]>8)]

# Removing the Outlier
id1=cars[(cars["Car_Name"]=="corolla altis")&(cars["Selling_Price"]>12)].index
cars.drop(id1,inplace=True)

id2=cars[(cars["Car_Name"]=="ciaz")&(cars["Selling_Price"]>8)].index
cars.drop(id2,inplace=True)

#Finding Outlier for remaining 144
plt.figure(figsize=(7,8))
sns.boxplot(data=cars.tail(144),x="Selling_Price",y="Car_Name")
plt.grid()
plt.show()

cars[(cars["Car_Name"]=="verna")&(cars["Selling_Price"]>9)]

id3=cars[(cars["Car_Name"]=="verna")&(cars["Selling_Price"]>9)].index
cars.drop(id3,inplace=True)

cars[(cars["Car_Name"]=="amaze")&(cars["Selling_Price"]>5)]

id3=cars[(cars["Car_Name"]=="amaze")&(cars["Selling_Price"]>5)].index
cars.drop(id3,inplace=True)

cars

#categorical Data
cars_cat = cars.select_dtypes(object)

#Numerical Data
cars_num = cars.select_dtypes(["float64","int64"])

cars_cat.head()

cars_num.head()

"""**Handling Categorical data and turning it to numerical**"""

cars_cat["Fuel_Type"].value_counts()

#One hot encoding
fuel_data = pd.get_dummies(cars_cat["Fuel_Type"])

fuel_data

from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()

le.fit_transform(cars_cat["Fuel_Type"])

Car_Name_data = pd.get_dummies(cars_cat["Car_Name"])
Car_Name_data

le.fit_transform(cars_cat["Car_Name"])

for col in cars_cat:
  le = LabelEncoder()
  cars_cat[col] = le.fit_transform(cars_cat[col])

cars_cat.head()

"""**Merging categorical and numerical column and creating new data for prediction**"""

cars_new = pd.concat([cars_num,cars_cat],axis=1)

cars_new.head()

cars_new.info()

"""**CONCLUSION**

1) We have done all the Algorithms of EDA and preprosessing

2) We had prepared the New data for ML algorithm i.e (cars_new)

3) We have 0 null values in and all the values are in NUMERICAL

**Spilliting Test And Train Values**
"""

X = cars_new.iloc[:, :-1].values
y = cars_new.iloc[:, -1].values
# Splitting the data into Train and Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""**# Algorithm 1- DecisionTree**"""

from sklearn.tree import DecisionTreeClassifier

Model = DecisionTreeClassifier()

Model.fit(X_train, y_train)

y_pred = Model.predict(X_test)

# Predictions made by the classifier
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Accuracy score
print('accuracy is',accuracy_score(y_pred,y_test))
print('accuracy in % is',accuracy_score(y_pred,y_test)*100)

"""**#Algorithm 2- RandomForest**"""

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=20)
model.fit(X_train, y_train)
y_pred=Model.predict(X_test)

model.score(X_test, y_test)

y_predicted = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predicted)
cm

print(classification_report(y_test,y_pred))

#Accuracy Score
print('accuracy is: ',accuracy_score(y_pred,y_test))
print('accuracy in percentage:',accuracy_score(y_pred,y_test)*100)

#Plotting Heat Map
plt.figure(figsize=(10,7))
sns.heatmap(cm, annot=True)
plt.xlabel('Truth')
plt.ylabel('Predicteed')

"""**CONCLUSION**

1) We have done all the Algorithms of EDA and preprosessing

2) We had prepared the New data for ML algorithm i.e (cars_new)

3) We have 0 null values in and all the values are in NUMERICAL

4)Seperating Test and Train values

5)Applying Decision Tree Algorithm:

  Accuracy in % is 91.52542372881356

6)Applying Random Forest Algorithm:

  Accuracy in percentage: 91.52542372881356
"""

