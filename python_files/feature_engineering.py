"""Ce fichier a pour objectif de nettoyer les différents features
"""
# import libs et donnees
 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import LabelEncoder

PATH = "../data/"

X_test = pd.read_csv(PATH + "X_test_v1.csv")
X_train = pd.read_csv(PATH + "X_train_v1.csv")
y_train = pd.read_csv(PATH + "Y_train_v1.csv").drop(columns=['ID'], axis=1)

X_train['Nb_of_items'] = pd.to_numeric(X_train['Nb_of_items'], downcast='integer')
X_train['Nbr_of_prod_purchas'] = pd.to_numeric(X_train['Nbr_of_prod_purchas'], downcast='integer')
X_train = X_train.drop(columns=['ID', 'goods_code'], axis=1)

X_test['Nb_of_items'] = pd.to_numeric(X_test['Nb_of_items'], downcast='integer')
X_test['Nbr_of_prod_purchas'] = pd.to_numeric(X_test['Nbr_of_prod_purchas'], downcast='integer')
X_test = X_test.drop(columns=['ID', 'goods_code'], axis=1)

le_item = LabelEncoder()
le_item.fit(pd.concat([X_train['item'], X_test['item']]))
X_train['item'] = le_item.transform(X_train['item'])
X_test['item'] = le_item.transform(X_test['item'])

le_make = LabelEncoder()
le_make.fit(pd.concat([X_train['make'], X_test['make']]))
X_train['make'] = le_make.transform(X_train['make'])
X_test['make'] = le_make.transform(X_test['make'])

le_model = LabelEncoder()
le_model.fit(pd.concat([X_train['model'], X_test['model']]))
X_train['model'] = le_model.transform(X_train['model'])
X_test['model'] = le_model.transform(X_test['model'])

X_test.to_csv(PATH + "X_test_v1_clean.csv", index_label=False)
X_train.to_csv(PATH + "X_train_v1_clean.csv", index_label=False)
y_train.to_csv(PATH + "y_train_v1_clean.csv", index_label=False)