# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

You are given a string containing characters A  and B only. 
Your task is to change it into a string such that there are no matching adjacent characters. 
To do this, you are allowed to delete zero or more characters in the string.
Your task is to find the minimum number of required deletions.
"""

s = "AAABBBAABB"

#Keep count for number of deletions
numberOfDeletions = 0

#Keep track what the previous letter is
currentLetter = s[0]

#loop through the whole string
for index,value in enumerate(s):
    
    #If the previous letter is not different to current letter, it needs to be removed. Add to count.
    if value == currentLetter and index !=0:
        numberOfDeletions += 1
    else:
        #Only update the current letter value if current letter is different to previous
        currentLetter = value

print(numberOfDeletions)