"""A program that takes a positive integer as input.
The programme performs a calculation on the current value, (starting with input).
If the initial value is 1 the program output nothing.
The user input is converted to an integer so as not be treated as a string a cause an error
If the value is even it is divided by two and assigned to the current value variable
If it is odd it is multiplied by 3 and 1 is added and then the value is assigned to current value.
The program ends when the current value is 1"""
#Author: Jon Ishaque

#output message and ask user for +ve int and assign input to variable.
#Convert the input string to an integer to be treated as such by python
userNum = int(input("Enter a  positve integer"))
#Reassign UserNum to nextVal to be consistent with following loop operation.
nextVal = userNum
#Start a while loop with the condion nextVal is not 1.
#The logig of the loop will ensure the nextVal will eventually becomem 1
while nextVal !=1:
    #Test for an even number by tesing in the remainder of division by 2, == 0
    if (nextVal % 2) == 0:
        #If is even it will be divisible by zero and only this branch of the if statement will
        #be used for the remaining interations of the loop. 
        nextVal = int(nextVal/2)
    #Test even number by tesing in the remainder of division by 2, == 1
    elif (nextVal % 2) == 1:
        #multiply by 3 and add 1. multiplication of an odd number by 3 + 1 

        nextVal = (nextVal *3)+1
    else:
        #could write error here
        #exit the while loop
        break

    #print next value using the format method of the string object.
    print ("{} ".format(nextVal))

    
