
#swapcase and the capitilize method


s = "python is FUN!"

#When capitilize method is used first letter will be upper, the rest
# will be in lower cases. 
print(s.capitalize())

#When swap case method is used, all cases in the string will be changed.
print(s.swapcase()) #PYTHON IS fun!

#If you want to make all words in the string starting with upper case,
# you can use the title method. Which will make only first letter of 
# words in upper case and the rest in lower case. 

print(s.title())
#Python Is Fun!


print(s) # "python is FUN!"

# Since there was no reassignment original value of the string s is 
# protected. 
# reassignment

s = "New String"

print(s) #  "New String"
