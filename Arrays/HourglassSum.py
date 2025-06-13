# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays


Given a 6x6 2D array, arr , an hourglass is a subset of values with indices falling in the following pattern:
    1 2 3
      4 
    5 6 7
    
There are 16 hourglasses in a 6c6 array. Th hourglass sum is the sum of the values in an hourglass.
Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum
"""

arr = [[-9,-9,-9,1,1,1],
       [0,-9,0,4,3,2,1],
       [-9,-9,-9,1,2,3],
       [0,0,8,6,6,0],
       [0,0,0,-2,0,0],
       [0,0,1,2,4,0]]

sumArray = []
for y in range(0,4):
    for x in range(0,4):
        sum = arr[y][x] + arr[y][x+1] + arr[y][x+2] + arr[y+1][x+1] + arr[y+2][x] + arr[y+2][x+1] + arr[y+2][x+2]
        sumArray.append(sum)
print(str(max(sumArray)))