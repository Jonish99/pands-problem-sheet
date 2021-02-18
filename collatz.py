"""A program that takes a positive integer as input.
The programme performs a calculation on the current value, (starting with input).
If the value is even it is divided by two and assigned to the current value variable
If it is odd it is multiplied by 3 and 1 is added and then the value is assigned to current value.
The program ends when the current value is 1"""
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
