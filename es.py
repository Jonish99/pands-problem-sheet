'''A program, that will read a text file and count the number of es. The text file is defined by the user on the command line, 
it is checked if exists and checked for file extension. The approriate system path of the program directory is determined. 
The file is opened, the number of es is the file are counted and it is the value is returned to the user. '''

#Author: Jon Ishaque

#imports
import sys #to get help get the system path
import os.path # to check if file exists and get system path.

#function to check a string has the .txt file extension

def checkForTxt(userf):
    #get the lenght of the string
    l=len(userf)
    s = userf
    #find the  postion of .txt from the back
    s= userf.rfind('.txt')
    #if postion is not - 1 and lentht of string  minus postion = 4 then .txt is the file extension
    if s !=-1 and (l-s)== 4:
        return userf
    else:
        return userf+".txt"

#define function to read the the file
def readFile(filename):
    #add try - it will work because we have the isfile method already
    try:
        #use with to carry out file operations on file
        #open file and assign local name, f
        with open(filename,'r') as f:
            #read file contents, convert the string to an int and assign to variable
            eString = f.read()
            #return the string from the file to the function call
            return eString
    except IOError:
        # this file will be created when we write back.
        # # no file assumes first time running 
        # # ie 0 previous runs

        #the funciton call is expecting something.
        return "This file cannot be opened by programme"

#function takes the string as an argument and returns the number of es
#(Python | Count occurrences of a character in string - GeeksforGeeks, 2021)
def countEs(eString):
    #(Python | Count occur
    count =0
    #for loop, iterating through every char in the string
    
    for i in eString: 
        #for each char in the string, check if it's e
        if i == 'e': 
            #if it's an e, increment the counter
            count = count + 1
    #after loop has run, return the count of es to the function call.
    return count

#main program

#initiate variable to control while loop.
userf=""


#loop until user enters 'q'
while userf !="q":
    #get user to input name of file to count the es.    
    userf = input('Please enter the name of the txt file of you which you wish to count the es:') 
    #quit if user has enter q
    if userf=="q" : exit() 

    #pass the input to check for .txt file extension. The function will return a file name with the .txt extenstion
    filen =  checkForTxt(userf)

    #this system requires an absolute path from to find file
    #my OS does not (always) read relative paths in python. I could use hardcoded paths, not useful when porting the program to other systems
    #assign file name & prefix double slash to join file name string
    mypath =str(os.path.dirname(os.path.abspath(sys.argv[0])))

    #join the path with the filen. "\\" is the directory seperator being used in this path format
    filename = mypath+"\\"+filen

    # check file exists
    if not os.path.isfile(filename):
        print("File does not exist, or enter q to quit")
        #initialise file here

    else: #file does exist
        #assign the string from function call to read file with filename
        stringf = readFile(filename)

        #call the counteEs function with the string with es to count, as the argument, format the returned number and the file name into the
        #output string. I could also call the readFile function here, and pass the return directly as an argument to countEs, I have not done so as it is more 
        #difficult to read.
        print("The file, {}, contains {} es".format(filen,countEs(stringf)))
        





    



