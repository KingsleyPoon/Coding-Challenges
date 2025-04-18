
"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

CODING CHALLENGE

A left rotation operation on an array shifts each of the array's elements  unit to the left.
For example, if  left rotations are performed on array , then the array would become . 
Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

Given an array  of  integers and a number, , perform  left rotations on the array. 
Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below.

rotLeft has the following parameter(s):

    int a[n]: the array to rotate
    int d: the number of rotations

Returns
    int a'[n]: the rotated array

Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations.
The second line contains  space-separated integers, each an .

For Example:
    
    Input of 5 and 4 on array [1,2,3,4,5] gives [5,1,2,3,4]
"""
import numpy

rotationLeftNumber = 4
arrayLengthInteger = 5

#Create numbers array (since it is not provided)
array = numpy.array([],dtype = int)

for i in range(1,arrayLengthInteger+1):
    array = numpy.append(array,i)

#Join the two separate parts of array together
newArray = numpy.append(array[rotationLeftNumber:], array[0:rotationLeftNumber])

#Print string out
ArrayString = ' '.join(map(str,newArray))
print(ArrayString)
        