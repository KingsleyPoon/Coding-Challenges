# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times. 
Given a string , determine if it is valid. If so, return YES, otherwise return NO.
"""


def SherlockString(s):
    #Sort array of letters
    s = sorted(s)
    
    #Keep an array for the counts of each letter that appears
    countArray = []
    numberSeen = 0
    currentLetter = s[0]
    
    #Count how many of each letter there is and append number to countArray
    for index,value in enumerate(s):
        
        #if the same letter, add to count
        if value == currentLetter:
            numberSeen +=1
        
        #If letter has changed, append previous number, change current letter, reset count
        else:
            countArray.append(numberSeen)
            currentLetter = value
            numberSeen = 1
    
    #Append last number to array corresponding to last letter counted
    countArray.append(numberSeen)
    
    #sort the counts of numbers 
    countArray = sorted(countArray)
    uniqueOccurences = len(set(countArray))
    
    
    if uniqueOccurences > 2:
        return "NO"
    elif uniqueOccurences == 1:
        return "YES"
    elif countArray[-2]+1 == countArray[-1]:
        return "YES"
    elif len(set(countArray[1:]))==1:
        return "YES"
    else:
        return "NO"

s = "abcdefghhgfedecba"
result = SherlockString(s)
print(result)      
