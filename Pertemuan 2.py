def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4) 

def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)

# Output: Sum: 5 

def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)


# function call with two arguments
add_numbers(2, 3)

#  function call with one argument
add_numbers(a = 2)

# function call with no arguments
add_numbers() 

def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function
print(message) 

# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message) 

c = 1 # global variable

def add():
    print(c)

add()

# Output: 1 

# global variable
c = 1 

def add():

    # use of global keyword
    global c

    # increment c by 2
    c = c + 2 

    print(c)

add()

# Output: 3  

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num)) 

# import standard math module 
import math

# use math.pi to get value of pi
print("The value of pi is", math.pi) 

# import module by renaming it
import math as m

print(m.pi)

# Output: 3.141592653589793 

def main():
    print("Hello World")

if __name__=="__main__":
    main()

import os

print(os.getcwd())

# Output: C:\Program Files\PyScripter 

import os

# change directory
os.chdir('C:\\Python33')

print(os.getcwd())

Output: C:\Python33 