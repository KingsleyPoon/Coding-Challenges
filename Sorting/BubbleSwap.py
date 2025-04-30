'''
CODING CHALLENGE

https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. 
Once sorted, print the following three lines:

    1) Array is sorted in X swaps.
    2) First Element: Y
    3) Last Element: Z
    
'''

def countSwaps(a):
    
    sortedA = sorted(a)
    swaps = 0
    for targetIndex,valueTarget in enumerate(sortedA):
        
        for index,valueSearch in enumerate(a):
            if valueSearch == valueTarget:
                swaps += index
                del a[index]
                break
                
    print("Array is sorted in " + str(swaps) + " swaps.")
    print("First Element: " + str(min(sortedA)))
    print("Last Element: " + str(max(sortedA)))   
    
    return  

a = [4,2,3,1]

countSwaps(a)