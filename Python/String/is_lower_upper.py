
s = "Python"

print(s.islower())
# This will print False because string has upper case letter. 

s = "python"
print(s.islower()) # True

s = "python is fun"

print(s.islower()) # True

s.upper()

print(s.isupper()) # False

s = s.upper()

print(s.isupper()) # True

# Unless reassigned value of string NEVER changes. 

# islower returns True when all LETTERS in string is lower case, 
# isupper returns True when all LETTERS in string is upper case.

#NOTE!!!!!! When there is no LETTER in string, both method will return
# False.

print("1323456".islower()) # False

print("1323456a".islower()) # True

print("1323456".isupper()) # False

print("1323456A".isupper()) # True
