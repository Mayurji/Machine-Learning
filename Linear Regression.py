import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

def get_data(fileName):
    data = pd.read_csv(fileName)
    x_param = []
    y_param = []
    for single_square_feet ,single_price_value in zip(data['square_feet'],data['price']):
        x_param.append([float(single_square_feet)])
        y_param.append(float(single_price_value))
    return x_param,y_param

def linear_model_main(X_parameters,Y_parameters,predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions

def show_linear_line(x_pa,y_pa):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(x_pa, y_pa)
    plt.scatter(x_pa,y_pa,color='blue')
    plt.plot(x_pa,regr.predict(x_pa),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()

x,y = get_data('/Users/mayurjain/Documents/Machine Learning Algorithms/Linear Regression/inputdata.csv')
predict_value = 700
result = linear_model_main(x,y,predict_value)
print("Intercept value " , result['intercept'])
print("coefficient" , result['coefficient'])
print("Predicted value: ",result['predicted_value'])
show_linear_line(x,y)