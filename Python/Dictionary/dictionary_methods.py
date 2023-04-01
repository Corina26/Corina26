
# values method 
laptop ={
    "brand" : "Apple",
    "model" : "Macbook Pro",
    "year"  : "2021"
    
    }
print(laptop.values())
print(type(laptop.values())) # dict_values
# NOTE: dict_values object can be easily converted to list object and 
# modified or categorized if necessary. 
list_of_values = list(laptop.values())

print(f"the value of list is {list_of_values} and the type is",type(list_of_values))

# keys method
print(laptop.keys())
print(type(laptop.keys())) # -> dict_keys
# NOTE: dict_keys object can easily be converted to set or list object. 
set_of_keys = set(laptop.keys())
print(set_of_keys)