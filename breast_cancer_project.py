# -*- coding: utf-8 -*-
"""breast cancer project

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kI_IC8ifokz3E36YjjrjwdtDJFbzo0bX
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.datasets import load_breast_cancer

cancer= load_breast_cancer()
cancer.keys()

print(cancer['data'])

print(cancer['DESCR'])

df_feat = pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
df_feat.head()

cancer['target']

df_target = pd.DataFrame(cancer['target'],columns=['cancer'])
df_target.head()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test= train_test_split( df_feat, np.ravel(df_target),test_size= 0.4 , random_state= 101)
x_train.info()

from sklearn.svm import SVC

model = SVC()

model.fit(x_train,y_train)

predection = model.predict(x_test)

from sklearn.metrics import classification_report

print ( classification_report(y_test, predection))

