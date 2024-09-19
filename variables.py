# To check the version
import sys
print(sys.version)

# To give correct indentation(4 spaces)

""" if 5 > 2:
 print('Five is greater than two!') """
# The above code generate an indentation error 

if 5 > 2:
    print("Five is greater than two!")
# The above code will run without any error. The print statement is indented with 4 spaces.


# Pyhton Variables

# Variables are containers for storing data value
# Variable names are case sensitive.

x = 5
X = 10
y = "John"

# Type Casting
# Type casting is the process of converting a variable from one data type to another.
a = int(3)
b = float(3)
c = str(3)

print(x)
print(X)
print(y)

print(a)
print(b)
print(c)

# To know type of a variable

print(type(x))
print(type(y))
print(type(a))
print(type(b))
print(type(c))


# Python Variable Names

""" A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). 
Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords. """

# Multi word variable names
# Three types are there, Camel Case (myName), Pascal Case (MyName), Snake Case (my_name)


myName = "Srinu"
my_name = "SRINU"

print(myName)
print(my_name)

# Assign Multiple Values

# Many to multiple values
a, b, c = "Srinu", "Bilwan", "Ganesh"
print(a, b, c)

# One value to multiple variables 
a = b = c = 150
print(a)
print(b)
print(c)

# To unpack a list
print("\nStages of a life: \n")
life_cycle = ["Birth","Childhood", "Adulthood", "Middleage", "Oldage", "Death"]
stage1, stage2, stage3, stage4, stage5, stage6 = life_cycle

print(stage1)
print(stage2)
print(stage3)
print(stage4)
print(stage5)
print(stage6)

#  Global and Local variable
print("\n Global and Local Variables\n ")
x = "awesome" # Global variable
y = "marvelous"

def func():
    x = "fantastic" # Local Variable
    global y
    print("Python is " + x, y)

func()
print("Python is " + x, y)

