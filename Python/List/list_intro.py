    # 0 1      2   3     4
l1 = [2, 5, True, "str", 3.14]

print(type(l1)) # <class 'list'>

print(l1[2]) # True

# print(l1[10]) # Index Error

print(type(l1[4])) # <class 'float'>

# As we practiced in string, we can get range of elements from list 

print(l1[2:12]) # [True,"str",3.14]

#When we are getting range of elements from a list, return type will be 
# another list. 
print(type(l1[2:5]))
