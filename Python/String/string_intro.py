
# Ask user to enter a string.
# print the length of string
# print the 4th letter of the string. 

str = input("Enter a string: ")

print("The length of the text you have entered is",len(str))

print("The 4th letter of the text you have entered is",str[3])

# When the index number you are trying to access doesn't exist in str
# python will generate IndexError. 

# Print the last character from the given string without negative 
# indexing.    01234
# Example     "STRIN"
#              12345
#There are 5 characters in the string and last index is 4
# Last index can be found by subtracting 1 from the length of string.
#len(str)-1 will always result in last index from the string.
print("Last index from the str is",(len(str)-1))














