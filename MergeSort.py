# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 12:38:00 2015

@author: bryan_000
"""

def mergeSort(alist):
    if len(alist)==0:
        print "Nothing to do "
    else:
        print("Splitting ",alist)
        if len(alist)>1:
            mid = len(alist)//2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
    
            mergeSort(lefthalf)   #  Recursion 1
            mergeSort(righthalf)  #  Recursion 2
    
            i=0
            j=0
            k=0
            while i<len(lefthalf) and j<len(righthalf):
                if lefthalf[i]<righthalf[j]:
                    alist[k]=lefthalf[i]
                    i=i+1
                else:
                    alist[k]=righthalf[j]
                    j=j+1
                k=k+1
    
            while i<len(lefthalf):
                alist[k]=lefthalf[i]
                i=i+1
                k=k+1
    
            while j<len(righthalf):
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
        print("Merging ",alist)
    
alist = [110,33,9,40,6,8]
print sorted(alist)
mergeSort(alist)
print(alist)
