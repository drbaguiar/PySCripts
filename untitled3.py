# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:56:29 2015

@author: bryan_000
"""

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False
    
print search(['e','g','f'],'f')
print newsearch(['e','g','f'],'f')