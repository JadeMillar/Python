'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function.

EXAMPLE TASK:
'''
#EX) Define a function that has two parameters. Make the function add the two
#numbers together and return the result.
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that has two int parameters. Make the function subtract 
#the first parameter minus the second one. Then, return the result. Now call 
#the function.
#Print what the function returns.

def sub_two_numbers(num1, num2):
    subTwoNums = num1 - num2
    return subTwoNums

num1 = 8
num2 = 6
sub = sub_two_numbers(num1, num2)
print(sub)

#2) Define a function that has one parameter. Make the function divide the 
#parameter by 2, multiply it by 77, and then add 10,000. Return the result.
#Now call the function.
#Print what the function returns.

def equation(num):
    equation = num / 2 * 77 +10,000
    return equation
num = 5
print(equation(num))

#3) Define a function that has two int parameters. Make the function check if 
#two numbers are equal. If they are equal, return true. If they are not equal, 
#return false. Now call the function.
#Print what the function returns.
def numEqual (num1, num2):
    if (num1 == num2):
        print("true")
        return
    num1 = 10
    num2= 10
    print(numEqual)


#4) Define a function that has two int parameters. Make the function
#check which parameter is bigger, and return the bigger parameter. 
#If they are the same, it should just return either parameter. Now call the 
#function.
#Print what the function returns.

def numSize (num1, num2):
    if (num1 > num2):
        print(num1)
    if(num1 < num2):
         print(num2)
    if (num 1 == num 2):
        print(num1 or num2)
        return 
    num1 = 2
    num2 = 4
    print(numSize)

#5) Define a function that has two string parameters. Make the function
#add the two strings together. And then return the combined string. Now call 
#the function.
#Print what the function returns.

def sumTwoStrings(string1, string2):
    sumTwoStrings = ("chocolate" + "Candy")
    return
print(sumOfTwoStrings)

#6) Define a function that has three int parameters. If the first number is 
#equal to the second OR the third number, return true. Else, return false. Now 
#call the function.
#Print what the function returns.

def numEqual (num1, num2, num3):
    if(num1 == num2):
        print("true")
    elif(num 1 == num3):
        print("true")
    else: print("false")
    return 
print(numEqual)

#7) Define a function that prints your name. It should have no parameters and 
#shouldn't return anything. Now call the function.

def printName (name):
    name = "Jade"
    print(name)
    return 
print(printName)

#8) Define a function that has one string parameter. The string should be a
#color. If that string is equal to your favorite color, it prints "That's my 
#favorite color!". If it is not, it prints "That is not my favorite color. 
#Try again.". It shouldn't return anything. Now call the function.

def favColor ("blue"):
   favColor == pink
    if("blue" == "pink"):
        print("That's my favorite color!")
    else
    print("That is not my favorite color. Try again.")

#9) Define a function that has one int parameter. The int should be 
#positive. If the number is not equal to zero, the function runs a loop that
#decrements the parameter by 1 and prints it each time. Now call the function.
def loop (num1):
    if(num1 > 0):
        while (num1 > 0)
        print(num1)
        num1 -= 1
        print(num1)
        return 
    num1= 11
    print(loop)
