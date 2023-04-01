
# Ask user to enter a word. 
# print True if the first and last letter of the string is same.
# Otherwise, print False

str = input("Please enter a word: ")
first_letter= str[0] #P
last_index = len(str)-1 # 1
last_letter = str[last_index] # Y

print(first_letter == last_letter)

print(type(first_letter)) #  <class 'str'>
print(type(last_letter))  #  <class 'str'>

print(type(str[1]))       #  <class 'str'>
