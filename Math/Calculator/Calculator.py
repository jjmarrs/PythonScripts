import math
import operator
import functools

def printMenu():
    print("\nHello, user. What would you like to do today?")

    print("1. Addition")

    print("2. Subtraction")

    print("3. Division")

    print("4. Multiplication")

    print("5. Square Root")

    print("6. Exit")

def getAnswer():
    choice = int(input("Enter choice (1,2,3,4,5,6): "))
    while choice != 6:

        if choice < 1 or choice > 6:
            print("Please enter a number from 1 to 5.")
            break

        elif choice == 1:
            sum_list = list()
            sum_list.append(input("Enter numbers seperated by a comma: "))
            for x in sum_list:
                print sum(x)
            break

        elif choice == 2:
            subnum1 = int(input("Enter first number: "))
            subnum2 = int(input("Enter second number: "))
            print (subnum1 - subnum2)

        elif choice == 3:
            divnum1 = int(input("Enter first number: "))
            divnum2 = int(input("Enter second number: "))
            print (divnum1/divnum2)
            break

        elif choice == 4:
            mult_list = list(map(int, raw_input
                     ("Enter numbers seperated by a comma: ").split(',')))
            num = 1
            for i in mult_list:
                num *= i
                print(num)
            break

        elif choice == 5:
            sqrnum = int(raw_input("Please enter a number: "))
            result = math.sqrt(sqrnum)
            print result
            break
loop = 1
while loop:
    printMenu()
    getAnswer()

# Going to keep this program somewhat simple for now.