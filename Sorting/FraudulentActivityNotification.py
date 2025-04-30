# -*- coding: utf-8 -*-
"""
CODING CHALLENGE

https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
If the amount spent by a client on a particular day is greater than or equal to 2x  the client's median spending 
for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send 
the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days d and a client's total daily expenditures for a period of n days, 
determine the number of times the client will receive a notification over all n days.

Example
expenditure = [10,20,30,40,50]
d = 3

On first three days, they just collect spending data
At day 4, median is 20. Next day spending is 40. A notification is sent.
At day 5, median is 30, next day spending is 50. No notification is sent.

Therefore there will be one notification sent.

"""

def searchBinary(value,analysingArray):
    
    #Perform a binary search for position to add value
    left,right = 0, len(analysingArray)
    midPoint = int((left + right)/2)
    
    if value < analysingArray[0]:
        return 0
    
    while left < right:
        midPoint = int((left + right)/2)
        valueMidPoint = analysingArray[midPoint]
        
        if value < valueMidPoint:
            right = midPoint
        elif value == valueMidPoint:
            left = midPoint
            break
        else:
            left = midPoint + 1

    return left

def activityNotifications(expenditure, d):
    
    daysLength = len(expenditure)
    notifications = 0
    if d >= daysLength:
        return notifications
        
    analysingArray = sorted(expenditure[0:d])
    

    
    for index in range(d,daysLength):
        
        #Find Current value
        value = expenditure[index]
        
        #Find midValue
        if d%2 == 1:
            midValue = analysingArray[int(d/2)]
        else:
            midValue = (analysingArray[int(d/2-1)] + analysingArray[int(d/2)])/2
        
        if value >= midValue*2:
            notifications += 1



        #Find the value that will 
        oldValue = expenditure[index-d]

        removeIndex = searchBinary(oldValue,analysingArray)
        analysingArray.pop(removeIndex)
        
        
        insertIndex = searchBinary(value,analysingArray)

    return notifications


expenditure = [10,20,30,40,50]
d = 3

result = activityNotifications(expenditure,d)
print(result)