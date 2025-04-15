# -*- coding: utf-8 -*-
"""
CODING CHALLENGE

https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

Each time Sunny and Johnny take a trip to the Ice Cream Parlor, they pool their money to buy ice cream. 
On any given day, the parlor offers a line of flavors. Each flavor has a cost associated with it.

Given the value of  and the  of each flavor for  trips to the Ice Cream Parlor, help Sunny and Johnny choose
two distinct flavors such that they spend their entire pool of money during each visit. ID numbers are the 
1- based index number associated with a . For each trip to the parlor, print the ID numbers for the two types 
of ice cream that Sunny and Johnny purchase as two space-separated integers on a new line. 
You must print the smaller ID first and the larger ID second.

Example:
    cost = [2, 1, 3, 5, 6]
    money = 5
    
    Purhcase flavour 1 and 3 (2 + 3 = 5)

"""
def whatFlavours(cost,money):
    for indexX,valueX in enumerate(cost):
        for indexY,valueY in enumerate(cost):
            
            # Determine cost of specific combination, also check that you are adding two unique flavours
            if ((valueX + valueY) == money) and indexX != indexY:
                
                #Since you are always starting at beginning index, indexX will always have the smaller ID number
                print(str(indexX+1) + ' ' + str(indexY+1))
                return

cost = [2,1,3,5,6]
money = 4

whatFlavours(cost,money)