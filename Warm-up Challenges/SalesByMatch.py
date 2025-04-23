'''
CODING CHALLENGE

https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Example
n = 7
ar = [1,2,1,2,1,3,2]

The number of pairs is 2.

'''

def sockMerchant(n, ar):
    
    socksArray = []
    numberArray = []
    
    ar = sorted(ar)
    
    for n,value in enumerate (ar):
        if value in socksArray:
            
            numberArray[-1] +=1 
            
        else:
            socksArray.append(value)
            numberArray.append(1)
    
    pairsSocks = 0
    
    for n,value in enumerate(numberArray):
        pairsSocks += int(value/2)

    return pairsSocks

ar = [1,2,1,2,1,3,2]
n = 7
result = sockMerchant(n,ar)
print(result)