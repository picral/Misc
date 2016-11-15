# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 16:20:13 2016

@author: hg

happy number

takes a number and returns true if number is happy and false if number is unhappy

"""

def happy_number(n):
    ''' test conditions, if number is happy cycle ends in 1 by definition
        if the number is unhappy it enters a cycle containing 4'''
    testconditions = [1,4]    
    while n not in testconditions:
        total = 0
        n = list(str(n))
        for i in n:
            total += int(i)**2
        n = total
        if n == 4:
            return False
        elif n == 1:
            return True

#generates array with all happy numbers in range
array = []
for i in range(1,1000001):
    if happy_number(i) == True:
        array.append(i)

print(array)