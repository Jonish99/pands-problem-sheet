"""Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.


$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1"""
#Author: Jon Ishaque

#out put message and ask user for +ve int and assign input to variable
userNum = int(input("Enter a  positve integer"))
nextVal = userNum
#loop until code assigns next val as 1.
while nextVal !=1:
    #test for even
    if (nextVal % 2) == 0:
        #divide by two
        nextVal = int(nextVal/2)
        #test for odd
    elif (nextVal % 2) == 1:
        #multiply by 3 and 1. 
        nextVal = (nextVal *3)+1
    else:
        #could write error here
        break

    #print out put
    print ("{} ".format(nextVal))