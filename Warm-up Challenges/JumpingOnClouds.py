# -*- coding: utf-8 -*-
"""
CODING CHALLENGE

https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup

There is a new mobile game that starts with consecutively numbered clouds. 
Some of the clouds are thunderheads and others are cumulus. 
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. 
The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud.
It is always possible to win the game.

For each game, you will get an array of clouds numbered  0 if they are safe or 1 if they must be avoided.

Example

c = [0,1,0,0,0,1,0]

Path can be 0 --> 2 --> 4 --> 6
therefore 3 jumps

"""

def jumpingOnClouds(c):
    
    jumps = 0
    
    index = 0
    
    while index < len(c)-1:
        if index+2 < len(c) and c[index + 2] == 0:
            index += 2
        else:
            index += 1

        jumps += 1

    
    return jumps

c = [0,1,0,0,0,1,0]
result = jumpingOnClouds(c)
print(result)