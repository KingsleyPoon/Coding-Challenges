# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

A student is taking a cryptography class and has found anagrams to be very useful. 
Two strings are anagrams of each other if the first string's letters can be rearranged to form the second string. 
In other words, both strings must contain the same exact letters in the same exact frequency. 
For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

The student decides on an encryption scheme that involves two large strings. 
The encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. 
Determine this number.

Given two strings, a  and b, that may or may not be of the same length, 
determine the minimum number of character deletions required to make a and  b anagrams. 
Any characters can be deleted from either of the strings.

Example:
    a = 'cde'
    b = 'abc'
This take 2 character deletions

"""

a = 'fcrxzwscanmligyxyvym'
b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

# Sort the letters in alphabetical order
a = sorted(a)
b = sorted(b)

# A tracker of number of deletions applied    
numberOfDeletions = 0

#While there are still letters in the array, keep the loop running
while True:
    
    #If one of the words is empty, remaining letters must be deleted since they are not common.
    if len(a) == 0:
        numberOfDeletions += len(b)
        break 
    elif len(b) == 0:
        numberOfDeletions += len(a)
        break
    
    #If letter is present in one string and not another, add to deletion count
    if a[0] != b[0] and a[0] in b:
        b = b[1:]
        numberOfDeletions += 1
    elif a[0] != b[0] and a[0] not in b:
        a = a[1:]
        numberOfDeletions += 1
    
    #If letter is both strings, delete both and DO NOT ADD TO COUNT (since it is common between both strings)
    else:
        a = a[1:]
        b = b[1:]

print(numberOfDeletions)