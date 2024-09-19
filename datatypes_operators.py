# Python Data Types 

""" Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType """

# Random Number
#  random module 

import random 

print("\nRandom Numbers: \n")
print(random.randrange(1, 100))
print(random.randrange(100, 200))
print(random.randrange(1, 2000))

# Strings 
string = "Python is inevitable."
print(string[0:20:2])
if "inevitable" in string:
    print("Yes, it is in the string.")

print("\nString Operations: \n")

name = "I am continuosly doing this tasks for atleast 2:30 hrs."
print(name.upper())
print(name.lower())
print(name.strip())
print(name.split())
print(name.replace("I", "You").replace("am", "are"))

Name = "Srinu Taddi"
Age = 24
print(f"{Name} is {Age} year's old.")


# Boolean values 
print("\nBoolean Values: \n")
print("True and False")

a = 10
b = 5
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")

# Python Operators

'''
Arithmetic operators (+, -, *, /, %, **, //, %, **)
Assignment operators(=, +=, -=, *=, /=,	%=, //=, **=, &=, |=, ^= , >>=, <<=	, :=)
Comparison operators(==, !=, >, <, >=, <=)
Logical operators(and, or, not)
Identity operators(is, is not)
Membership operators(in, not in)
Bitwise operators(& (AND), |(OR), ^(XOR), ~(NOT), <<(left shift), >>(right shift))
'''
