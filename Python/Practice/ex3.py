
# Let's create a function that takes any count of number or numbers.
# find sum of all given numbers. 
# The function can get 4 number parameter or 12 .
# in order to be flexible with amount of values (parameters),
# we could take we will use * symbol before the name.
def find_sum (*numbers):
    print(type(numbers)) # tuple
    # I should treat this numbers variable as a tuple.
    # in the tuple how can i find the sum of all numbers. 
    sum = 0
    for num in numbers:
        sum += num 
    return sum    

print(find_sum(30,20))
