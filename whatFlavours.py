# -*- coding: utf-8 -*-
"""
CODING CHALLENGE

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. 
On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of each flavor to the Ice Cream Parlor, help Sunny and Johnny choose
two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 
1- based index number associated with a . For each trip to the parlor, print the ID numbers for the two types 
of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. 
You must print the smaller ID first and the larger ID second.

Example:
    cost = [2, 1, 3, 5, 6]
    money = 5
    
    Purhcase flavour 1 and 3 (2 + 3 = 5)

"""

import numpy as np

'''
def whatFlavours(cost,money):
    for indexX,valueX in enumerate(cost):
        for indexY,valueY in enumerate(cost):
            
            # Determine cost of specific combination, also check that you are adding two unique flavours
            if ((valueX + valueY) == money) and indexX != indexY:
                
                #Since you are always starting at beginning index, indexX will always have the smaller ID number
                print(str(indexX+1) + ' ' + str(indexY+1))
                return

'''
def whatFlavours(cost,money):
    
    prices = set(cost)
    
    for index,value in enumerate(cost):
        if (money - value) in prices:
            
            for indexOther,valueOther in enumerate(cost):
                if valueOther == (money-value) and index != indexOther:
                    print(str(index+1) + ' ' + str(indexOther+1))
                    return



'''
cost = []
for i in range(2**12):
    cost.append(int(1))
    
cost.append(int(2))
cost.append(int(3))
cost.append(int(5))
cost.append(int(6))
'''
cost = [4,3,2,5,7]

cost = np.array(cost)
money = 8

whatFlavours(cost,money)