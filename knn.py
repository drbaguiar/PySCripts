# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:48:57 2015

@author: bryan_000
"""

from IPython.display import HTML
HTML('<iframe src=http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data width=300 height=200></iframe>')

# import load_iris function from datasets module
from sklearn.datasets import load_iris

# save "bunch" object containing iris dataset and its attributes
iris = load_iris()

# store feature matrix in "X"
X = iris.data
print X
# store response vector in "y"
y = iris.target
print y

# Import
from sklearn.neighbors import KNeighborsClassifier

# Set N
knn = KNeighborsClassifier(n_neighbors=5)

# Fit the model
knn.fit(X, y)

# New data for prediction
X_new = [[3, 5, 4, 2], [5, 4, 3, 2]]

# Print a prediction
print knn.predict(X_new)

