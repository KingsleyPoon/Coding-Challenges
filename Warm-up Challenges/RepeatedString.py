# -*- coding: utf-8 -*-
"""
CODING CHALLENGE

https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

There is a string,s , of lowercase English letters that is repeated infinitely many times.
Given an integer, n , find and print the number of letter a's in the first n letters of the infinite string.
 
Example
s = 'abcac'
n = 10

Then the string is abcacabcac --> there are 4 instances of the letter a.
 
"""

def repeatedString(s, n):
    
    
    
    repeatedInt = int(n/len(s))
    modInt = n%len(s)
    
    totalRepeats = 0
    subRepeats = 0
    
    for n,value in enumerate(s):
        
        if value == "a":
            totalRepeats += 1
            
            if n <= modInt-1:
                subRepeats += 1
    
    total = totalRepeats*repeatedInt + subRepeats
    return total

s = "aba"
n = 10

result = repeatedString(s,n)
print(result)