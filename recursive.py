#Welcome to Recursive Factorial Function
print("WELCOME TO THE RECURSIVE FACTORIAL CALCULATOR")

#User input a number
number = int(input("Enter a number to calculate its factorial: "))

#Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#Calculate and display the factorial
result = factorial(number)
print(f"The factorial of {number} is {result}")

