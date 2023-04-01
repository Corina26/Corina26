# Ask user to enter a password
# The password should contain
# both upper and lower case letters
# If it contains both upper and lower case letter
# print True, otherwise print False. 

# We are expecting user to enter a both with lower and upper case letter
password = input("Enter a pass contains upper and lower case: ") 

# password variable will protect its value

#mouse
#               mouse        mouse      -> True
is_all_lower = password == password.lower()
# When is_all_lower False it tells that there are upper cases in str.
#
# MOUSE           MOUSE           MOUSE      -> True    
is_all_upper = password == password.upper()
#when is_all_upper False it tells us that there are lower cases in str.


# I want both of these conditions to be false
is_password_good = not is_all_lower and not is_all_upper

print("The condition of given password is", is_password_good)


