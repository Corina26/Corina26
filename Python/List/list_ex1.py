# Ask user 7 times to enter different integer numbers. 
# If user doesn't give you
# integer number ask again. Create a list using these 7 different numbers.
# Print second biggest number from the list. 

# How can I create a loop that repeats 7 times? 

#I can use range object -> range(7) -> 0,1,2,3,4,5,6 -> 
# it would give 7 numbers
# Therefore loop I use with range(7) would iterate 7 times.

# What am I expecting user to give me? 
# Only digits, and it should not start with 0.

# When what user gave us is not matching with
# what we are expecting. We should ask user
# again to enter a number.
list_of_nums = []
for i in range(7):
    num = input("Enter an integer number: ")
    while not num.isnumeric() or num.startswith("0"):
       num = input("You have entered a wrong input try again: ")
    #In this line I have to add given number to list  
    num = int(num) 
    list_of_nums.append(num)

print(list_of_nums)
# Second biggest number should be smaller than biggest number in list.
# To be able to find biggest number in a list max(list)

second_highest = min(list_of_nums)

# I will for loop the list

for number in list_of_nums:
    if number > second_highest and number < max(list_of_nums):
        second_highest = number

print(second_highest)
