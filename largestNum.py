#Welcome User
print("WELCOME TO THE LARGEST NUMBER FINDER")

#User input three numbers
User_num1 = int(input("Enter the first number: "))
User_num2 = int(input("Enter the second number: "))
User_num3 = int(input("Enter the third number: "))

#Function to find the largest number
def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

#Find and display the largest number
largest_number = find_largest(User_num1, User_num2, User_num3)
print(f"The largest number among {User_num1}, {User_num2}, and {User_num3} is {largest_number}.")

