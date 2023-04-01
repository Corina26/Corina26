# We need to write a program to give most efficient 
# coin exchange for given dollar amount. 
# Such as if we need to convert 
# 1 dollar in to a coin exchange you would 4 quarters.
#Coin values
# quarters is 25 cents
# dime is 10 cents
# nickel is 5 cents
# penny is one cent.
given_amount = 3.67



given_amount = 3.67

# converting the given amount into cents
cents = int(given_amount * 100)

# defining the values of coins in cents
quarter = 25
dime = 10
nickel = 5
penny = 1

# calculating the number of coins required for each denomination
num_quarters = cents // quarter
cents = cents % quarter

num_dimes = cents // dime
cents = cents % dime

num_nickels = cents // nickel
cents = cents % nickel

num_pennies = cents // penny

# printing the results
print(f"Quarters: {num_quarters} cents",cents)
print(f"Dimes: {num_dimes}")
print(f"Nickels: {num_nickels}")
print(f"Pennies: {num_pennies}")




# print() - it helps us to display output of the programming. 

Arithmetical Operators
+ - * / 

# Between the string and number we can only use 
multiplication operator
print("t"*3)
The output will be -> ttt <-

# String to String only addition operator can be used. 
print("Mac" + "Book")
The output will be -> MacBook <-

Numerical Data Types
THese are the types that will help us to store different types of numbers
in our code. 
All numerical types in python are immutable which means unless
rassigned, value of numerical types will stay the same. 

We have 3 numerical types -> 
Integer -> Store whole numbers such as -> 1,2,-3,0,12345 etc.
Float  -> Store numbers with decimal points -> 5.3,-45.6, 37.9
Complex -> Numbers with real and imaginary part. Imaginary part
of this numbers are represented by letter j.For example,
4+1j etc. 


More Arithmetic Operators

% // **
// Floor division operator -> It gives only the integer part 
of division operator. Such as, 
15/6 will result in 2.5 however 15//6 will result in 2

% Remainder(Modulus) Operator -> Remaining part of the division after
floor division operator. 
15 % 6 will be the 3 


Exponentiation will be used for finding the power of number. 
Exponentiation operator is more precedence than any other operator. 

16 / 2 ** 3 -> 2







