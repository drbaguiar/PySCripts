# -*- coding: utf-8 -*-
"""
Created on Thu Jul 02 22:39:17 2015

@author: bryan_000
"""

def Karatsuba(number1,number2,N):
     
     
 
    if N==1:
        return number1*number2
 
    if N%2==1:
        N+=1
 
    exp=N//2
    pw=pow(10,exp)
 
    num1,num2=number1//pw,number1%pw
    num3,num4=number2//pw,number2%pw
 
     
 
    U=Karatsuba(num1,num3,exp)
    V=Karatsuba(num2,num4,exp)
     
 
    N1=num1-num2
    N2=num3-num4
 
     
    W=Karatsuba(N1,N2,exp)
    Z=U+V-W
     
    result=pow(10,N)*U+pow(10,N/2)*Z+V
    return result
      
 
num=Karatsuba(123,5678,4)
print(num)