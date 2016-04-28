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

print("5.Square Root")

choice = int(rawinput("Enter number (1,2,3,4,5): "))

if (choice <= 4):

    num1 = int(rawinput("Enter first number: "))
    num2 = int(rawinput("Enter second number: "))


    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))

	elif choice == '2':
		print(num1,"-",num2,"=", subtract(num1,num2))

	elif choice == '3':
		print(num1,"/",num2,"=", divide(num1,num2))

	elif choice == '4':
		print(num1,"*",num2,"=", multiply(num1,num2))

if choice == '5':
	sqrnum = int(input("Enter number: "))
	print("Square root of ",sqrnum," is", math.sqrt(sqrnum))
