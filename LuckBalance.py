# -*- coding: utf-8 -*-
"""
CODING CHALLENGE

https://www.hackerrank.com/challenges/luck-balance/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

Lena is preparing for an important coding competition that is preceded by a number of sequential preliminary contests. 
Initially, her luck balance is 0. She believes in "saving luck", and wants to check her theory. 
Each contest is described by two integers, L[i] and T[i]:

L[i] is the amount of luck associated with a contest. If Lena wins the contest, her luck balance will decrease by L[i]; 
if she loses it, her luck balance will increase by L[i].

T[i] denotes the contest's importance rating. It's equal to 1 if the contest is important, and it's equal to 0  if it's unimportant.

If Lena loses no more than k important contests, what is the maximum amount of luck she can have after competing in all the preliminary contests? 
This value may be negative.
"""
import math
import os
import random
import re
import sys


def luckBalance(k, contests):
    
    luckSum = 0
    
    importantContest = []
    
    #Sum all the nonimportant contests and add important contests to new array.
    # You will lose all non-important contests and the top k amount of important contests.
    #You will win the lower value important contest (subtracting the luck of those contests)
    for index,value, in enumerate(contests):
        luck,importance = value
        if importance == 0:
            luckSum += luck
        else:
            importantContest.append(luck)
    
    importantContest = sorted(importantContest)
    wonContest = importantContest[max(0,len(importantContest)-k):]
    lostContest = importantContest[0:max(0,len(importantContest)-k)]
    
    luckSum += sum(wonContest) - sum(lostContest)
    return luckSum


contests = [[5, 1], [2, 1], [1, 1], [8, 1], [10, 0], [5, 0]]
k = 3

print(luckBalance(k,contests))