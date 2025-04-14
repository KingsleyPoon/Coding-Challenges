'''
CODING CHALLENGE
Write a program to find the highest common factor of two numbers (a,b) without using recursion.

'''

# In the most simplistic way, you can loop between all the numbers betwee 2 and the n (where n is the lowest number)
# Store the highest common factor that you find in this loop

HCF = 0

a  = 70
b = 15

if a < b:
    lowestNumber = a
    highestNumber = b
else:
    lowestNumber = b
    highestNumber = a

for n in range (2,lowestNumber+1):
    if lowestNumber % n == 0 and highestNumber % n == 0:
        HCF = n

print(HCF)