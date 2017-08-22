# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 17:50:50 2017

@author: MI5022414
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=1/3,random_state=0)

# Simple Linear Regression !
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)

plt.scatter(X_train,y_train,color = 'red')
plt.plot(X_train,lr.predict(X_train),color = 'blue')
plt.title("Years of Experience vs Salary ('Training Set')")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()

plt.scatter(X_test,y_test,color = 'red')
plt.plot(X_train,lr.predict(X_train),color = 'blue')
plt.title("Years of Experience vs Salary ('Test Set')")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()
