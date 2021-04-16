'''This program uses asks a user to imput a number and return an approximate square root of the number using the Newton Method. 
See the README.md to understand how this programmer came up with the solution below, the program has an i counter, commented out,
which can be printed to see how many interations it took.  '''

#Author: Jon Ishaque

#Functions
#define function, receive an argument, the number to find the root of
def newtonSrt(num):
    #1st guess, have the origiginal number. 
    #convert to float because if 20 is halved it will return an integer which will define the guess as an integer, but the value is reassigned later
    #maybe as a float and this will cause an error
    guessRoot = float(num/2 ) #convert to float because if 20 is halved it will return an integer
    #counter if needed to see how many interations it tool
    i=1
    #Continue loop until break condition is met
    while True: 
        #This the main part of Newton's Method (see README.md) and is repeated until conditon below is met
        NewGuess = 0.5 * (num/guessRoot +guessRoot)
        #once the difference between the new guess and the previous guess is less than .00001 
        #The function returns the guess (and the loop exits)
        #The number of decimal places of .1 determines the accuracy of the program
        if (guessRoot-NewGuess) < .00001:
            #print counter if user wants to know how many iterations of the loop are used
            #print ("Number of 'guesses': ",i)
            return NewGuess #and therefore exit thefunction
        
        #if the return condtion is not met, we assign the latest guess to guessRoot variable for the next interation of the loop
        guessRoot = NewGuess
        #increment counter
        i +=1
    


#Main program

num = float(input("Enter a positve number to test the programme:"))
#call the function, newtonSrt passing the input number as an argument
#Output original number and the square formatted to 4 decimal places
print("The square root of {} is approx, {:.4f}".format(num,newtonSrt(num)))