#for week 3 assigment
#a programme to take a string and output every 2nd char in reverse order
#Author: Jon Ishaque
#See README.md for references

#Get user input for string
strSecAndRev=input("Enter a string of any length:")

#get lenth of string
lenStr=len(strSecAndRev)

#get every 2nd char only
str2ndChar = (strSecAndRev[::2])

#reverse the string
strRev =str2ndChar [::-1]

#ouput and format
print ("The string  with every 2nd character of the string only is,{}".format(strRev))
