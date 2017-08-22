#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 22:36:12 2017

@author: mayurjain
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()
      
# To Avoid Dummy variable trap,we are dropping one dummy variable !
X = X[:,1:]
          
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)


import statsmodels.formula.api as sm
X = np.append(arr=np.ones((50,1)).astype(int),values = X, axis=1)
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()
# We removed index = 2 because the column will have p value > that significance value of 0.05
X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:,[0,3]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X_opt,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)
y_pred2 = lr.predict(X_test)
