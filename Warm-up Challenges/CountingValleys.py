# -*- coding: utf-8 -*-
"""
CODING CHALLENGE



An avid hiker keeps meticulous records of their hikes. 
During the last hike that took exactly steps steps, 
or every step it was noted if it was an uphill, U , or a downhill, D  step. 
Hikes always start and end at sea level, and each step up or down represents a  unit change in altitude.
 We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.

steps = 8 paths = [DDUUUUDD]

The hiker first enters a valley 2 units deep. Then they climb out and up onto a mountain 2 units high. 
Finally, the hiker returns to sea level and ends the hike.

"""

def countingValleys(steps, path):
    
    altitude = 0
    valleyCount = 0
    for n,value in enumerate(path):
        
        if value == "D":
            if altitude == 0:
                valleyCount +=1
            
            altitude -= 1
        
        else:
            altitude +=1
            
    return valleyCount

steps = 8
path = "UDDDUDUU"

result = countingValleys(steps,path)
print(result)
