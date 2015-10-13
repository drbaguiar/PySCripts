# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:55:35 2015

@author: bryan_000
"""

import pandas
import numpy
# any additional libraries would be imported here

data = pandas.read_csv('D:\Data\EdX\gapminder.csv')

print (len(data)) #number of observations (rows)
print (len(data.columns)) # number of variables (columns)