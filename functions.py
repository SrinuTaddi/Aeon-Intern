#  Functions 
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

print("\n Functions \n")

def fullname():
    fname = "Srinu"
    lname = "Taddi"
    full_name = fname + " " + lname
    return full_name


print("Full Name: ",fullname())
print("\n")

# Using Parameters & Arguments

def fullName(fname, lname):
    print("Full Name: ",fname + ' ' + lname)

fullName("Aashish", "Patil")

print("\n Using multiple arguments at once: \n")
def say_hello(*args):
    for arg in args:
        print("Hello, ", arg)

say_hello("Srinu", "Aashish", "Madhu")


print("\nCalling the function with different keyword arguments\n")

def person_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

person_details(name = "Bruce Lee", age = 32, occupation = "Actor, Martial Artist & Philoshpher.")


print("\nCalling the function with both positional and keyword arguments\n")

def both_args_kwargs(*args, **kwargs):
    print("Arguments: ",args)
    print("Keyword Arguments: ",kwargs)

both_args_kwargs("Srinu","Programming",name = "Bruce Lee", age = 32, occupation = "Actor, Martial Artist & Philoshpher.")

print("\nCalling the function with default and custom arguments\n")

def order_summary(order_type="Food", *args, **kwargs):
    print(f"Order Type: {order_type}")
    print("Items:", args)
    print("Details:", kwargs)


order_summary("Groceries","Apples", "Oranges", delivery="Fast", payment="Online Transaction")


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

print("\n Lambda Functions \n")

#  syntax  -->  lambda arguments : expression
# Higher Order Function: A function returns another function
# Closure : the function retains the value even though it already has been executed.

c = lambda b : b ** 10
print(c(2))

def lambda_func(n):
    return lambda x: x * n
func = lambda_func(5)

print(func(2))
print(func(9))

def new_lam(n):
    return lambda a: a / n 

fun = new_lam(15)
print(fun(75))


print("\n Arrays \n")

# Python does not have any built in arrays, we can use lists as arrays as well as we can import from NumPy module.