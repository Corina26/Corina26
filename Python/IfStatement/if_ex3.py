# Ask user to give you two integer numbers. 
# Find the sum of these two integer numbers. 
# If sum of these two integer is smaller than 10 
# print sum of these two numbers is 10 
# if sum of these two number is between 10 - 19 inclusive, 
# print sum of these two numbers is 20
# For all other conditions 
# print the actual sum of these two numbers. 

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
sum_of_two = num1 + num2

if sum_of_two < 10:
    print("Sum of these two numbers is 10")
elif 10<=sum_of_two<=19:
    print("Sum of these two numbers is 20")
else:
    print(f"Sum of these two numbers is {sum_of_two}")
