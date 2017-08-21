# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importing Dataset
dataset = pd.read_csv('Advertising.csv',index_col='Unnamed: 0')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,5].values

# Removing Missing data with Mean or any other                 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN",strategy="mean",axis=0)
imputer = imputer.fit(X[:,:3])
X[:,:3] = imputer.transform(X[:,:3])

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder
labelEncoder_y = LabelEncoder()
y = labelEncoder_y.fit_transform(y)

#Dummy Encoding since value of country is not quantifyiable

# make Four seperate variable
from sklearn.preprocessing import OneHotEncoder
onehotencoder = OneHotEncoder(categorical_features = [4] )
X = onehotencoder.fit_transform(X)

from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

#Feature Scaling

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)