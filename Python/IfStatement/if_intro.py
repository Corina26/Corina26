
b = False
if b:
    print("The condition given is True")   

print("There is no indentation so this line is not effected by if")

# NOTE: Anything that returns(gives) boolean can be put after if.
if True:
    print("This is line #1")
    print("This is line #2")
    print("This is line #3") 

# Whenever we use comparison operators they will give us a bool value,
# therefore, we could use comparison oprs. after if keyword.



# if True:
#     print("This is line #1")
#     print("This is line #2")
#     print("This is line #3") 

#     print("This is line #5")
# print("This is line #6")
#     print("This is line #7")

# What will be the output of the code above?
# This will generate an error. 

# Indented lines want to belong a certain control 
# flow statements or methods. Such as if, while, for, def(methods) etc.










if True:
    print("This is line #1")
    print("This is line #2")
    print("This is line #3") 

    print("This is line #5")
print("This is line #6")

# Which lines will be printed? 

# line # 1,2,3,5,6

if False:
    print("This is line #1")
    print("This is line #2")
    print("This is line #3") 

    print("This is line #5")
print("This is line #6")

# Which lines will be printed? 

# Only line #6 will be printed, because it is not effected by if.
