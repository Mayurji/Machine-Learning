from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import scipy as sp
import nltk.stem
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import KFold
english_stemmer = nltk.stem.SnowballStemmer('english')
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from DateTime import DateTime
import csv
import pandas as pd
import os
import re
from os import path
from Email_Classifier import GeneratingDataSet
from Email_Classifier import fetchEmails

gds = GeneratingDataSet()

global bodyword
global subjectword
global X_trained_
global datetimevalue
global time
global formattedDateTime
time = []
subjectword = []
datetimevalue = []
formattedDateTime = []

# def convertDateTimeFormat(timestamp):
#     print(timestamp[0])
#     for i in range(len(timestamp)):
#         if '-' in timestamp[0][i]:
#             splitTZ = timestamp[0][i].split('-')
#             y = DateTime(splitTZ[0])
#             x = [y.parts()]
#             dateval = int(str(x[0][0])+str(x[0][1])+str(x[0][2])+str(x[0][3]))#+str(x[0][4])+str(x[0][5]))
#             datetimevalue.append(dateval)
            
#         elif '+' in timestamp[0][i]:
#             splitTZ = timestamp[0][i].split('+')
#             y = DateTime(splitTZ[0])
#             x = [y.parts()]
#             dateval = int(str(x[0][0])+str(x[0][1])+str(x[0][2])+str(x[0][3]))#+str(x[0][4])+str(x[0][5]))
#             datetimevalue.append(dateval)
        
#         else:
#             datetimevalue.append(timestamp)
    
#     return datetimevalue

def DateTimeFormat(time):
    
    dayhours = ['0','1','2','3','4','5','6','7','8','9']
    months = ['1','2','3','4','5','6','7','8','9']
    days = ['1','2','3','4','5','6','7','8','9']
    minus = '-'
    addition = '+'

    for i in range(len(time)):
        print(time[i])
        if '-' in time[i]:
            splitTZ = time[i].split('-')
            y = DateTime(splitTZ[0])
            x = [y.parts()]
            month = str(x[0][1])
            day = str(x[0][2])
            hours = str(x[0][3])
            if month in months:
                month = '0'+month
                #return month
            if day in days:
                day = '0'+day
                #return day
            if hours in dayhours:
                hours = '0'+hours

            formattedDateTime.append(int(str(x[0][0])+month+day+hours))
            
        elif '+' in time[i]:
            splitTZ = time[i].split('+')
            y = DateTime(splitTZ[0])
            x = [y.parts()]
            month = str(x[0][1])
            day = str(x[0][2])
            hours = str(x[0][3])
            if month in months:
                month = '0'+month
                #return month
            if day in days:
                day = '0'+day
                #return day
            if hours in dayhours:
                hours = '0'+hours

            formattedDateTime.append(int(str(x[0][0])+month+day+hours))

    return formattedDateTime
def distMatrix(v1,v2):
    v1_norm = v1/sp.linalg.norm(v1.toarray())
    v2_norm = v2/sp.linalg.norm(v2.toarray())
    delta = v1_norm - v2_norm
    return sp.linalg.norm(delta.toarray())


def similarityMatrixBody(bodyList):
    vec = TfidfVectorizer(min_df=1,stop_words = 'english',decode_error='ignore',analyzer='word',ngram_range=(1, 2),token_pattern=r'\b\w+\b')
    X_train = vec.fit_transform(bodyword).toarray()
    transformer = TfidfTransformer(smooth_idf=False)
    print(transformer)
    tfidf = transformer.fit_transform(X_train).toarray()
    print(tfidf.shape)
    return X_train

def testEmailBody(newEmailBody):
    classifier = MultinomialNB()
    new_vec = vec.transform(newEmailBody)
    #print(new_vec)
    for i in range(len(emailClassification['SNIPPET'])):
        bodyVec = bodyVector[i]
        if bodyVec == newEmailBody:
            continue
        post_vec = X_train.getrow(i)
        d = distMatrix(post_vec,new_vec)
        print("Post %i with distance = %.2f: %s"%(i,d,bodyVec))


def similarityMatrixSubject(subjectList):
    subvec = TfidfVectorizer(min_df=1,stop_words = 'english',decode_error='ignore',analyzer='word',ngram_range=(1, 2),token_pattern=r'\b\w+\b')
    X_train = subvec.fit_transform(subjectList).toarray()
    transformer = TfidfTransformer(smooth_idf=False)
    tfidf = transformer.fit_transform(X_train).toarray()

    return X_train

def testEmailSubject(newEmailSubject):    
    
    new_vec = Subvec.transform(newEmailSubject)
    #print(new_vec)
    for i in range(len(emailClassification['SUBJECT'])):
        subVec = SubjectVector[i]
        if subVec == newEmailSubject:
            continue
        post_vec = X_train.getrow(i)
        d = distMatrix(post_vec,new_vec)
        print("Post %i with distance = %.2f: %s"%(i,d,subVec))

    
def main():
    PATH = '/Users/XXXXXXXXX/Documents/Google Gmail API /EmailClass.csv'
    global newDateTime
    global newSpam
    global newSnippet
    global newMailID
    global newSubject
    global getDateTime

    getDateTime = []
    newDateTime = []
    newSpam = []
    newSnippet = []
    newMailID = []
    newSubject = []

    if os.path.isfile(PATH):
        #print('True')
        with open('/Users/XXXXXXXXX/Documents/Google Gmail API /EmailClass.csv','a') as f:
            w = csv.writer(f)
            getDateTimeCSV = pd.read_csv(PATH,header='infer',sep=',',encoding='ISO-8859-1')
            getDateTime = getDateTimeCSV['Date']
            global latestDateTime
            latestDateTime = max(getDateTime)
            times = fetchEmails()
            #updatedRecords = DateTimeFormat(times[0])
            x = 0
            while True:
                print(times[0][x])
                print(latestDateTime)
                if times[0][x] > int(latestDateTime):
                    newDateTime.append(times[0][x])
                    newSpam.append(times[1][x])
                    newSnippet.append(times[2][x])
                    newMailID.append(times[3][x])
                    newSubject.append(times[4][x])
                    x = x + 1
                    if times[0][x] <= latestDateTime:
                        break
                else:
                    break

            w.writerows(zip(newDateTime,newSpam,newSnippet,newMailID,newSubject))
            f.close()   #times = DateTimeFormat(fetchEmails())
                    

    else:
        print('File Not Found')

    ########################################### MACHINE LEARNING ALGORITHM STARTS ##########################################################
    
    emailClassification = pd.read_csv('/Users/XXXXXXXXX/Documents/Google Gmail API /EmailClass.csv',sep=',',header='infer',encoding='ISO-8859-1')
    emailClassification['SNIPPET'] = emailClassification['SNIPPET'].fillna("UNKNOWN")
    emailClassification['SUBJECT'] = emailClassification['SUBJECT'].fillna("UNKNOWN")
    classifiers = {'Adaptive Boosting Classifier':AdaBoostClassifier(),'Linear Discriminant Analysis':LinearDiscriminantAnalysis(),'Random Forest Classifier': RandomForestClassifier(),'Decision Tree Classifier':DecisionTreeClassifier()}
    
    # CLASSIFIYING EMAIL WITH BOTH FEATURE TOGATHER (SUBJECT AND SNIPPET) WE GET BETTER ACCURACY !!!
    
    # Classifying the Email Based on Subject and SNIPPET togather 
    
    X_ = emailClassification[['SUBJECT', 'SNIPPET']].apply(lambda x: ''.join(x), axis=1)
    X_trained_= similarityMatrixSubject(X_)
    email_Classifier = pd.DataFrame(X_trained_[:,:],columns=X_trained_[0,:])
    y_trained = emailClassification['SPAM']
    rs = StratifiedShuffleSplit(n_splits=1, test_size=0.2,random_state=0)
    for Name,Classify in classifiers.items():
        for train_index,test_index in rs.split(email_Classifier,y_trained):    
            X__tr,X__test = email_Classifier.iloc[train_index], email_Classifier.iloc[test_index]
            y,y_test = y_trained.iloc[train_index], y_trained.iloc[test_index]
            clf1 = Classify
            clf1.fit(X__tr,y)
            y_pred1 = clf1.predict(X__test)
            print("EMAIL vs SPAM - Accuracy of Classifier "+Name,accuracy_score(y_pred1,y_test))
            print(y_test[:30].as_matrix())
            print(y_pred1[:30])
    

    # Classifying the Email Based on Subject and SNIPPET Seperately 
    
    X_trained_SNIPPET = emailClassification['SNIPPET']
    X_trained_SUBJECT = emailClassification['SUBJECT']
    X_trained_NP_SUB = similarityMatrixSubject(X_trained_SUBJECT)
    X_trained_NP_SNI = similarityMatrixSubject(X_trained_SNIPPET)
    X_trained_SNI = pd.DataFrame(X_trained_NP_SNI[:,:],columns=X_trained_NP_SNI[0,:])
    X_trained_SUB = pd.DataFrame(X_trained_NP_SUB[:,:],columns=X_trained_NP_SUB[0,:])
    
    for Name,Classify in classifiers.items():
        for train_index,test_index in rs.split(X_trained_SNI,y_trained):    
            X_SNI_tr,X_SNI_test = X_trained_SNI.iloc[train_index], X_trained_SNI.iloc[test_index]
            y,y_test = y_trained.iloc[train_index], y_trained.iloc[test_index]
            clf1 = Classify
            clf1.fit(X_SNI_tr,y)
            y_pred1 = clf1.predict(X_SNI_test)
            print("SNIPPET vs SPAM - Accuracy of Classifier "+Name,accuracy_score(y_pred1,y_test))
            print(y_test[:10].as_matrix())
            print(y_pred1[:10])
            
        for train_index,test_index in rs.split(X_trained_SUB,y_trained):
            X_SUB_tr,X_SUB_test = X_trained_SUB.iloc[train_index], X_trained_SUB.iloc[test_index]
            y,y_test = y_trained.iloc[train_index], y_trained.iloc[test_index]
            clf2 = Classify
            clf2.fit(X_SUB_tr,y)
            y_pred2 = clf2.predict(X_SUB_test)
            print("SUBJECT vs SPAM - Accuracy of Classifier "+Name,accuracy_score(y_pred2,y_test))
            print(y_test[:10].as_matrix())
            print(y_pred2[:10])
    

if __name__ == '__main__':
    main()