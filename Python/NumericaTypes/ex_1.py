# The three digit number created below
num = 347
# Create a python code to find product of digits from that number.
# The code created should work
#  even the value of the variable num changes


product = 1
num = 347

# extract the digits of the number
digit1 = num // 100       
digit2 = (num % 100) // 10  
digit3 = num % 10        

# multiply the digits to the product
product *= digit1
product *= digit2
product *= digit3

# print the product of the digits
print("Product of digits of the number:", product)



# 2 % 10 -> 2
# 15 % 10 -> 5
# 103 % 10 -> 3
# 143 % 10 -> 3
# 97 % 10 -> 7
# when we find remainder with 10 we always get last digit 
# from that number 
# to be able to find last digit of variable num 
# last-digit = % 10

# 17 // 10 -> 
100 // 10 -> 
150 
143 

To get rid of last digits from the number i shouls use floor 
division by 10
