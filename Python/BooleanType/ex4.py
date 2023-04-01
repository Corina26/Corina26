#Calculate if the given year number is the leap year or not. 
# if it is a leap year we'll print True, if not we'll print False. 

#A leap year is a year that is evenly divisible by 4, 
# unless it is a century year (divisible by 100), 
# in which case it must also be divisible by 400 to be a leap year

# get input from user
year = int(input("Enter a year: "))

# check if the year is a leap year or not
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

# print the result
print(is_leap_year)







