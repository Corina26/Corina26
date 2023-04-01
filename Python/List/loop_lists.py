#Lists are iterable objects. Therefore they can easily be used with for
# loop

# for name in iterable_object:
#       print(name) # this would print each element from given iterable object.

list = ["str1",'str2',3,4,5.6]

for item in list:
    print(item)

# Print only string objects from given list. 

for element in list:
    if type(element) == str:
        print(f"String object {element}")

# print only integer objects from given list? 

for element in list:
    if type(element) == int:
        print(f"integer objects {element}")
