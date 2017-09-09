#Data Preprocessing

# To read CSV

dataset = read.csv('Data.csv')

# To remove Missing value

dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x,na.rm = TRUE)),
                     dataset$Age)

# To Handle Categorical Data

dataset$Country = factor(dataset$Country,
                         levels = c('France','Spain','Germany'),
                         labels = c(1,2,3))

library(caTools)
# To keep same data without shuffling
set.seed(123)

split = sample.split(dataset$Purchased,SplitRatio = 0.8)

# Splitting data into test and train data
training_set = subset(dataset,split==TRUE)
test_set = subset(dataset,split==FALSE)

# Feature Scaling

training_set = scale(training_set)
test_set = scale(test_set)

training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])
