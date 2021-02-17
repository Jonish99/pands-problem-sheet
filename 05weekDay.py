#program to get the week date from today's date 
#or any date and determine if it is weekday.

#Author: Jon Ishaque


#import date and time library
from datetime import date
import calendar
#get date extract day

#assign todays date
#could use all in one line but expansion may require user to input a specific date
#day=calendar.day_name[date.today.weekday()] 
dateToTest = date.today()
#assign day to testDate
#
day=calendar.day_name[dateToTest.weekday()] 

#Create Tuple for weekend days 
weekDays=("Monday","Tuesday","Wednesday","Thursday","Friday")

#Test if day is weekDays tuple
if day in weekDays:
    #if a weekday print msg 1
    print("Unfortunately today,({}) is a weekday".format(dateToTest))
else:
    #if not a weekend, must be a week day, print msg 2
    print("You're in luck, kick back and enjoy the weekend!")