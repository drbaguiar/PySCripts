# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:49:21 2015

@author: bryan_000
"""

from pyngram import calc_ngram
txt = 'aaaabbbcccdb'
results = calc_ngram(txt, 2)   

print results

import nltk
a = nltk.bigrams(txt)

print nltk