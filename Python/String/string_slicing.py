
#Slicing with the steps
#    0123456789
s = "Techtorial"

substr = s[3:8:2]

print(substr)

sub = s[2:4:-1]

print(sub)
print(len(sub))
# Since slicing will go from right to left because of the negative step
# the code will not be able to find index 4 after starting from
# index number 2. THerefore the variable sub will be an empty string

#    012345678910
s = "Techtorial"

substr2 = s[4:2:-1]

print(substr2) #th


# Question
print(s[:] == s)
# What will be the output of the code above?
# True
# What will be the output of the code below?


print(   s[:] == s[::1] == s == s[0:len(s):1] == s[0:len(s)]   )
# True

print(s[::-1])
#lairothceT
