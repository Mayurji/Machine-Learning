# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:17:29 2017

@author: MI5022414
"""

# Five methods of Buliding a Model
'''
1. ALL-IN
    Keeping all the attributes or feature for prediction
    
# stepwise regression starts

2. Backward Elimination
    
    s1. select a significance level  to stay in the model (SL = 0.05)
    s2. Fit the full model with all predictor
    s3. Consider the predictor  with the highest P-value. If P > SL, go to step 4 otherwise
        go to FIN
    s4. Remove the predictor
    s5. Fit the model without this variable & Go back to s3.
    
    FIN - Finish i.e. the model is ready !
    
3. Forward Selection
    
    s1. select a significance level  to stay in the model (SL = 0.05)
    s2. Fit all the simple regression model y ~ X(sub n). Select the one with the lowest
        P-value.
    s3. Keep this variable and fit all the possible models with one extra predictor
        added to the one already have
    s4. consider the predictor with the lowest p-value. If  p < SL, go to step 3 , 
        otherwise go to FIN
    
4. Bidirectional Elimination

    s1. select a significance level  to stay in the model (SLENTER = 0.05 and SLSTAY = 0.05)
    s2. Perform the next steps of forward selection (new variables must have: p < SLENTER to enter)
    s3. Perform the all steps of backward Elimination (old variables must have: p < SLSTAY to stay)
        iterate between s2 and s3
    s4. No new variable to enter and no old variable to exit
    
        FIN model is ready !
    
    
# stepwise regression ends

ALL possible models:
    
    s1. Select a criterion of goodness of fit (eg. Akaike criterion)
    s2. Construct all possible regression models: 2^N - 1 total combinations
    s3. Select the one with best criterion
    
    FIN Model is ready !
    
    EG: 10 columns with 1023 models  

5. Score Comparsion
'''
# Multiple Linear Regression 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('50_startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

from sklearn.preprocessing import LableEncoder , OneHotEncoder
le_X = LabelEncoder()
X[:,3] = le_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()
      
# To Avoid Dummy variable trap,we are dropping one dummy variable !
X = X[:,1:]
          
from sklearn.cross_validation import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X_train,y_train)
y_pred = lr.predict(X_test)


'''
Multiple Linear Regression

y = b0X0+b1X1....+bnXn
normally X0 wont be present, whose value is 1.To include the coeff. b0 in statsmodels
we need to include X0 by adding that column in X 


'''
#Buliding optimal Model Using Backward Elimination

import statsmodels.formula.api as sm
X = np.append(arr=np.ones((50,1)).astype(int),values = X, axis=1)
X_opt = X[:,[0,1,2,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()
# We removed index = 2 because the column will have p value > that significance value of 0.05
X_opt = X[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(endog = y,exog = X_opt).fit()
regressor_OLS.summary()















































