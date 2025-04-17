"""
CODING CHALLENGE

https://www.hackerrank.com/challenges/minimum-time-required/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

You are planning production for an order. 
You have a number of machines that each have a fixed number of days to produce an item. 
Given that all the machines operate simultaneously, determine the minimum number of days to produce the required order.

For example, you have to produce 10 items. You have three machines that take [2,3,2]  days to produce an item.

It takes  days to produce  items using these machines.

"""
import numpy as np


'''
Slower method of finding by calculating each possible day

numberOfItems = 10
machines = np.array([1,3,4])


def minTime(numberOfItems,machines):
    
    n = 0
    while True:
        n += 1
        result = map(lambda x: int(n/x),machines)
        totalItems = sum(result)
        
        if totalItems >= numberOfItems:
            print(n)
            return

minTime(numberOfItems,machines)

'''

# Faster method of searching includes a binary search where you guess how many days and improve the guesses

numberOfItems = 5
machines = np.array([2,3])

#maximum days needed is slowest machine producing all goods
high = max(machines)*numberOfItems
low = 1

while low < high:
    
    mid = (low + high)//2
    
    totalItems = sum(map(lambda x: mid//x,machines))
    
    if totalItems >= numberOfItems:
        high = mid
    else:
        low = mid+1
print(low)