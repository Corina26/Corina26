#Ask user to enter any string value using input function.
#Then, remove ALL THE SPACES (" ") from the given string.
#After removing the spaces from the string,
#if the string's length is odd print True, otherwise print False.


# Take input from user
input_str = input("Enter a string: ")

# Remove all spaces from the input string
input_str = input_str.replace(" ", "")

# Check if length of string is odd or even
if len(input_str) % 2 == 0:
    print(False)
else:
    print(True)