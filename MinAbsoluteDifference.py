# -*- coding: utf-8 -*-
"""
Coding Challenge

https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

Complete the minimumAbsoluteDifference function in the editor below. 
It should return an integer that represents the minimum absolute difference between any pair of elements.
"""

import math
import os
import random
import re
import sys


#Smallest min value is equal to
def minimumAbsoluteDifference(arr):
    
    arr = sorted(arr)
    
    #Only perform subtraction of adjacent numbers
    minValue = 2e9
    
    for n, value in enumerate(arr):
        
        if n != 0:
            minValue = min(minValue,abs(value - arr[n-1]))
    
        if n != len(arr)-1:
            minValue = min(minValue,abs(value - arr[n+1]))
            
    return minValue

arr = [-59,-36,-13,1,-53,-92,-2,-96,-54,75]

print(minimumAbsoluteDifference(arr))