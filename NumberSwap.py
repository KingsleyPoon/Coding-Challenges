
'''
CODING CHALLENGE
Given an integer, if 2 adjacent digits are both odd or even, we can swap these digits around. 
Obtain the largest number given any integer.

For examples:
Given the number is 5976833, the largest digit possible is 9758633

'''

# Important to realise that the numbers are sorted in groups of even or groups of odd numbers. 
# Therefore you must determine the index positions of these groups



#A function to determine if two numbers are both even or both odd, return True if so.
def isSame(n,y):
    if int(n)%2 == int(y)% 2:
        return True
    else:
        return False

# number can be manipulated as a string to determine index position of odd or even sections
number = 5976833
numberString = str(number)
numberOfDigits = len(numberString)
indexPositions = ["0"]

#Loop through each number in the number string. When there is a change from even to odd (or vice versa), note its position.
# Ensure first position and last position are noted
for i in range(1,len(numberString)):
    value = numberString[i]
    previousValue = numberString[i-1]
    if isSame(value,previousValue) == False:
        indexPositions += str(i)

indexPositions += str(len(numberString))

#Make a variable for the final number
finalNumber = ""

# Loop through each section of odd or even numbers and sort largest to smallest
for i in range(1,len(indexPositions)):
    valuesInterested = numberString[int(indexPositions[i-1]):int(indexPositions[i])]
    sortedvalues = sorted(valuesInterested,reverse= True)
    print(sortedvalues)
    
    for value in sortedvalues:
        finalNumber += value
        
finalNumber = int(finalNumber)