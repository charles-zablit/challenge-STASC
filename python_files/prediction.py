"""Ce fichier va concentrer les démarches de prédictions
"""

# import

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import average_precision_score
from sklearn.model_selection import train_test_split
from sklearn import svm

PATH = "../data/"

X = pd.read_csv(PATH + "X_train_v1_clean.csv")
y = pd.read_csv(PATH + "Y_train_v1_clean.csv")

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Partie 1: dealing with unbalanced class
# On va mettre en oeuvre plusieurs démarches : métrique adaptéé et sampling adapté

# fit the model and get the separating hyperplane using weighted classes
wclf = svm.SVC(kernel="linear", class_weight={1: 100})
wclf.fit(X_train, y_train)
print(wclf.score(X_test, y_test))