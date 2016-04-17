import math 

def add(x,y):
	return x + y 

def subtract(x,y):
	return x - y

def divide(x,y):
	return x / y
	
def multiply(x,y): 
	return x * y

def squareRoot(x):
	return math.sqrt(x)

print("Hello, user. What would you like to do today? ")

print("1. Addition")

print("2. Subtraction")

print("3. Division")

print("4. Multiplication")

print("5.Square Root")

choice = input("Enter number (1/2/3/4/5): ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
	print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
	print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
	print(num1,"/",num3,"=", divide(num1,num2))

elif choice == '4':
	print(num1,"*",num2,"=", multiply(num1,num2))
	
elif choice == '5':
	sqrnum = int(input("Enter number: "))
	print("Square root of ",sqrnum," is", math.sqrt(sqrnum))
else: 
	print("Invalid input. Please type 1, 2, 3, 4, or 5.")



