# -*- coding: utf-8 -*-
"""
Coding Challenge 
https://www.hackerrank.com/challenges/balanced-brackets/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].

Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left
of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched.
For example, {[(])} is not balanced because the contents in between { and } are not balanced.
The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses 
encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given n strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
"""

def isBalanced(s):
    
    stringLength = len(s)
    uniqueCharacters = len(set(s))
    
    if stringLength%2 !=0 or uniqueCharacters%2 !=0:
        return "NO"
    
    currentQueue = []
    currentQueueLength = 0
    
    for n in range(0,stringLength):

        currentCharacter = s[n]
        
        if currentCharacter in ('{' , '[' , '('):
            currentQueue.append(currentCharacter)
            currentQueueLength += 1
        else:
            if currentQueueLength == 0:
                return "NO"
                     
            lastCharacter = currentQueue[-1]
            
            if currentCharacter == ']' and lastCharacter == '[':
                currentQueue.pop(-1)
                currentQueueLength -=1
            elif currentCharacter == '}'and lastCharacter == '{':
                currentQueue.pop(-1)
                currentQueueLength -=1
            elif currentCharacter == ')'and lastCharacter == '(':
                currentQueue.pop(-1)
                currentQueueLength -=1
            else:
                return "NO"
                

    if currentQueueLength == 0:
        return "YES"
    else: 
        return "NO"

s = "{[()]}"
result = isBalanced(s)
print(result)
