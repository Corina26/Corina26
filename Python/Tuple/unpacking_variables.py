
# Unpacking is assigning elemetn of a sequence, such as tuple or a list, to separate variables.

elements = ("word","python",12,13)
# We could unpack this tuple and assign it to individual elements.

var1, var2, var3, var4 = elements

print(var1) # word

print(var2) # python

print(var3) # 12

print(var4) # 13

# We could also use * to unpack remaining of tuple. 

# I will unpack 4 elements tuple to 3 variables. 

elements = ("word","python",12,13)

var1, var2, *var3 =  elements

print(var3)       #  12,13
print(type(var3)) # <class 'list'>






# QUESTION


values = ("laptop","cable","table","TV","light")

var1, *var2, var3 = ("laptop","cable","table","TV","light")

print(var2)        # ["cable","table","TV"]
print(type(var2))  # <class 'list'>
