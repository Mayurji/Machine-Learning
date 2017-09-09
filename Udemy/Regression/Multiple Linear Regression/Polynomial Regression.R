dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

# fitting linear regression on dataset
lin_reg = lm(formula = Salary ~ .,data = dataset)
summary(lin_reg)

# fitting Polynomial regression on dataset
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
poly_reg = lm(formula = Salary ~ .,data = dataset)
summary(poly_reg)

# Visualising using linear regression

library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level,y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(lin_reg,newdata = dataset)),colour = 'blue')+
  ggtitle("Position vs Salary (Linear Regression)") +
  xlab('Level')+
  ylab('Salary')

# Visualising using polynomial regression

library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level,y = dataset$Salary),
             colour = 'red') +
  geom_line(aes(x = dataset$Level, y = predict(poly_reg,newdata = dataset)),colour = 'blue')+
  ggtitle("Position vs Salary (Polynomial Regression)") +
  xlab('Level')+
  ylab('Salary')


# Prediction in Linear Regression
y_pred = predict(lin_reg,data.frame(Level = 6.5))

# Prediction in Polynomial Regression
y_pred = predict(poly_reg,data.frame(Level = 6.5,Level2 = 6.5^2,Level3 = 6.5^3,Level4 = 6.5^4))
