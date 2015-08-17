# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:00:00 2015

@author: bryan_000
"""

# import the class
from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
logreg.fit(X, y)

X_new = [[3, 5, 4, 2], [5, 4, 3, 2]]

# predict the response for new observations
print logreg.predict(X_new)