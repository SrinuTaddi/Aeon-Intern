# From here onwards rather than practicing single elements, I will try to implement all the functionalities in one
""" print("\n  From here onwards rather than practicing single elements, I will try to implement all the functionalities in one. \n")

print("\n ATM Money Withdrawl \n")

customer_name = input("Enter Your Name: ")
# Pin Number initialization
pin_num = 9999
# Balance Initialization
balance = 10000
print("Welcome to ATM !")
i = 1
while i <= 3:
    pin = int(input("Enter your Pin Number: "))
    if pin == pin_num:
        print(f"Welcome, {customer_name}")
        print("Select options")
        print("1. Check Balance and 2. Withdrawl Money.")
        option = int(input("Enter your option: "))
        if option == 1:
            print(f"Your current balance is: {balance}")
            amount = int(input("Enter the amount you want to withdrawl: "))
            if amount > balance:
                print("Insufficient Balance!")
                break
            else:
                balance -= amount
                print("Your withdrawl is successful.")
                print(f"Your current balance is {balance}.")
                break
        else:
            print("Ok")
    else:
        print("Invalid Pin")
    i = i+1
else:
    print("You have entered wrong pin 3 times. Your account is blocked.")

"""

# Fizz - Buzz Program
print("\n Fizz Buzz Program \n")

for num in range(1, 150):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num) 

# We can use " continue, break, pass " for better exection of the program



