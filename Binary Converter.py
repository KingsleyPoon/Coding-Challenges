'''
CODING CHALLENGE
Write a program to change a integer number to a binary number

ie. 4 = 100, 15 = 01111

'''

value = 15
binary = 0
numberofTimesLooped = 0

while value > 0:
    mod = (value % 2)
    value = int(value / 2)
    binary = binary + 10**numberofTimesLooped*mod
    numberofTimesLooped +=1
    