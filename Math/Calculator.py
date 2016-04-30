import math


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def divide(x, y):
    return x / y


def multiply(x, y):
    return x * y


def squareRoot(x):
    return math.sqrt(x)

print("Hello, user. What would you like to do today?")

print("1. Addition")

print("2. Subtraction")

print("3. Division")

print("4. Multiplication")

print("5. Square Root")

choice = int(input("Enter choice (1,2,3,4,5): "))


if choice == 1:
    num_list = list()
    num_list.append(input("Enter numbers seperated by a comma: "))
    for x in num_list:
        print sum(x)

if choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print subtract(num1, num2)
