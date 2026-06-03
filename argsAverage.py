#Welcome message
print("WELCOME TO THE AVERAGE CALCULATOR")

#User input three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

#Function to calculate the average using *args
def calculate_average(*args):
    total = sum(args)
    count = len(args)
    average = total / count
    return average

#Calculate and display the average
average = calculate_average(num1, num2, num3)
print(f"The average of {num1}, {num2}, and {num3} is {average}.")

