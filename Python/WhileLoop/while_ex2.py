# Ask user to enter two numbers that are not the same. 
# And print all numbers that is divisible by 3 and 8 between 
# given 2 numbers. 

num1 = int(input("Enter a positive integer number: "))
num2 = int(input("Enter a number bigger than first number: "))

# I have to check range of given numbers 
# Starting from num1 and ending at num2
while num1 < num2:
    # How can I understand if number is divisible by 3 and 8
    # When the remainder gives 0, it means we can divide that number.
    if num1 % 3 == 0 and num1 % 8 == 0:
        print(f"{num1} is divisible by 3 and 8.")
    #For condition update I could increase the value of num1
    num1 += 1
