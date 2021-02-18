#Assignment wk 2
#Programme to take 2 inputs and calcualte BMI
#Author: Jon Ishaque

#output instruction and input values for vars, height and weight
print('The following programme will calculate the BMI from the data entred:')
weight=int(input('Please enter your weight in kilograms:'))
height=int(input('Please enter your height in centmeters:'))


#convert height cm to metres
height_M = height/100
#square height
height_Sq = height_M * height_M
#Calculate BMI

BMI = weight/height_Sq
#print output and format BMI to 2 decimal places
print('The BMI for a person {} CM tall weighing {} KG is,{:.2f}.'.format(height,weight,BMI))
