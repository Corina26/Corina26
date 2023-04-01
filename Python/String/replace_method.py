# Given a string, if the first or last chars are 'z', 
# print the string without those 'z' chars, and
#  otherwise return the string unchanged.

# "zHiz" → "Hi"
# "zHi" → "Hi"
# "Hziz" → "Hzi"
# "zzHizz" → zHiz

str = input("Enter a string: ")

first_letter = str[0].replace("z","")
last_letter  = str[len(str)-1].replace('z','')

# I should get a part of string where first and last letter is
# not included. 
mid_str = str[1:len(str)-1]

end_result = first_letter + mid_str + last_letter

print("The answer is",end_result)
