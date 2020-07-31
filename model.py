import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn.metrics import roc_auc_score,auc
import pickle
data = pd.read_csv('diabetes.csv')

X_train, X_test, y_train, y_test = train_test_split(data.drop('Outcome', axis =1), data['Outcome'], test_size =0.3, random_state =0)
param = {'n_estimators':[100,200,300,400], 'max_features':[2,3,8], 'max_depth':[2,4,3,8]}

self = RandomForestClassifier()
grid = GridSearchCV(self, param_grid = param, scoring = 'roc_auc', cv=10, n_jobs = -1)
grid.fit(X_train, y_train)

pickle.dump(grid, open('model.pkl', 'wb'))
pred = grid.predict_proba(X_train)
ausd = roc_auc_score(y_train, pred[:,1])

pre = grid.predict_proba(X_test)
aus = roc_auc_score(y_test, pre[:,1])
print(f'train_auc is {ausd} and the test_auc is {aus}')
