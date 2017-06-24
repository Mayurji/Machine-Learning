>>> import pandas as pd
>>> import numpy as np
>>> from sklearn.preprocessing import Imputer
>>> from sklearn import preprocessing
>>> from sklearn.cross_validation import train_test_split
/Library/Python/2.7/site-packages/sklearn/cross_validation.py:44: DeprecationWarning: This module was deprecated in version 0.18 in favor of the model_selection module into which all the refactored classes and functions are moved. Also note that the interface of the new CV iterators are different from that of this module. This module will be removed in 0.20.
  "This module will be removed in 0.20.", DeprecationWarning)
>>> from sklearn.naive_bayes import GaussianNB
>>> from sklearn.metrics import accuracy_score
>>> adult_df = pd.read_csv('/Users/mayurjain/Documents/NaiveBayes Python/adult.data',header = None,delimiter =',',engine = 'python')
>>> adult_df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num',
...                     'marital_status', 'occupation', 'relationship',
...                     'race', 'sex', 'capital_gain', 'capital_loss',
...                     'hours_per_week', 'native_country', 'income']
>>> adult_df.isnull().sum()
age               0
workclass         0
fnlwgt            0
education         0
education_num     0
marital_status    0
occupation        0
relationship      0
race              0
sex               0
capital_gain      0
capital_loss      0
hours_per_week    0
native_country    0
income            0
dtype: int64
>>> for value in ['workclass', 'education',
...           'marital_status', 'occupation',
...           'relationship','race', 'sex',
...           'native_country', 'income']:
...     print value,":", sum(adult_df[value] == '?')
... 
workclass : 0
education : 0
marital_status : 0
occupation : 0
relationship : 0
race : 0
sex : 0
native_country : 0
income : 0
>>> adult_df_rev = adult_df
>>> adult_df_rev.describe(include= 'all')
                 age workclass        fnlwgt education  education_num  \
count   32561.000000     32561  3.256100e+04     32561   32561.000000   
unique           NaN         9           NaN        16            NaN   
top              NaN   Private           NaN   HS-grad            NaN   
freq             NaN     22696           NaN     10501            NaN   
mean       38.581647       NaN  1.897784e+05       NaN      10.080679   
std        13.640433       NaN  1.055500e+05       NaN       2.572720   
min        17.000000       NaN  1.228500e+04       NaN       1.000000   
25%        28.000000       NaN  1.178270e+05       NaN       9.000000   
50%        37.000000       NaN  1.783560e+05       NaN      10.000000   
75%        48.000000       NaN  2.370510e+05       NaN      12.000000   
max        90.000000       NaN  1.484705e+06       NaN      16.000000   

             marital_status       occupation relationship    race    sex  \
count                 32561            32561        32561   32561  32561   
unique                    7               15            6       5      2   
top      Married-civ-spouse   Prof-specialty      Husband   White   Male   
freq                  14976             4140        13193   27816  21790   
mean                    NaN              NaN          NaN     NaN    NaN   
std                     NaN              NaN          NaN     NaN    NaN   
min                     NaN              NaN          NaN     NaN    NaN   
25%                     NaN              NaN          NaN     NaN    NaN   
50%                     NaN              NaN          NaN     NaN    NaN   
75%                     NaN              NaN          NaN     NaN    NaN   
max                     NaN              NaN          NaN     NaN    NaN   

        capital_gain  capital_loss  hours_per_week  native_country  income  
count   32561.000000  32561.000000    32561.000000           32561   32561  
unique           NaN           NaN             NaN              42       2  
top              NaN           NaN             NaN   United-States   <=50K  
freq             NaN           NaN             NaN           29170   24720  
mean     1077.648844     87.303830       40.437456             NaN     NaN  
std      7385.292085    402.960219       12.347429             NaN     NaN  
min         0.000000      0.000000        1.000000             NaN     NaN  
25%         0.000000      0.000000       40.000000             NaN     NaN  
50%         0.000000      0.000000       40.000000             NaN     NaN  
75%         0.000000      0.000000       45.000000             NaN     NaN  
max     99999.000000   4356.000000       99.000000             NaN     NaN  
>>> le = preprocessing.LabelEncoder()
>>> workclass_cat = le.fit_transform(adult_df.workclass)
>>> education_cat = le.fit_transform(adult_df.education)
>>> marital_cat   = le.fit_transform(adult_df.marital_status)
>>> occupation_cat = le.fit_transform(adult_df.occupation)
>>> relationship_cat = le.fit_transform(adult_df.relationship)
>>> race_cat = le.fit_transform(adult_df.race)
>>> sex_cat = le.fit_transform(adult_df.sex)
>>> native_country_cat = le.fit_transform(adult_df.native_country)
>>> adult_df_rev['workclass_cat'] = workclass_cat
adult_df_rev['education_cat'] = education_cat
adult_df_rev['marital_cat'] = marital_cat
adult_df_rev['occupation_cat'] = occupation_cat
adult_df_rev['relationship_cat'] = relationship_cat
adult_df_rev['race_cat'] = race_cat
adult_df_rev['sex_cat'] = sex_cat
adult_df_rev['native_country_cat'] = native_country_cat
dummy_fields = ['workclass', 'education', 'marital_status', 
...                   'occupation', 'relationship', 'race',
...                   'sex', 'native_country']
>>> adult_df_rev = adult_df_rev.drop(dummy_fields, axis = 1)
>>> adult_df_rev.head()
   age  fnlwgt  education_num  capital_gain  capital_loss  hours_per_week  \
0   39   77516             13          2174             0              40   
1   50   83311             13             0             0              13   
2   38  215646              9             0             0              40   
3   53  234721              7             0             0              40   
4   28  338409             13             0             0              40   

   income  workclass_cat  education_cat  marital_cat  occupation_cat  \
0   <=50K              7              9            4               1   
1   <=50K              6              9            2               4   
2   <=50K              4             11            0               6   
3   <=50K              4              1            2               6   
4   <=50K              4              9            2              10   

   relationship_cat  race_cat  sex_cat  native_country_cat  
0                 1         4        1                  39  
1                 0         4        1                  39  
2                 1         4        1                  39  
3                 0         2        1                  39  
4                 5         2        0                   5  
>>> adult_df.head()
   age          workclass  fnlwgt   education  education_num  \
0   39          State-gov   77516   Bachelors             13   
1   50   Self-emp-not-inc   83311   Bachelors             13   
2   38            Private  215646     HS-grad              9   
3   53            Private  234721        11th              7   
4   28            Private  338409   Bachelors             13   

        marital_status          occupation    relationship    race      sex  \
0        Never-married        Adm-clerical   Not-in-family   White     Male   
1   Married-civ-spouse     Exec-managerial         Husband   White     Male   
2             Divorced   Handlers-cleaners   Not-in-family   White     Male   
3   Married-civ-spouse   Handlers-cleaners         Husband   Black     Male   
4   Married-civ-spouse      Prof-specialty            Wife   Black   Female   

          ...          native_country  income  workclass_cat education_cat  \
0         ...           United-States   <=50K              7             9   
1         ...           United-States   <=50K              6             9   
2         ...           United-States   <=50K              4            11   
3         ...           United-States   <=50K              4             1   
4         ...                    Cuba   <=50K              4             9   

  marital_cat  occupation_cat  relationship_cat  race_cat  sex_cat  \
0           4               1                 1         4        1   
1           2               4                 0         4        1   
2           0               6                 1         4        1   
3           2               6                 0         2        1   
4           2              10                 5         2        0   

   native_country_cat  
0                  39  
1                  39  
2                  39  
3                  39  
4                   5  

[5 rows x 23 columns]
>>> adult_df_rev = adult_df_rev.reindex_axis(['age', 'workclass_cat', 'fnlwgt', 'education_cat',
...                                     'education_num', 'marital_cat', 'occupation_cat',
...                                     'relationship_cat', 'race_cat', 'sex_cat', 'capital_gain',
...                                     'capital_loss', 'hours_per_week', 'native_country_cat', 
...                                     'income'], axis= 1)
>>> adult_df_rev.head(1)
   age  workclass_cat  fnlwgt  education_cat  education_num  marital_cat  \
0   39              7   77516              9             13            4   

   occupation_cat  relationship_cat  race_cat  sex_cat  capital_gain  \
0               1                 1         4        1          2174   

   capital_loss  hours_per_week  native_country_cat  income  
0             0              40                  39   <=50K  
>>> num_features = ['age', 'workclass_cat', 'fnlwgt', 'education_cat', 'education_num',
...                 'marital_cat', 'occupation_cat', 'relationship_cat', 'race_cat',
...                 'sex_cat', 'capital_gain', 'capital_loss', 'hours_per_week',
...                 'native_country_cat']
>>> scaled_features = {}
>>> for each in num_features:
...     mean, std = adult_df_rev[each].mean(), adult_df_rev[each].std()
...     scaled_features[each] = [mean, std]
...     adult_df_rev.loc[:, each] = (adult_df_rev[each] - mean)/std
... 
>>> adult_df_rev.head()
        age  workclass_cat    fnlwgt  education_cat  education_num  \
0  0.030670       2.150546 -1.063594      -0.335432       1.134721   
1  0.837096       1.463713 -1.008692      -0.335432       1.134721   
2 -0.042641       0.090049  0.245075       0.181329      -0.420053   
3  1.057031       0.090049  0.425795      -2.402474      -1.197440   
4 -0.775756       0.090049  1.408154      -0.335432       1.134721   

   marital_cat  occupation_cat  relationship_cat  race_cat   sex_cat  \
0     0.921620       -1.317789         -0.277801  0.393661  0.703061   
1    -0.406206       -0.608377         -0.900167  0.393661  0.703061   
2    -1.734032       -0.135436         -0.277801  0.393661  0.703061   
3    -0.406206       -0.135436         -0.900167 -1.962591  0.703061   
4    -0.406206        0.810446          2.211664 -1.962591 -1.422309   

   capital_gain  capital_loss  hours_per_week  native_country_cat  income  
0      0.148451     -0.216656       -0.035429            0.291564   <=50K  
1     -0.145918     -0.216656       -2.222119            0.291564   <=50K  
2     -0.145918     -0.216656       -0.035429            0.291564   <=50K  
3     -0.145918     -0.216656       -0.035429            0.291564   <=50K  
4     -0.145918     -0.216656       -0.035429           -4.054160   <=50K  
>>> features = adult_df_rev.values[:,:14]
>>> target = adult_df_rev.values[:,14]
>>> features_train, features_test, target_train, target_test = train_test_split(features,target, test_size = 0.33, random_state = 10)
>>> clf = GaussianNB()
>>> clf.fit(features_train, target_train)
GaussianNB(priors=None)
>>> target_pred = clf.predict(features_test)
>>> accuracy_score(target_test, target_pred, normalize = True)
0.79890191699236923
>>> 
