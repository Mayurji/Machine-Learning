import unicodecsv
import random
import operator
import math

#getdata() function definition
def getdata(filename):
    with open(filename,'rb') as f:
        reader = unicodecsv.reader(f)
        return list(reader)

#random train test data split function definition
def shuffle(i_data):
    random.shuffle(i_data)
    train_data = i_data[:int(0.7*30)]
    test_data = i_data[int(0.7*30):]
    return train_data, test_data

def euclideanDist(x, xi):
    d = 0.0
    for i in range(len(x)-1):
        d += pow((float(x[i])-float(xi[i])),2)  #euclidean distance
    d = math.sqrt(d)
    return d

#KNN prediction and model training
def knn_predict(test_data, train_data, k_value):
    for i in test_data:
        eu_Distance =[]
        knn = []
        good = 0
        bad = 0
        for j in train_data:
            eu_dist = euclideanDist(i, j)
            eu_Distance.append((j[5], eu_dist))
            eu_Distance.sort(key = operator.itemgetter(1))
            knn = eu_Distance[:k_value]
            for k in knn:
                if k[0] =='g':
                    good += 1
                else:
                    bad +=1
        if good > bad:
            i.append('g')
        elif good < bad:
            i.append('b')
        else:
            i.append('NaN')

#Accuracy calculation function
def accuracy(test_data):
    correct = 0
    for i in test_data:
        if i[5] == i[6]:
            correct += 1
    accuracy = float(correct)/len(test_data) *100  #accuracy 
    return accuracy

dataset = getdata('/Users/mayurjain/Documents/Machine Learning Algorithms/KNN 1/ionosphere.data')  #getdata function call with csv file as parameter
train_dataset, test_dataset = shuffle(dataset) #train test data split
K = 5# Assumed K value
knn_predict(test_dataset, train_dataset, K)   
#print(test_dataset)
print("Accuracy : ",accuracy(test_dataset))