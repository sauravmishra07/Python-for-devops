# Fuction defination in python 

def sum_of_two_numbers():
    num1 = int(input("Enter the value of num1: "))
    num2 = int(input("Enter the value of num2: "))
    sum = num1 + num2
    print("The sum of given two numbers is: ", sum)

sum_of_two_numbers()

'''
Function to check given env is prd, stg, test or dev and print respective message
'''
def check_env(env):
    if env == "prd":
        print("Don't Deploy on Friday")
    elif env == "stg":
        print("Take backup & Test well")
    elif env == "test":
        print("Test it well")
    else: 
        print("Safe to deploy any day")

user_env = input("Enter the Environment value: ")
check_env(user_env)
