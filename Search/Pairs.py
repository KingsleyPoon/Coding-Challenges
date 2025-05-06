# -*- coding: utf-8 -*-
"""
CODING CHALLENGE
https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

Example
k = 1
arr = [1,2,3,4]

There are three values that differ by k = 1: 2-1 = 1, 3-2 = 1, 4-3 = 1.

Return 3


"""

def binarySearch(value,array):
    left,right = 0,len(array)

    
    while left < right:
        midPoint = int((left+right)/2)
        if value == array[midPoint]:
            return True
        elif value < array[midPoint]:
            right = midPoint
        else:
            left = midPoint + 1
        
        
    return False


def pairs(k, arr):
    
    arr = sorted(set(arr))

    seen = []
    count = 0
    
    for n,value in enumerate(arr):
        if binarySearch(value,seen) == True and n!=0:
            count += 1
        
        seen.append(value+k)
    
    return count

k = 1
arr = [1,2,3,4]

result = pairs(k,arr)
print(result)