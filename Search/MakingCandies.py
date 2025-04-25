'''
CODING CHALLENGE

https://www.hackerrank.com/challenges/making-candies/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search

Karl loves playing games on social networking sites. His current favorite is CandyMaker, where the goal is to make candies.

Karl just started a level in which he must accumulate n candies starting with m machines and w workers. 
In a single pass, he can make m x w candies. 
After each pass, he can decide whether to spend some of his candies to buy more machines or hire more workers. 
Buying a machine or hiring a worker costs p units, and there is no limit to the number of machines he can own or workers he can employ.

Karl wants to minimize the number of passes to obtain the required number of candies at the end of a day. 
Determine that number of passes.

For example, Karl starts with m = 1 machine and w = 2 workers. The cost to purchase or hire, p = 1 and he needs to accumulate 60 candies. 
He executes the following strategy:
    1. make m x w  = 2 candies. Purchase 2 machines.
    2. Make 3 x 2 = 6 candies. purchase 3 machines and 3 workers.
    3. make 6 x 5 = 30 candies. Retain all 30 candies
    4. make 6 x 5 = 30 candies. With yesterday's production, Karl has 60 candies.
    
    it took 4 passes.
'''


def minimumPasses(m, w, p, n):
    
    machines = m
    workers = w
    cost = p
    requiredCandies = n
    
    numPassArray = []
    
    producedCandy = 0
    remainingCandy = 0
    passes = 0
    while True:
        passes += 1
        producedCandy = machines * workers
        remainingCandy += producedCandy
        
        if remainingCandy >= requiredCandies:
            numPassArray.append(passes)
            break
        
        #Work out remaining days if at current production rate
        if (requiredCandies-remainingCandy)%producedCandy == 0:
            numPassArray.append(passes + int((requiredCandies-remainingCandy)/producedCandy))

        else:
            numPassArray.append(passes +1+ int((requiredCandies-remainingCandy)/producedCandy))
            
        if numPassArray[-1] <= passes:
            break    
        
        
        #Speeds up day process so it doesnt have to iterate day by day
        daysUntilNextPurchase = int((cost-remainingCandy)/producedCandy)
        
        if daysUntilNextPurchase > 1:
            remainingCandy += (daysUntilNextPurchase-1)*producedCandy
            passes += daysUntilNextPurchase-1
        
        numberToPurchase = int(remainingCandy/cost)

        remainingCandy = remainingCandy % cost

        #It is always optimal to have same number of workers and machines
        while machines != workers and numberToPurchase > 0:
            if machines < workers:
                machines += 1
            else:
                workers += 1
            numberToPurchase -= 1
        
        
        #Faster way to assign workers and machines than individually
        if numberToPurchase > 0:
            
            totalPoolWorkersMachines = machines + workers + numberToPurchase
        
            machines = int(totalPoolWorkersMachines/2)
            workers = int(totalPoolWorkersMachines/2) + totalPoolWorkersMachines%2
    
    return min(numPassArray)

result = minimumPasses(1,1,1,1000000000000)

    
