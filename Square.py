#Welcome Page
print("WELCOME TO YOUR SQUARE CALCULATOR")

#User inputs a Number
number = int(input("Enter a number to calculate its square: "))

#Function to calculate number square
def calculate_square(number):
    return number ** 2

#Calculate and display the square
square = calculate_square(number)
print(f"The square of {number} is {square}")


