"""Ce fichier a pour objectif de créer les différents jeu de données d'étude

Le script est a exécuter avec pour répertoire de travail challenge-STASC/python_files/.
"""
### PARTIE 1 : Version bourrin (on garde l'item le plus cher s'il y en a plusieurs)

# import libs et donnees
 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

PATH = "../data/"

X_test = pd.read_csv(PATH + "X_test_8skS2ey.csv")
X_train = pd.read_csv(PATH + "X_train_G3tdtEn.csv")
y_train = pd.read_csv(PATH + "Y_train_2_XPXJDyy.csv").drop(columns=["index"], axis=1)

# nettoyage

item = []
cash_price = []
make = []
model = []
goods_code = []
Nbr_of_prod_purchas = []

for i in X_train.index:
    item_index = 0
    if X_train.iat[i,-1] != 1:
        j = 1
        while j < 24 and X_train.iat[i, 25 + j] != np.nan:
            if X_train.iat[i, 25 + j] > X_train.iat[i, 25 + item_index]:
                item_index = j
            j = j + 1
    item.append(X_train.iat[i, 1 + item_index])
    cash_price.append(X_train.iat[i, 25 + item_index])
    make.append(X_train.iat[i, 49 + item_index])
    model.append(X_train.iat[i, 73 + item_index])
    goods_code.append(X_train.iat[i, 97 + item_index])
    Nbr_of_prod_purchas.append(X_train.iat[i, 121 + item_index])

X_train_new = X_train[['ID', 'Nb_of_items']]
X_train_new['item'] = item
X_train_new['cahs_price'] = cash_price
X_train_new['make'] = make
X_train_new['model'] = model
X_train_new['goods_code'] = goods_code
X_train_new['Nbr_of_prod_purchas'] = Nbr_of_prod_purchas

item = []
cash_price = []
make = []
model = []
goods_code = []
Nbr_of_prod_purchas = []

for i in X_test.index:
    item_index = 0
    if X_test.iat[i,-1] != 1:
        j = 1
        while j < 24 and X_test.iat[i, 25 + j] != np.nan:
            if X_test.iat[i, 25 + j] > X_test.iat[i, 25 + item_index]:
                item_index = j
            j = j + 1
    item.append(X_test.iat[i, 1 + item_index])
    cash_price.append(X_test.iat[i, 25 + item_index])
    make.append(X_test.iat[i, 49 + item_index])
    model.append(X_test.iat[i, 73 + item_index])
    goods_code.append(X_test.iat[i, 97 + item_index])
    Nbr_of_prod_purchas.append(X_test.iat[i, 121 + item_index])

X_test_new = X_test[['ID', 'Nb_of_items']]
X_test_new['item'] = item
X_test_new['cahs_price'] = cash_price
X_test_new['make'] = make
X_test_new['model'] = model
X_test_new['goods_code'] = goods_code
X_test_new['Nbr_of_prod_purchas'] = Nbr_of_prod_purchas

X_test_new.to_csv(PATH + "X_test_v1.csv", index_label=False)
X_train_new.to_csv(PATH + "X_train_v1.csv", index_label=False)
y_train.to_csv(PATH + "y_train_v1.csv", index_label=False)

