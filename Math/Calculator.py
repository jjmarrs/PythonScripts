# Simple Calculator Program

import math
import operator
import functools


print("Hello, user. What would you like to do today?")

print("1. Addition")

print("2. Subtraction")

print("3. Division")

print("4. Multiplication")

print("5. Square Root")

choice = int(input("Enter choice (1,2,3,4,5): "))

if choice < 1 or choice > 5:
    print("Please enter a number from 1 to 5.")


if choice == 1:
    sum_list = list()
    sum_list.append(input("Enter numbers seperated by a comma: "))
    for x in sum_list:
        print sum(x)

if choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print subtract(num1, num2)

if choice == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print divide(num1, num2)

if choice == 4:
    mult_list = list()
    mult_list.append(input("Enter numbers seperated by a comma: "))
    mult = functools.reduce(lambda x, y: x*y, [mult_list])
    print mult
