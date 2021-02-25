### pands-problem-sheet

GMIT repository for Jon Ishaque Programming and Scripting Problem sets. 2021



## [1. bmi.py] (bmi.py)
    A program that allows a user to enter their weight in KG and height in Metres which calculates and outputs the BMI for the inputs.

### References:
    Kite.com. 2021. Code Faster with Line-of-Code Completions, Cloudless Processing. [online] Available at: <https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python> [Accessed 3rd February 2021].

    W3schools.com. 2021. Python Numbers. [online] Available at: <https://www.w3schools.com/python/python_numbers.asp> [Accessed 28 Jan 2021].
## [02 seconds.py]

    A program that takes a string, revereses it and outputs every second letter.

### References:

    Python, G., Aytekin, C., Pieters, M., TP, S. and Iddon, J., 2021. Getting every nth character in the string in Python. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/46503865/getting-every-nth-character-in-the-string-in-python> [Accessed 3rd February 2021].

    W3schools.com. 2021. How to reverse a String in Python. [online] Available at: <https://www.w3schools.com/python/python_howto_reverse_string.asp> [Accessed 3rd February 2021].

    Docs.python.org. 2021. Built-in Functions — Python 3.9.2 documentation. [online] Available at: <https://docs.python.org/3/library/functions.html> [Accessed 3rd February 2021].
    
    
## [03 collatz.py]

    A program that takes a positive integer as input.
    The programme performs a calculation on the current value, (starting with input).
    If the value is even it is divided by two and assigned to the current value variable
    If it is odd it is multiplied by 3 and 1 is added and then the value is assigned to current value.
    The program ends when the current value is 1

## References
    Programiz.com. 2021. Python if, if...else, if...elif...else and Nested if Statement. [online] Available at: <https://www.programiz.com/
    
    python-programming/if-elif-else> [Accessed 12 February 2021].
    W3schools.com. 2021. Python While Loops. [online] Available at: <https://www.w3schools.com/python/python_while_loops.asp> [Accessed 12 February 2021].

## [04 weekday.py]

    A Programme that determines the day of the week from the system date., and outputs a message depending on whether it is a weekday or weekend.
    It can be extended to allow the user to input any date

### References:
    date?, H., Visser, S. and Ramaswamy, K., 2021. How do I get the day of week given a date?. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date> [Accessed 18 February 2021].

    Python, R., 2021. Lists and Tuples in Python – Real Python. [online] Realpython.com. Available at: <https://realpython.com/python-lists-tuples/> [Accessed 25 February 2021].

## [05 squareroot.py]

### Introduction:
    Although the learning objective of this PandD problem is to demonstrate the use of functions in python, it required using a level of maths beyond the normal scope of the programmer’s experience, Newton’s Method. It would be disingenuous, to copy and amend one the numerous examples of using python and comment the code without demonstrating an understanding of principle of Newton’s Method for approximating the square of a number and developing ones own code to that.

### To solve this PandD problem:

### 1.	Determine the meaning of Newtons method:
    ‘Newtons method is based on the geometry of a curve. The method requires that a initial guess of the root must be made, putting the guess into an equation to get a new guess and repeating the process until the root is found’. (Newton's Square Root Approximation by Ron Kurtus - Succeed in Understanding Algebra: School for Champions, 2021)
    More simplistically it can be described in repeating the following equation on a candidate number until an approximation is found
    ‘√ N ≈ ½(N/A + A)’ (Newton's Square Root Approximation by Ron Kurtus - Succeed in Understanding Algebra: School for Champions, 2021). 

    N is the number to find the square root of
    A is the guess
    If we repeat the equation using the outcome of the previous equation as the guess, we will get closer and closer to a square root.

### 2.Test Newtons Method
    N = 94
    A= 5
    1st attempt
    √ N ≈ ½(N/A + A)

    √94= .5 * (94/5+5) = 11.9
    Check: 11.9 * 11.9 = 141 – still some way off
    2nd attempt
    √94 = .5(94/11.9+11.9) = 9.8
    Check: 9.8 *9.8 = 96.04 – getting close
    3rd attempt
    √94 = .5(94/9.8+9.8) = 9.6 =92.16
    It seems that using only one decimal place the method cannot get close enough.
    3rd attempt repeated.
    √94 = .5(94/9.8+9.8) = 9.6953 
    Check: 9.6953 * 9.6953 = 93.998 Very close
    The above demonstrates that the method works, and with greater accuracy eventually find the square root.

### 3.	 Experiment with python code

    num =  4 a number to be input 
    guess = 3 a reasonable guess, in reality a number between num/2 and num
    Sqrt =  (num/guess – guess)/2
    To repeated in a loop
    While i < 50
    guess =  (num/guess – guess)/2
    i+1
    The program requires a guess, which can’t be hard coded. For this program it is half of the original number, depending on the number, the root and the degree of accuracy required, the programme will need to stop a some point. The example above gives a finite number of iterations. Easier on the processor would be to determine a level of accuracy by the size of the fraction returned and compare it to the previous interaction. The following snippet references: (python, 2021),(Break, Continue, and Pass Statements in For and While Loops | DigitalOcean, 2021)
    If abs(prevGuess – guessRoot) < .00001:
        Break
    Else
        prevGuess = guessRoot

    In the final program I have used a while True (Python While Loops, 2021) loop inside the function which returns the value when the above condition has been met.



### References
    DigitalOcean. 2021. Break, Continue, and Pass Statements in For and While Loops | DigitalOcean. [online] Available at: <https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3> [Accessed 25 February 2021].

    Brilliant.org. 2021. Newton Raphson Method | Brilliant Math & Science Wiki. [online] Available at: <https://brilliant.org/wiki/newton-raphson-method/> [Accessed 25 February 2021].

    Encyclopedia Britannica. 2021. Derivative | mathematics. [online] Available at: <https://www.britannica.com/science/derivative-mathematics> [Accessed 25 February 2021].

    Kite.com. 2021. Code Faster with Line-of-Code Completions, Cloudless Processing. [online] Available at: <https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python> [Accessed 25 February 2021].

    Method, P., Yadav, A., Yadav, A. and Yadav, A., 2021. Python Program to find the square root of a number by Newton’s Method. [online] Goeduhub Technologies. Available at: <https://www.goeduhub.com/3398/python-program-to-find-the-square-root-number-newtons-method> [Accessed 25 February 2021].
    python, N., 2021. Newton’s method for finding square roots in python. [online] Stack Overflow. Available at: <https://stackoverflow.com/questions/20811208/newton-s-method-for-finding-square-roots-in-python> [Accessed 25 February 2021].

    School-for-champions.com. 2021. Newton's Square Root Approximation by Ron Kurtus - Succeed in Understanding Algebra: School for Champions. [online] Available at: <https://www.school-for-champions.com/algebra/square_root_approx.htm#.YDd0-dzLdhF> [Accessed 25 February 2021]

    W3schools.com. 2021. Python While Loops. [online] Available at: <https://www.w3schools.com/python/python_while_loops.asp> [Accessed 25 February 2021].


## General References:
    Matthes, E., 2019. Python crash course. San Francisco, CA: No Starch Press.

    McKinney, W., 2013. Python for data analysis. Beijing [etc.]: O'Reilly.

    Programiz.com. 2021. How to get current date and time in Python?. [online] Available at: <https://www.programiz.com/python-programming/datetime/current-datetime> [Accessed 25 February 2021].

    Stackoverflow 2012, accessed 17th February 2021,<https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date>
