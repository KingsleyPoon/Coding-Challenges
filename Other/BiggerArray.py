'''
CODING CHALLENGE
Tom and Jerry have same length of arrat all containing integers. There is a flag that is either odd or even.
Find the difference in sum of the arrays based on the value of the flag. If the flag is even, consider only the
even elements. If the flag is odd, consider only the odd elements. If Tom has a bigger sum array, output Tom's name.
If it is Jerry, output Jerry's name. If it is a tie, output Tie.

'''




Tom = [2,2,3]
Jerry = [3,1,4]
flag = "Even"
sumTom = 0
sumJerry = 0

for i in range(len(Tom)):

    if flag == "Odd":
        if int(Tom[i]) % 2 != 0:
            sumTom += int(Tom[i])
        if int(Jerry[i]) % 2 != 0:
            sumJerry += int(Jerry[i])
   
    if flag == "Even":
        if int(Tom[i]) % 2 == 0:
            sumTom += Tom[i]
        if int(Jerry[i]) % 2 == 0:
            sumJerry += int(Jerry[i])
    
    
difference = sumTom - sumJerry

if difference > 0:
    print("Tom")
elif difference < 0:
    print("Jerry")
else:
    print("Tie")     



    
    
    

